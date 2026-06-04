---
title: "Frontend Development"
slug: "appdev-modules-m4-frontend-dev"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-frontend-dev.md"
source_title: "Frontend Development"
tags:
  - appdev
  - modules
  - m4-frontend-dev
---

# Frontend Development

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Frontend Development

> Build a React frontend for Canton applications with TypeScript bindings and wallet integration

The frontend is the user-facing layer of your Canton application. This page uses [cn-quickstart](https://github.com/digital-asset/cn-quickstart) as a running example. cn-quickstart is a full-stack reference application that implements a software licensing workflow on Canton Network. The [cn-quickstart frontend](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/frontend) is a React application built with TypeScript and Vite. It communicates with the backend over HTTP using types generated from a shared OpenAPI schema. The patterns shown here — connecting to the backend, displaying contract data, handling authentication — apply to any Canton frontend, but the code samples are drawn directly from cn-quickstart so you can see them in a working context.

## Connecting to the Backend

In cn-quickstart, the frontend does not talk to the Ledger API directly — all ledger interactions go through the backend's REST endpoints. Canton does provide a [JSON API](/sdks-tools/api-reference/json-api) that frontends can use for direct ledger access, but the cn-quickstart architecture routes everything through the backend for separation of concerns.

The API client is configured in [`api.ts`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/api.ts) using the `openapi-client-axios` library, which reads the OpenAPI schema and produces a typed HTTP client:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import OpenAPIClientAxios from 'openapi-client-axios';
import openApi from '../../common/openapi.yaml'

const api: OpenAPIClientAxios = new OpenAPIClientAxios({
    definition: openApi as any,
    withServer: { url: '/api' },
});

api.init();

export default api;
```

The shared [`common/openapi.yaml`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/common/openapi.yaml) defines every endpoint, request body, and response shape. The `openapi-client-axios` library generates a typed `Client` interface from this spec at build time, so every API call in the frontend is type-checked against the backend's contract:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import type { Client, License } from '../openapi.d.ts';

const client: Client = await api.getClient();
const response = await client.listLicenses();  // typed as License[]
```

If the backend API changes, the frontend build breaks rather than failing silently at runtime.

## TypeScript Code Generation

The cn-quickstart frontend generates its TypeScript types from the OpenAPI spec using the `gen:openapi` script in [`package.json`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/package.json):

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "scripts": {
    "gen:openapi": "npx --yes openapicmd typegen --client ../common/openapi.yaml >| src/openapi.d.ts",
    "build": "npm run gen:openapi && tsc -b --noEmit && vite build"
  }
}
```

The `build` script runs type generation before compilation, so the TypeScript types always match the OpenAPI schema.

Separately, `dpm codegen-js` generates TypeScript types from your compiled DAR file. These types mirror your Daml templates, choices, and data types:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm codegen-js <DAR-FILES> -o <DIR>
```

Whether you use DAR-generated types depends on your architecture:

* **Fully mediated** (cn-quickstart default) -- The frontend uses OpenAPI-generated types from the backend's REST schema. The Daml-generated TypeScript types are not needed in the frontend because the backend translates between ledger concepts and REST DTOs.
* **Direct ledger access via JSON API** -- The frontend submits commands through the [JSON API](/sdks-tools/api-reference/json-api) using the Daml-generated TypeScript bindings. This gives tighter integration with the ledger but requires the frontend to handle party IDs, contract IDs, and command submission directly.

For most applications, the fully mediated approach is simpler. The JSON API approach makes sense when you want a thin or no backend layer.

## Application Structure

The cn-quickstart frontend uses React Context providers for state management. [`App.tsx`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/App.tsx) composes them at the top level:

```tsx theme={"theme":{"light":"github-light","dark":"github-dark"}}
const App: React.FC = () => {
    const AppProviders = composeProviders(
        ToastProvider,
        UserProvider,
        TenantRegistrationProvider,
        AppInstallProvider,
        LicenseProvider
    );

    return (
        <AppProviders>
            <Header />
            <main className="container mt-4">
                <Routes>
                    <Route path="/" element={<HomeView />} />
                    <Route path="/tenants" element={<TenantRegistrationView />} />
                    <Route path="/login" element={<LoginView />} />
                    <Route path="/app-installs" element={<AppInstallsView />} />
                    <Route path="/licenses" element={<LicensesView />} />
                </Routes>
            </main>
            <ToastNotification />
        </AppProviders>
    );
};
```

