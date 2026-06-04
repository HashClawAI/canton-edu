---
title: "Keycloak Configuration Guide for Canton Validator (Community)"
slug: "global-synchronizer-deployment-community-keycloak-config"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/community-keycloak-config.md"
source_title: "Keycloak Configuration Guide for Canton Validator (Community)"
tags:
  - global-synchronizer
  - deployment
  - community-keycloak-config
---

# Keycloak Configuration Guide for Canton Validator (Community)

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Keycloak Configuration Guide for Canton Validator (Community)

> Community-contributed end-to-end Keycloak configuration guide for Canton validators

<Warning>
  This section features solutions shared by community members. While they haven't been formally tested by the Splice maintainers, users are encouraged to verify the information independently. Contributions to enhance accuracy and completeness are always welcome.
</Warning>

To deploy a validator node with Keycloak authentication, follow these detailed configuration steps. This guide provides comprehensive instructions for setting up Keycloak as your validator's OIDC provider, including all required customizations for your Canton network deployment.

For additional authentication providers and configuration details, see Configuring Authentication.

## Prerequisites

Before proceeding with the configuration, ensure you have:

* A running Keycloak instance with administrative access
* Admin Console access to your Keycloak deployment
* The following hostnames configured:
  * Validator API base URL: `https://validator-api.your-domain.example/api`
  * Wallet UI: `https://wallet.your-domain.example`
  * CNS UI: `https://cns.your-domain.example`
* Your assigned `PARTY_HINT` identifier from the Canton network

## Realm Configuration

1. Create the realm for your Canton validator.
   1. Navigate to **Admin Console** → **Manage realms** → **Create realm**.
   2. Set **Realm name** to `canton` (or your environment-specific name).
   3. Click **Create** to initialize the realm.
2. Configure session settings for offline access and refresh tokens.
   1. Navigate to **Realm Settings** → **Sessions**.
   2. Configure the following settings:
      * Set **Offline Session Max Limited** to `ON`
      * Set **Offline Session Max** to `5,184,000` seconds (60 days; adjust as desired)
      * Set **Offline Session Idle Timeout** to `2,592,000` seconds (30 days; adjust as desired)
   3. Click **Save** to apply the changes.

## Client Scopes Setup

3. Create the `daml_ledger_api` client scope.
   1. Navigate to **Client Scopes** → **Create**.

   2. Configure the basic settings:

      * **Name**: `daml_ledger_api`
      * **Protocol**: `OpenID Connect`
      * **Type**: `Default`
      * **Display on consent screen**: `OFF`
      * **Include in token scope**: `OFF`

   3. Click **Save**.

   4. Add the required mappers to `daml_ledger_api`:

      **User Client Role mapper:**

      * Navigate to **daml\_ledger\_api** → **Mappers** → **Create**
      * Set **Mapper Type** to `User Client Role`
      * Set **Name** to `daml_ledger_api_scope`
      * Set **Add to access token** to `ON`
      * Set **Add to ID token**, **Add to userinfo**, **Add to token introspection**, and **Multivalued** to `OFF`
      * Click **Save**

      **Audience mapper:**

      * Navigate to **daml\_ledger\_api** → **Mappers** → **Create**
      * Set **Mapper Type** to `Audience`
      * Set **Name** to `audience`
      * Set **Included Custom Audience** to `https://canton.network.global`
      * Set **Add to access token** and **Add to token introspection** to `ON`
      * Set **Add to ID token** and **Add to lightweight access token** to `OFF`
      * Click **Save**
4. Create the `openid` client scope.
   1. Navigate to **Client Scopes** → **Create**.

   2. Configure the settings:

      * **Name**: `openid`
      * **Protocol**: `OpenID Connect`
      * **Type**: `Default`
      * **Display on consent screen**: `OFF`
      * **Include in token scope**: `ON`

   3. Click **Save**.

   4. Add the required mappers to `openid`:

      **Validator API Audience mapper:**

      * Navigate to **openid** → **Mappers** → **Create**
      * Set **Mapper Type** to `Audience`
      * Set **Name** to `aud`
      * Set **Included Custom Audience** to `https://validator-api.your-domain.example/api`
      * Set **Add to access token** and **Add to token introspection** to `ON`
      * Set **Add to ID token** and **Add to lightweight access token** to `OFF`
      * Click **Save**

      **Subject mapper:**

      * Navigate to **openid** → **Mappers** → **Create**
      * Set **Mapper Type** to `Subject (sub)`
      * Set **Name** to `sub`
      * Set **Add to access token** and **Add to token introspection** to `ON`
      * Set **Add to lightweight access token** to `OFF`
      * Click **Save**

## Client Configuration

5. Create the ledger API resource client.
   1. Navigate to **Clients** → **Create client**.
   2. Set **Client Type** to `OpenID Connect` and **Client ID** to `ledger-api`.
   3. Click **Next**.
   4. In **Capability config**, set all toggles to `OFF`.
   5. Click **Next**.
   6. Leave all **Login settings** fields empty and click **Save**.
   7. Add the client scope: Navigate to **Client scopes** → **Add client scope** → Select `daml_ledger_api` → **Add as "Default"**.
