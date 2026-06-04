---
title: "Ledger API Errors"
slug: "appdev-troubleshooting-guide-ledger-api-errors"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/ledger-api-errors.md"
source_title: "Ledger API Errors"
tags:
  - appdev
  - troubleshooting-guide
  - ledger-api-errors
---

# Ledger API Errors

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Ledger API Errors

> Common Ledger API error codes encountered during command submission, with causes and resolutions.

These gRPC status codes come from the Ledger API layer.

### AUTH\_INVALID\_TOKEN

```
UNAUTHENTICATED: Could not verify JWT token
```

**Cause:** The bearer token is missing, malformed, expired, or signed with an unrecognized key.

**Fix:**

* Verify the token has not expired (check the `exp` claim)
* Confirm the token audience matches `LEDGER_API_AUTH_AUDIENCE`
* Ensure the token includes the `daml_ledger_api` scope
* Check that the JWKS URL configured on the validator is reachable and returns the correct signing keys

### PACKAGE\_NOT\_FOUND

```
NOT_FOUND: PACKAGE_NOT_FOUND - Could not find package <package-id>
```

**Cause:** The validator does not have the DAR that contains the referenced package, or the package has not been vetted.

**Fix:** Upload the DAR:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm build
curl -X POST http://localhost:5002/v2/packages -F "dar=@.build/your-package.dar"
```

After uploading, confirm the package appears in the package list before retrying the command.

### PARTY\_NOT\_KNOWN

```
NOT_FOUND: PARTY_NOT_KNOWN - Party not known on participant
```

**Cause:** The party identifier in the command does not match any party allocated on this validator.

**Fix:** Allocate the party first, or verify you are using the correct party identifier. Party IDs are case-sensitive and include a fingerprint suffix (e.g., `Alice::1220abcd...`). List known parties:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl http://localhost:5002/v2/parties | jq '.party_details[].party'
```

### PERMISSION\_DENIED

```
PERMISSION_DENIED: An error occurred. Please contact the operator.
```

**Cause:** The authenticated user does not have rights to act as the requested party.

**Fix:** Grant the user read/write access to the party through the Admin API:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST http://localhost:5002/v2/users/<user-id>/rights \
  -H "Content-Type: application/json" \
  -d '{"rights": [{"can_act_as": {"party": "<party-id>"}}]}'
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