Each domain has its own store under [`stores/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/frontend/src/stores) that wraps a React Context with the API calls and state for that domain. The stores use the typed `Client` from the OpenAPI schema for all backend communication.

## Displaying Contract Data

The frontend fetches contract data from the backend's GET endpoints and renders it in React components. The [`licenseStore`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/stores/licenseStore.tsx) manages license state and API calls:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
export const LicenseProvider = ({ children }: { children: React.ReactNode }) => {
    const [licenses, setLicenses] = useState<License[]>([]);
    const toast = useToast();

    const fetchLicenses = useCallback(
        withErrorHandling(`Fetching Licenses`)(async () => {
            const client: Client = await api.getClient();
            const response = await client.listLicenses();
            setLicenses(response.data);
        }), [withErrorHandling, setLicenses, toast]);

    // ... other operations (renew, expire, complete renewal)

    return (
        <LicenseContext.Provider value={{ licenses, fetchLicenses, /* ... */ }}>
            {children}
        </LicenseContext.Provider>
    );
};
```

[`LicensesView.tsx`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/views/LicensesView.tsx) consumes this store and renders the data with periodic polling to keep the UI current:

```tsx theme={"theme":{"light":"github-light","dark":"github-dark"}}
const LicensesView: React.FC = () => {
    const { licenses, fetchLicenses, initiateLicenseRenewal,
            initiateLicenseExpiration, completeLicenseRenewal } = useLicenseStore();
    const { user } = useUserStore();

    useEffect(() => {
        fetchLicenses();
        const intervalId = setInterval(() => {
            fetchLicenses();
        }, 5000);
        return () => clearInterval(intervalId);
    }, [fetchLicenses]);

    return (
        <div>
            <h2>Licenses</h2>
            <table className="table table-fixed" id="licenses-table">
                <thead>
                    <tr>
                        <th>License Contract ID</th>
                        <th>Expires At</th>
                        <th>License #</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {licenses.map((license) => (
                        <tr key={license.contractId}>
                            <td>{license.contractId}</td>
                            <td>{formatDateTime(license.expiresAt)}</td>
                            <td>{license.licenseNum}</td>
                            <td>{license.isExpired ? 'EXPIRED' : 'ACTIVE'}</td>
                            <td>
                                {/* Renew, Archive buttons */}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};
```

Because the backend handles all ledger translation, the frontend works with plain JSON objects. Fields like `contractId`, `expiresAt`, and `licenseNum` appear as simple strings and numbers in the `License` type — not ledger-specific types.

## Exercising Choices via the Backend

When the user takes an action (renew a license, expire a license), the frontend posts to the backend's REST API. Each request includes a unique command ID that the backend passes to the Ledger API for deduplication. From the license store:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const expireLicense = useCallback(
    withErrorHandling(`Archiving License`)(async (contractId: string, meta: Metadata) => {
        const client: Client = await api.getClient();
        const commandId = generateCommandId();
        await client.expireLicense({ contractId, commandId }, { meta });
        await fetchLicenses();
        toast.displaySuccess('License archived successfully');
    }),
    [withErrorHandling, fetchLicenses, toast]
);
```

The [`generateCommandId()`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/utils/commandId.ts) utility produces a UUID using the browser's `crypto.randomUUID()` API. The backend forwards this ID to the Ledger API, which uses it to prevent duplicate command submission if the user retries an action.

## Authentication

Canton applications typically use OAuth2 / OpenID Connect (OIDC) for user authentication. On LocalNet, cn-quickstart uses Keycloak as the identity provider. The backend handles the OAuth2 flow, and the frontend manages session state through the [`userStore`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/stores/userStore.tsx):

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
export const UserProvider = ({ children }: { children: React.ReactNode }) => {
    const [user, setUser] = useState<AuthenticatedUser | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

    const fetchUser = useCallback(async () => {
        setLoading(true);
        try {
            const client: Client = await api.getClient();
            const response = await client.getAuthenticatedUser();
            setUser(response.data);
        } catch (error) {
            if ((error as any)?.response?.status === 401) {
                setUser(null);
            } else {
                toast.displayError('Error fetching user');
            }
        } finally {
            setLoading(false);
        }
    }, [setUser, setLoading, toast]);

    const logout = useCallback(async () => {
        const response = await fetch('/api/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-XSRF-TOKEN': getCsrfToken(),
            },
        });
        if (response.ok) {
            clearUser();
            navigate('/');
        }
    }, [clearUser, toast, navigate]);

    return (
        <UserContext.Provider value={{ user, loading, fetchUser, clearUser, logout }}>
            {children}
        </UserContext.Provider>
    );
};
```

The `AuthenticatedUser` type (from the OpenAPI spec) includes the user's name, whether they're an admin, and their wallet URL. Components use this to conditionally render admin-only features and to link to the Splice wallet. The backend handles all authorization decisions — the frontend is responsible only for checking whether the user is logged in and displaying the appropriate UI.

