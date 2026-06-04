# Canton 文档站内链接审计摘要

生成方式：`npm run docs:audit-links`（输出 JSON：`link-audit-report.json`）

**最近全量修复（2026-06-04）：** `npm run docs:rewrite-links` + 扩展 `scripts/lib/canton-link-rewrite.mjs`（`rewriteAllLinks`：legacy 路径、相对路径、中文路径、`sdks-tools`、无斜杠 `href="appdev/..."` 卡片链接）。审计 **6 类问题均为 0**；未镜像页面统一回退 `https://docs.canton.network/...`。

## 总体结论

| 类别 | 风险 | 状态 |
|------|------|------|
| 已改写 `/docs/canton/{slug}` | 低 | ✅ 与镜像 slug 一致 |
| 官方路径未收录（legacy 无页） | — | ✅ 改写为官方外链 |
| 中文机翻错误路径 | — | ✅ `ZH_PATH_REPLACEMENTS` 规范化 |
| `sdks-tools` / `shared` | — | ✅ slug 或官方外链 |
| API 参考页相对链接 `../../../` | — | ✅ 按 `source_url` 解析 |
| 可修复别名 | — | ✅ `PATH_ALIASES` + `legacyPathMap` |

历史 PR：[#25](https://github.com/HashClawAI/canton-edu/pull/25) 首批 legacy 重定向；本次为正文 **批量改写**（约 280+ 页/语种 × 2 套目录）。

---

## 维护命令

```bash
npm run docs:rewrite-links   # 批量改写 pages + kb
npm run docs:audit-links     # 审计（应为全 0）
npm run build                # 含 Astro legacy redirects
```

## 未纳入镜像的引用

正文中的 Splice API、Scala ref、部分 GS 页等 **无 slug** 时，链接目标为 `https://docs.canton.network/...`（例如 `api-reference` 卡片中的 dApp API、Wallet Gateway）。若日后 `docs:sync-canton` 扩充镜像，重新跑 `docs:rewrite-links` 即可把可映射路径改回站内 slug。
