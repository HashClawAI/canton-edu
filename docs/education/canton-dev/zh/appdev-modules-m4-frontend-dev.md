---
title: "前端开发"
slug: "appdev-modules-m4-frontend-dev"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-frontend-dev.md"
source_title: "Frontend Development"
tags:
  - appdev
  - modules
  - m4-frontend-dev
---

# 前端开发

> 使用 TypeScript 绑定与钱包集成构建 Canton 应用的 React 前端

前端是 Canton 应用面向用户的层。本节以 [cn-quickstart](https://github.com/digital-asset/cn-quickstart) 为示例。cn-quickstart 是在 Canton Network 上实现软件许可工作流的全栈参考应用。[cn-quickstart 前端](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/frontend) 是用 TypeScript 与 Vite 构建的 React 应用，通过共享 OpenAPI schema 生成的类型经 HTTP 与后端通信。此处模式——连接后端、展示合约数据、处理认证——适用于任何 Canton 前端，代码样例直接来自 cn-quickstart 以便在可运行上下文中查看。

## 连接后端

cn-quickstart 中前端不直接连接 Ledger API——所有账本交互经后端 REST 端点。Canton 提供 [JSON API](/sdks-tools/api-reference/json-api) 供前端直接访问账本，但 cn-quickstart 架构为关注点分离将所有流量路由经后端。

API 客户端在 [`api.ts`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/api.ts) 中用 `openapi-client-axios` 配置，读取 OpenAPI schema 并生成类型化 HTTP 客户端：

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

共享 [`common/openapi.yaml`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/common/openapi.yaml) 定义每个端点、请求体与响应形状。`openapi-client-axios` 在构建时从该 spec 生成类型化 `Client` 接口，前端每次 API 调用都经类型检查与后端契约对齐：

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import type { Client, License } from '../openapi.d.ts';

const client: Client = await api.getClient();
const response = await client.listLicenses();  // typed as License[]
```

后端 API 变更时，前端构建会失败而非运行时静默出错。

## TypeScript 代码生成

cn-quickstart 前端用 [`package.json`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/package.json) 中的 `gen:openapi` 脚本从 OpenAPI spec 生成 TypeScript 类型：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "scripts": {
    "gen:openapi": "npx --yes openapicmd typegen --client ../common/openapi.yaml >| src/openapi.d.ts",
    "build": "npm run gen:openapi && tsc -b --noEmit && vite build"
  }
}
```

`build` 脚本在编译前运行类型生成，TypeScript 类型始终与 OpenAPI schema 一致。

另外，`dpm codegen-js` 从已编译 DAR 生成 TypeScript 类型，镜像 Daml template、choice 与数据类型：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm codegen-js <DAR-FILES> -o <DIR>
```

是否使用 DAR 生成类型取决于架构：

* **完全中介**（cn-quickstart 默认）— 前端使用后端 REST schema 的 OpenAPI 生成类型。前端不需要 Daml 生成的 TypeScript 类型，因后端在账本概念与 REST DTO 间翻译。
* **经 JSON API 直接访问账本** — 前端通过 [JSON API](/sdks-tools/api-reference/json-api) 用 Daml 生成的 TypeScript 绑定提交命令。与账本集成更紧，但需前端处理 party ID、contract ID 与命令提交。

多数应用完全中介更简单。JSON API 方式适合希望薄后端或无后端的场景。

## 应用结构

cn-quickstart 前端用 React Context provider 管理状态。[`App.tsx`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/App.tsx) 在顶层组合：

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

每个域在 [`stores/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/frontend/src/stores) 下有独立 store，用 React Context 包装该域的 API 调用与状态。store 使用 OpenAPI schema 的类型化 `Client` 进行所有后端通信。

## 展示合约数据

前端从后端 GET 端点获取合约数据并在 React 组件中渲染。[`licenseStore`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/stores/licenseStore.tsx) 管理许可证状态与 API 调用：

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

[`LicensesView.tsx`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/views/LicensesView.tsx) 消费该 store 并定期轮询保持 UI 最新：

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

因后端处理全部账本翻译，前端使用 plain JSON 对象。`contractId`、`expiresAt`、`licenseNum` 等字段在 `License` 类型中为简单字符串与数字——非账本专用类型。

## 经后端行使 Choice

用户操作（续期、归档许可证）时，前端 POST 到后端 REST API。每个请求含唯一 command ID，后端传给 Ledger API 用于去重。来自 license store：

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

[`generateCommandId()`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/utils/commandId.ts) 用浏览器 `crypto.randomUUID()` 生成 UUID。后端将该 ID 转发给 Ledger API，防止用户重试时重复提交。

## 认证

Canton 应用通常用 OAuth2 / OpenID Connect（OIDC）做用户认证。LocalNet 上 cn-quickstart 用 Keycloak 作身份提供方。后端处理 OAuth2 流程，前端通过 [`userStore`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/stores/userStore.tsx) 管理会话状态：

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

`AuthenticatedUser` 类型（来自 OpenAPI spec）含用户名、是否 admin、钱包 URL。组件据此条件渲染 admin 功能并链接 Splice 钱包。授权决策由后端负责——前端仅检查登录状态并显示相应 UI。