## Wallet Integration

Applications that involve Canton Coin payments integrate with a wallet component in the frontend. In cn-quickstart, the license renewal flow triggers a payment through the Splice wallet system:

1. The user clicks "Renew License" in the UI
2. The frontend calls `client.renewLicense()`, which posts to the backend
3. The backend exercises the `License_Renew` choice, creating a `LicenseRenewalRequest` on the ledger that implements the Splice `AllocationRequest` interface
4. The Splice wallet detects the allocation request and creates an `AppPaymentRequest` for the user to approve
5. Once payment is confirmed, the provider calls `completeLicenseRenewal()` to create the renewed license

The `LicensesView` tracks renewal state by polling. Each license object includes its `renewalRequests` array, and the UI shows the count of pending and accepted renewals. The user's wallet URL comes from the `AuthenticatedUser` object and is used to link to the Splice wallet for payment approval.

## Development Workflow

When developing the frontend iteratively:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make build-frontend   # Rebuild after source changes
make restart          # Restart services to pick up changes
```

For faster iteration, run the Vite dev server directly against a running LocalNet backend:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make start-vite-dev
```

The Vite dev server proxies API requests to the backend. The proxy configuration in [`vite.config.ts`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/vite.config.ts) routes `/api`, `/login`, and `/oauth2` paths to the backend:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
export default defineConfig(({ mode }: ConfigEnv) => {
    const env = loadEnv(mode, '../');
    const backendPort = env.VITE_BACKEND_PORT || 8080;
    return {
        plugins: [react(), ViteYaml()],
        server: {
            host: 'localhost',
            strictPort: true,
            allowedHosts: ['app-provider.localhost'],
            proxy: {
                '/api': {
                    target: `http://localhost:${backendPort}/`,
                    changeOrigin: false,
                    rewrite: path => path.replace(/^\/api/, ''),
                },
                '/login': {
                    target: `http://localhost:${backendPort}/`,
                    changeOrigin: false,
                },
                '/oauth2': {
                    target: `http://localhost:${backendPort}/`,
                    changeOrigin: false,
                },
            },
        },
    }
});
```

The `ViteYaml` plugin allows importing the OpenAPI YAML file directly as a JavaScript module, which is how `api.ts` loads the schema at build time.

## Exercise: Add License Comments UI

<Note>
  This exercise builds on the backend exercise in [Backend Development](/appdev/modules/m4-backend-dev#exercise-add-license-comments). Complete that first — you need the `LicenseComment` Daml template, the OpenAPI endpoints, and the backend implementation before the frontend can use them.
</Note>

You'll add a comment list and comment form to the licenses view, following the same store/view patterns that cn-quickstart uses for licenses.

### Step 1: Regenerate TypeScript Types

The backend exercise added `LicenseComment`, `AddCommentRequest`, and two new endpoints to `openapi.yaml`. Regenerate the frontend types so the typed client picks them up:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
npm run gen:openapi
```

This runs `openapicmd typegen` against the shared `openapi.yaml` and overwrites `src/openapi.d.ts`. After this, your `Client` type will include `listLicenseComments()` and `addLicenseComment()` methods with the correct parameter and return types.

### Step 2: Create a Comment Store

Create a new store at `quickstart/frontend/src/stores/commentStore.tsx`. Follow the same Context + Provider pattern used by [`licenseStore.tsx`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/stores/licenseStore.tsx):

```tsx theme={"theme":{"light":"github-light","dark":"github-dark"}}
import React, { createContext, useContext, useState, useCallback } from 'react';
import { useToast } from './toastStore';
import api from '../api';
import { generateCommandId } from '../utils/commandId';
import type { Client, LicenseComment } from '../openapi.d.ts';
import { withErrorHandling } from '../utils/error';

interface CommentContextType {
    comments: LicenseComment[];
    fetchComments: (contractId: string) => Promise<void>;
    addComment: (contractId: string, body: string) => Promise<void>;
}

const CommentContext = createContext<CommentContextType | undefined>(undefined);

export const CommentProvider = ({ children }: { children: React.ReactNode }) => {
    const [comments, setComments] = useState<LicenseComment[]>([]);
    const toast = useToast();

    const fetchComments = useCallback(
        withErrorHandling('Fetching Comments')(async (contractId: string) => {
            const client: Client = await api.getClient();
            const response = await client.listLicenseComments({ contractId });
            setComments(response.data);
        }),
        [withErrorHandling, setComments, toast]
    );

    const addComment = useCallback(
        withErrorHandling('Adding Comment')(async (contractId: string, body: string) => {
            const client: Client = await api.getClient();
            const commandId = generateCommandId();
            await client.addLicenseComment({ contractId, commandId }, { body });
            await fetchComments(contractId);
            toast.displaySuccess('Comment added successfully');
        }),
        [withErrorHandling, fetchComments, toast]
    );

    return (
        <CommentContext.Provider value={{ comments, fetchComments, addComment }}>
            {children}
        </CommentContext.Provider>
    );
};

export const useCommentStore = () => {
    const context = useContext(CommentContext);
    if (context === undefined) {
        throw new Error('useCommentStore must be used within a CommentProvider');
    }
    return context;
};
```

