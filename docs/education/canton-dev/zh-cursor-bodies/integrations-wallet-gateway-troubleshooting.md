> Common 钱包 Gateway issues and fixes

本节介绍 common issues and their solutions when working with the 钱包 Gateway.

## 常见问题

## Database Connection 错误

**问题：** The Gateway fails to start with database connection 错误.

**解决方案：**

1. **PostgreSQL:**
   * 验证 the database exists: `psql -U postgres -l`
   * 检查 connection credentials in your config file
   * 确保 PostgreSQL is running: `pg_isready`
   * 验证 网络 connectivity and firewall rules

2. **SQLite:**
   * 确保 the directory exists for the database file
   * 检查 file permissions (read/write access required)
   * 验证 disk space is available

3. **Memory Store:**
   * No 配置 needed, but remember: data is lost on restart

## 认证 Failures

**问题：** API calls return 401 Unauthorized 错误.

**解决方案：**

1. **Invalid or Expired Token:**
   * 确保 you're using a valid JWT token
   * 检查 token expiration time
   * Regenerate the token if necessary

2. **Missing 授权 Header:**
   * Include the 授权 header: `授权: Bearer <token>`
   * 验证 the header format is correct

3. **会话 Not Found:**
   * 创建 a 会话 using `addSession()` 方法 first
   * 确保 the 会话 hasn't expired
   * 检查 that you're using the correct 用户 context

## 网络 Connection Issues

**问题：** Cannot connect to configured networks or ledger API.

**解决方案：**

1. **网络 Unreachable:**
   * 验证 the ledger API URL is correct in your 网络 配置
   * Test connectivity: `curl <ledger-api-url>/v2/version`
   * 检查 firewall rules and 网络 routing

2. **Invalid 网络 配置：**
   * 验证 the `synchronizerId` matches the validator 配置
   * 确保 the identity 提供方 ID matches between 网络 and IDP configs
   * 检查 that 认证 credentials are correct

3. **SSL/TLS Issues:**
   * For HTTPS 端点, verify certificates are valid
   * In 开发, you may need to use HTTP or configure certificate trust

## Port Already in Use

**问题：** 错误: `EADDRINUSE: address already in use :::3030`

**解决方案：**

1. Find and stop the process using the port:

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   # macOS/Linux
   lsof -ti:3030 | xargs kill -9

   # Or find the process
   lsof -i :3030
   ```

2. Use a different port:

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   wallet-gateway -c ./config.json -p 8080
   ```

3. 检查 if another Gateway instance is running:

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   ps aux | grep wallet-gateway
   ```

## 配置 Validation 错误

**问题：** Gateway fails to start with 配置 错误.

**解决方案：**

1. **Validate your config against the schema:**

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   wallet-gateway --config-schema > schema.json
   # Use a JSON schema validator tool
   ```

2. **检查 for common mistakes:**
   * Missing required fields
   * Invalid JSON syntax
   * 类型 mismatches (strings vs numbers)
   * Missing or incorrect IDP references in 网络 configs

3. **Use the example config as a template:**

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   wallet-gateway --config-example > my-config.json
   # Edit my-config.json
   ```

## Signing 提供方 Issues

**问题：** 交易 fail with signing 错误.

**解决方案：**

1. **Fireblocks:**
   * 验证 environment variables are set correctly: `FIREBLOCKS_SECRET` and `FIREBLOCKS_API_KEY`
   * 确保 API keys are valid and have proper permissions
   * 验证 Fireblocks API is accessible from your 网络

2. **参与者:**
   * 确保 the 参与者 node is running and accessible
   * 验证 the party exists on the 参与者
   * 检查 参与者 logs for signing 错误

3. **Blockdaemon:**
   * 验证 environment variables are set: `BLOCKDAEMON_API_URL` and `BLOCKDAEMON_API_KEY`
   * Test API connectivity
   * 确保 API key has signing permissions

4. **Dfns:**
   * 验证 environment variables are set: `DFNS_ORG_ID`, `DFNS_BASE_URL`, `DFNS_CRED_ID`, `DFNS_PRIVATE_KEY`, and `DFNS_AUTH_TOKEN`
   * 确保 the 服务 账户 credentials are correct
   * Confirm the 服务 账户 has 钱包 creation and signing permissions

## 调试

## Enable Debug Logging

设置 log level to debug for more detailed information:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
wallet-gateway -c ./config.json -f pretty
# Logs will show debug-level information
```

For structured logging (useful for log aggregation):

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
wallet-gateway -c ./config.json -f json
```

## 检查 Logs

Review the Gateway logs for 错误 messages and stack traces. Common log locations:

* Console output (when running directly)
* System logs (when running as a 服务)
* Container logs (when running in Docker/Kubernetes)

## 验证 API 端点

Test that the Gateway is responding:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Health check (web UI)
curl http://localhost:3030

# dApp API status (requires authentication)
curl -X POST http://localhost:3030/api/v0/dapp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"jsonrpc":"2.0","id":1,"method":"status","params":[]}'
```

## 获取帮助

若你 continue to experience issues:

1. 检查 the logs for detailed 错误 messages
2. 验证 your 配置 against the schema
3. Review the API specifications for correct usage
4. 检查 GitHub issues for similar problems
5. Review the 配置 documentation for your specific setup

## 日志级别

The Gateway uses structured logging with the following levels:

* **错误**: Critical 错误 that prevent operation
* **WARN**: 警告 conditions that may cause issues
* **INFO**: Informational messages about normal operation
* **DEBUG**: Detailed diagnostic information

Adjust log verbosity based on your needs. In 生产, INFO level is typically sufficient, while DEBUG is useful for troubleshooting.