## 钱包集成

涉及 Canton Coin 支付的应用在前端集成钱包组件。cn-quickstart 中许可证续期经 Splice 钱包系统触发支付：

1. 用户在 UI 点击「Renew License」
2. 前端调用 `client.renewLicense()` POST 到后端
3. 后端行使 `License_Renew` choice，在账本上创建实现 Splice `AllocationRequest` 接口的 `LicenseRenewalRequest`
4. Splice 钱包检测到分配请求，创建 `AppPaymentRequest` 供用户批准
5. 支付确认后，提供方调用 `completeLicenseRenewal()` 创建续期许可证

`LicensesView` 通过轮询跟踪续期状态。每个 license 对象含 `renewalRequests` 数组，UI 显示待处理与已接受续期数量。用户钱包 URL 来自 `AuthenticatedUser`，用于链接 Splice 钱包批准支付。

## 开发工作流

迭代开发前端时：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make build-frontend   # 源码变更后重建
make restart          # 重启服务以加载变更
```

更快迭代可对运行中的 LocalNet 后端直接运行 Vite 开发服务器：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make start-vite-dev
```

Vite 开发服务器将 API 请求代理到后端。[`vite.config.ts`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/vite.config.ts) 中的代理配置将 `/api`、`/login`、`/oauth2` 路由到后端：

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

`ViteYaml` 插件允许将 OpenAPI YAML 直接作为 JavaScript 模块导入，`api.ts` 据此在构建时加载 schema。

## 练习：添加许可证评论 UI

<Note>
  本练习基于 [后端开发](/appdev/modules/m4-backend-dev#exercise-add-license-comments) 中的后端练习。请先完成该练习——需要 `LicenseComment` Daml template、OpenAPI 端点与后端实现后前端才能使用。
</Note>

你将在许可证视图中添加评论列表与评论表单，遵循 cn-quickstart 用于许可证的 store/view 模式。

### 步骤 1：重新生成 TypeScript 类型

后端练习在 `openapi.yaml` 中添加了 `LicenseComment`、`AddCommentRequest` 与两个新端点。重新生成前端类型以便类型化客户端识别：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
npm run gen:openapi
```

对共享 `openapi.yaml` 运行 `openapicmd typegen` 并覆盖 `src/openapi.d.ts`。之后 `Client` 类型将含 `listLicenseComments()` 与 `addLicenseComment()` 及正确参数与返回类型。

### 步骤 2：创建 Comment Store

在 `quickstart/frontend/src/stores/commentStore.tsx` 创建新 store，遵循 [`licenseStore.tsx`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/stores/licenseStore.tsx) 的 Context + Provider 模式：

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

结构与 `licenseStore.tsx` 一致：React Context 持有状态，每个 API 调用用 `withErrorHandling`（HTTP 错误时显示 toast）与 `useCallback` 包装，类型化 `Client` 提供 OpenAPI spec 的编译时检查。`addComment` 生成 command ID 用于去重——与 `expireLicense`、`renewLicense` 相同模式。

在 `App.tsx` 与现有 provider 一并注册：

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

### 步骤 3：添加评论 UI

在 [`LicensesView.tsx`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/frontend/src/views/LicensesView.tsx) 添加评论区。需导入 comment store 并添加本地状态：

```tsx theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { useCommentStore } from '../stores/commentStore';

// inside the component:
const { comments, fetchComments, addComment } = useCommentStore();
const [showComments, setShowComments] = useState<string | null>(null);
const [commentBody, setCommentBody] = useState('');
```

添加 effect：当某许可证评论面板打开时轮询评论，遵循 `LicensesView` 对许可证列表使用的 5 秒 `setInterval` 模式：

```tsx theme={"theme":{"light":"github-light","dark":"github-dark"}}
useEffect(() => {
    if (showComments) {
        fetchComments(showComments);
        const intervalId = setInterval(() => fetchComments(showComments), 5000);
        return () => clearInterval(intervalId);
    }
}, [showComments, fetchComments]);
```

在每行许可证操作列添加「Comments」切换按钮，在许可证表下方渲染评论面板，展示已有评论与新评论表单：

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

`showComments` 状态跟踪当前展开的许可证 contract ID。`formatDateTime` 工具已在 `LicensesView` 中用于过期列。`handleAddComment` 调用 store 的 `addComment` 后清空输入。

### 步骤 4：构建与测试

重建后端（加载 OpenAPI 变更与新 Java 代码）与前端：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make build-frontend   # runs npm run gen:openapi && tsc && vite build
make build-backend    # runs ./gradlew :backend:build
make restart          # restart all services
```

或更快的前端热重载迭代：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make start-vite-dev
```

打开应用，进入 Licenses 页，点击某许可证的「Comments」并尝试发表评论。评论应在 5 秒内出现在列表中（或 POST 成功后立即出现，因 `addComment` 成功后会调用 `fetchComments`）。

## 下一步

* [Canton Coin 与 Traffic](/appdev/modules/m4-canton-coin) — CC 与 traffic 如何影响应用
* [后端开发](/appdev/modules/m4-backend-dev) — 前端通信的后端
* [cn-quickstart 前端源码](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/frontend) — 完整可运行前端实现

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