The structure mirrors `licenseStore.tsx`: a React Context holds the state, each API call is wrapped with `withErrorHandling` (which displays toast messages on HTTP errors) and `useCallback`, and the typed `Client` provides compile-time checking against the OpenAPI spec. The `addComment` function generates a command ID for deduplication — the same pattern `expireLicense` and `renewLicense` use.

Register the provider in `App.tsx` alongside the existing providers:

```tsx theme={"theme":{"light":"github-light","dark":"github-dark"}}
const AppProviders = composeProviders(
    ToastProvider,
    UserProvider,
    TenantRegistrationProvider,
    AppInstallProvider,
    LicenseProvider,
    CommentProvider       // add this
);
```

### Step 3: Add the Comment UI

Add a comment section to [`LicensesView.tsx`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/views/LicensesView.tsx). You'll need to import the comment store and add some local state:

```tsx theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { useCommentStore } from '../stores/commentStore';

// inside the component:
const { comments, fetchComments, addComment } = useCommentStore();
const [showComments, setShowComments] = useState<string | null>(null);
const [commentBody, setCommentBody] = useState('');
```

Add an effect that polls for comments when a license's comment panel is open. This follows the same 5-second `setInterval` pattern `LicensesView` already uses for the license list:

```tsx theme={"theme":{"light":"github-light","dark":"github-dark"}}
useEffect(() => {
    if (showComments) {
        fetchComments(showComments);
        const intervalId = setInterval(() => fetchComments(showComments), 5000);
        return () => clearInterval(intervalId);
    }
}, [showComments, fetchComments]);
```

Add a "Comments" toggle button in each license row's actions column, and render the comment panel below the license table. The panel shows existing comments and a form for new ones:

```tsx theme={"theme":{"light":"github-light","dark":"github-dark"}}
{showComments && (
    <div className="mt-4 card p-3">
        <h4>
            Comments for License #
            {licenses.find(l => l.contractId === showComments)?.licenseNum}
        </h4>
        {comments.length === 0 ? (
            <p className="text-muted">No comments yet.</p>
        ) : (
            <ul className="list-group mb-3">
                {comments.map((c) => (
                    <li key={c.contractId} className="list-group-item">
                        <strong>{c.commenter}</strong>
                        <span className="text-muted ms-2">
                            {formatDateTime(c.createdAt)}
                        </span>
                        <p className="mb-0 mt-1">{c.body}</p>
                    </li>
                ))}
            </ul>
        )}
        <form onSubmit={handleAddComment} className="d-flex gap-2">
            <input
                className="form-control"
                value={commentBody}
                onChange={(e) => setCommentBody(e.target.value)}
                placeholder="Add a comment..."
            />
            <button type="submit" className="btn btn-primary"
                    disabled={!commentBody.trim()}>
                Post
            </button>
        </form>
    </div>
)}
```

The `showComments` state tracks which license's contract ID is currently expanded. The `formatDateTime` utility is already imported in `LicensesView` for the expiration column. The `handleAddComment` handler calls `addComment` from the store, then clears the input.

### Step 4: Build and Test

Rebuild both the backend (to pick up the OpenAPI changes and new Java code) and the frontend:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make build-frontend   # runs npm run gen:openapi && tsc && vite build
make build-backend    # runs ./gradlew :backend:build
make restart          # restart all services
```

Or for faster frontend iteration with hot reload:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make start-vite-dev
```

Open the app, navigate to the Licenses page, click the "Comments" button on a license, and try posting a comment. The comment should appear in the list within 5 seconds (or immediately after the POST completes, since `addComment` calls `fetchComments` after success).

## Next Steps

* [Canton Coin and Traffic](/appdev/modules/m4-canton-coin) -- How CC and traffic affect your application
* [Backend Development](/appdev/modules/m4-backend-dev) -- The backend that the frontend communicates with
* [cn-quickstart frontend source](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/frontend) -- Full working frontend implementation

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