6. Create the validator app backend service account client.
   1. Navigate to **Clients** → **Create client**.
   2. Set **Client Type** to `OpenID Connect` and **Client ID** to `validator-app-backend`.
   3. Click **Next**.
   4. In **Capability config**:
      * Set **Client authentication** to `ON`
      * Set **Service accounts** to `ON`
      * Set all other options to `OFF`
   5. Click **Next**.
   6. Leave **Login settings** fields empty and click **Save**.
   7. Record the credentials:
      * From the **Credentials tab**, copy the **Client Secret**
      * From the **Service account roles tab**, click the service account user link
      * Copy the **user ID (UUID)** from the browser URL (use as `LEDGER_API_ADMIN_USER`)
   8. Add the client scope: Navigate to **Client scopes** → **Add client scope** → Select `daml_ledger_api` → **Add as "Default"**.
7. Create the wallet web UI public client.
   1. Navigate to **Clients** → **Create client**.
   2. Set **Client Type** to `OpenID Connect` and **Client ID** to `wallet-web-ui`.
   3. Click **Next**.
   4. In **Capability config**:
      * Set **Standard flow** to `ON`
      * Set all other options to `OFF`
   5. Click **Next**.
   6. Configure **Login settings**:
      * **Valid redirect URIs**: `https://wallet.your-domain.example/*`
      * **Valid post logout redirect URIs**: `https://wallet.your-domain.example`
      * **Web origins**: `https://wallet.your-domain.example`
   7. Click **Save**.
   8. Configure client scopes:
      * Add `openid` and `daml_ledger_api` as **"Default"**
      * Add `offline_access` as **"Optional"** (if needed)
8. Create the CNS UI public client.
   1. Follow the same process as the wallet web UI with these modifications:
      * Set **Client ID** to `cns-ui`
      * Set **Valid redirect URIs** to `https://cns.your-domain.example/*`
      * Set **Valid post logout redirect URIs** to `https://cns.your-domain.example`
      * Set **Web origins** to `https://cns.your-domain.example`
      * Configure the same client scopes as wallet-web-ui

## User Management

9. Create the operator wallet user.
   1. Navigate to **Users** → **Add user**.
   2. Configure the user:
      * Set **Username** to your exact `PARTY_HINT` value
      * Set **User Enabled** to `ON`
   3. Click **Save**.
   4. Set a permanent password: Navigate to **Credentials tab** → Set password with **Temporary** set to `OFF`.
   5. Copy the **user ID (UUID)** from the browser URL (use as `WALLET_ADMIN_USER`).

<Warning>
  The username must exactly match your assigned `PARTY_HINT` identifier from the Canton network.
</Warning>

## Application Configuration

Configure your validator application using the following Keycloak-related environment variables:

# Keycloak Realm Endpoints

AUTH\_URL=[https://your-keycloak-host/realms/canton](https://your-keycloak-host/realms/canton)
AUTH\_WELLKNOWN\_URL=[https://your-keycloak-host/realms/canton/.well-known/openid-configuration](https://your-keycloak-host/realms/canton/.well-known/openid-configuration)
AUTH\_JWKS\_URL=[https://your-keycloak-host/realms/canton/protocol/openid-connect/certs](https://your-keycloak-host/realms/canton/protocol/openid-connect/certs)

# Backend Client Credentials

VALIDATOR\_AUTH\_CLIENT\_ID=validator-app-backend
VALIDATOR\_AUTH\_CLIENT\_SECRET=REPLACE\_WITH\_CLIENT\_SECRET

# User Identity UUIDs (from Keycloak Users URLs)

LEDGER\_API\_ADMIN\_USER=REPLACE\_WITH\_SERVICE\_ACCOUNT\_USER\_UUID
WALLET\_ADMIN\_USER=REPLACE\_WITH\_OPERATOR\_USER\_UUID

# OAuth Scopes and Audiences

LEDGER\_API\_AUTH\_SCOPE=daml\_ledger\_api
LEDGER\_API\_AUTH\_AUDIENCE=[https://canton.network.global](https://canton.network.global)
VALIDATOR\_AUTH\_AUDIENCE=[https://validator-api.your-domain.example/api](https://validator-api.your-domain.example/api)

# UI Client IDs

WALLET\_UI\_CLIENT\_ID=wallet-web-ui
ANS\_UI\_CLIENT\_ID=cns-ui

## Validation and Testing

10. Verify your configuration by testing the backend client credentials flow:

    curl -X POST "[https://your-keycloak-host/realms/canton/protocol/openid-connect/token](https://your-keycloak-host/realms/canton/protocol/openid-connect/token)" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "grant\_type=client\_credentials" \
    -d "client\_id=validator-app-backend" \
    -d "client\_secret=YOUR\_CLIENT\_SECRET"

    Decode the returned `access_token` and verify it contains:

    * `aud`: `["https://canton.network.global"]`
    * `scope`: `"daml_ledger_api"`

## Configuration Notes

<Note>
  * **User Identifiers**: Both `LEDGER_API_ADMIN_USER` and `WALLET_ADMIN_USER` must be UUIDs from Keycloak URLs, not usernames
  * **Mapper Configuration**: The `daml_ledger_api` scope uses both User Client Role and Audience mappers for comprehensive authorization
  * **Token Audiences**: UI tokens contain both standard OpenID Connect claims and your validator API audience
  * **Username Matching**: The wallet admin user's username must exactly match your `PARTY_HINT` value
</Note>

## Troubleshooting

If you encounter authentication issues:

* Verify that all audience mappings are correctly configured
* Ensure client scopes are properly assigned as "Default" types
* Confirm that user UUIDs are copied from Keycloak URLs rather than using usernames
* Check that session timeout values are appropriate for your use case

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
