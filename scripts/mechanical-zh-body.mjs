#!/usr/bin/env node
/**
 * Mechanical zh body from en markdown (phrase glossary + header hints).
 * Usage: node scripts/mechanical-zh-body.mjs <slug>
 */
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { extractPageBody } from './lib/canton-doc-utils.mjs';

const ROOT = process.cwd();
const slug = process.argv[2];
if (!slug) {
  console.error('Usage: node scripts/mechanical-zh-body.mjs <slug>');
  process.exit(1);
}

const glossary = JSON.parse(
  await readFile(path.join(ROOT, 'scripts/zh-glossary-integrations.json'), 'utf8'),
);

const enPath = path.join(ROOT, 'docs/education/canton-dev/en', `${slug}.md`);
let body = extractPageBody(await readFile(enPath, 'utf8'));

// Remove doc index blockquote block
body = body.replace(
  /> ## Documentation Index[\s\S]*?(?=\n# |\n[^>])/,
  '',
);

// Strip duplicate H1
body = body.replace(/^# [^\n]+\n+> [^\n]+\n+/m, (m) => {
  const sub = m.match(/^# ([^\n]+)\n+> ([^\n]+)/);
  return sub ? `> ${sub[2]}\n\n` : m;
});

const FENCE = /```[\s\S]*?```/g;
const tokens = [];
let prose = body.replace(FENCE, (m) => {
  const t = `⟦C${tokens.length}⟧`;
  tokens.push(m);
  return t;
});

// Apply glossary (longer keys first)
const keys = Object.keys(glossary).filter(Boolean).sort((a, b) => b.length - a.length);
for (const key of keys) {
  const val = glossary[key];
  if (val === '') continue;
  prose = prose.split(key).join(val);
}

// Common sentence patterns
const patterns = [
  [/^> (.+)$/gm, '> $1'],
  [/\bThe following\b/g, '以下'],
  [/\bThis guide\b/g, '本指南'],
  [/\bThis section\b/g, '本节'],
  [/\bThis page\b/g, '本页'],
  [/\bYou can\b/g, '你可以'],
  [/\bYou will\b/g, '你将'],
  [/\bYou are\b/g, '你需要'],
  [/\bYou should\b/g, '你应'],
  [/\bWe recommend\b/g, '我们建议'],
  [/\bSee \[/g, '参见 ['],
  [/\bSee the\b/g, '参见'],
  [/\bFor more\b/g, '更多信息见'],
  [/\bNote that\b/g, '请注意'],
  [/\bNote also\b/g, '另请注意'],
  [/\bFor example\b/g, '例如'],
  [/\bFor details\b/g, '详见'],
  [/\bWhen creating\b/g, '创建时'],
  [/\bWhen migrating\b/g, '迁移时'],
  [/\bWhen a transaction\b/g, '当交易'],
  [/\bIf you\b/g, '若你'],
  [/\bIf the\b/g, '若'],
  [/\bIf yes\b/gi, '若是'],
  [/\bIf no\b/gi, '若否'],
  [/\bProblem:\*\*/g, '**问题：**'],
  [/\bSolutions:\*\*/g, '**解决方案：**'],
  [/\bLearn more:\*\*/g, '**了解更多：**'],
  [/\bPurpose\b/g, '用途'],
  [/\bDescription\b/g, '说明'],
  [/\bFunction\b/g, '职能'],
  [/\bRole\b/g, '角色'],
  [/\bType\b/g, '类型'],
  [/\bCategory\b/g, '类别'],
  [/\bExamples\b/g, '示例'],
  [/\bExample\b/g, '示例'],
  [/\bImportant\b/g, '重要'],
  [/\bWarning\b/g, '警告'],
  [/\bOptional\b/g, '可选'],
  [/\bRequired\b/g, '必需'],
  [/\bRecommended\b/g, '推荐'],
  [/\bDevelopment\/Testing\b/g, '开发/测试'],
  [/\bProduction\b/g, '生产'],
  [/\bEnterprise\b/g, '企业'],
  [/\bManaged\b/g, '托管'],
  [/\bSecurity Considerations\b/g, '安全注意事项'],
  [/\bHow it Works\b/g, '工作原理'],
  [/\bPrerequisites\b/g, '前置条件'],
  [/\bVerify\b/g, '验证'],
  [/\bCheck\b/g, '检查'],
  [/\bEnsure\b/g, '确保'],
  [/\bConfigure\b/g, '配置'],
  [/\bConnect\b/g, '连接'],
  [/\bDisconnect\b/g, '断开'],
  [/\bInstall\b/g, '安装'],
  [/\bDownload\b/g, '下载'],
  [/\bStart\b/g, '启动'],
  [/\bStop\b/g, '停止'],
  [/\bRun\b/g, '运行'],
  [/\bCreate\b/g, '创建'],
  [/\bRemove\b/g, '移除'],
  [/\bList\b/g, '列出'],
  [/\bGet\b/g, '获取'],
  [/\bSet\b/g, '设置'],
  [/\bAdd\b/g, '添加'],
  [/\bUpdate\b/g, '更新'],
  [/\bDelete\b/g, '删除'],
  [/\bSubmit\b/g, '提交'],
  [/\bExecute\b/g, '执行'],
  [/\bSign\b/g, '签名'],
  [/\bPrepare\b/g, '准备'],
  [/\bQuery\b/g, '查询'],
  [/\bRead\b/g, '读取'],
  [/\bWrite\b/g, '写入'],
  [/\bTransfer\b/g, '转账'],
  [/\bDeposit\b/g, '充值'],
  [/\bWithdrawal\b/g, '提现'],
  [/\bWithdrawals\b/g, '提现'],
  [/\bDeposits\b/g, '充值'],
  [/\bParty\b/g, 'Party'],
  [/\bparties\b/gi, 'Party'],
  [/\btransaction\b/gi, '交易'],
  [/\btransactions\b/gi, '交易'],
  [/\bwallet\b/gi, '钱包'],
  [/\bnetwork\b/gi, '网络'],
  [/\bapplication\b/gi, '应用'],
  [/\bapplications\b/gi, '应用'],
  [/\bdeveloper\b/gi, '开发者'],
  [/\bdevelopers\b/gi, '开发者'],
  [/\buser\b/gi, '用户'],
  [/\busers\b/gi, '用户'],
  [/\bsession\b/gi, '会话'],
  [/\bsessions\b/gi, '会话'],
  [/\bauthentication\b/gi, '认证'],
  [/\bauthorization\b/gi, '授权'],
  [/\bconfiguration\b/gi, '配置'],
  [/\bintegration\b/gi, '集成'],
  [/\bintegrations\b/gi, '集成'],
  [/\bworkflow\b/gi, '工作流'],
  [/\bworkflows\b/gi, '工作流'],
  [/\bcomponent\b/gi, '组件'],
  [/\bcomponents\b/gi, '组件'],
  [/\bservice\b/gi, '服务'],
  [/\bservices\b/gi, '服务'],
  [/\bendpoint\b/gi, '端点'],
  [/\bendpoints\b/gi, '端点'],
  [/\bprovider\b/gi, '提供方'],
  [/\bproviders\b/gi, '提供方'],
  [/\bmethod\b/gi, '方法'],
  [/\bmethods\b/gi, '方法'],
  [/\berror\b/gi, '错误'],
  [/\berrors\b/gi, '错误'],
  [/\brequest\b/gi, '请求'],
  [/\bresponse\b/gi, '响应'],
  [/\bevent\b/gi, '事件'],
  [/\bevents\b/gi, '事件'],
  [/\baccount\b/gi, '账户'],
  [/\baccounts\b/gi, '账户'],
  [/\bbalance\b/gi, '余额'],
  [/\bholdings\b/gi, '持仓'],
  [/\bcontract\b/gi, '合约'],
  [/\bcontracts\b/gi, '合约'],
  [/\bcommand\b/gi, '命令'],
  [/\bcommands\b/gi, '命令'],
  [/\boffset\b/gi, '偏移'],
  [/\boffsets\b/gi, '偏移'],
  [/\brecord time\b/gi, '记录时间'],
  [/\bupdate-id\b/gi, 'update-id'],
  [/\bsynchronizer\b/gi, '同步器'],
  [/\bparticipant\b/gi, '参与者'],
  [/\bvalidator node\b/gi, '验证者节点'],
  [/\bvalidator nodes\b/gi, '验证者节点'],
  [/\btraffic\b/gi, '流量'],
  [/\brewards\b/gi, '奖励'],
  [/\bmonitoring\b/gi, '监控'],
  [/\bbackup\b/gi, '备份'],
  [/\brestore\b/gi, '恢复'],
  [/\btesting\b/gi, '测试'],
  [/\bproduction\b/gi, '生产'],
  [/\bdevelopment\b/gi, '开发'],
];

for (const [re, rep] of patterns) {
  prose = prose.replace(re, rep);
}
body = prose;
tokens.forEach((val, i) => {
  body = body.replaceAll(`⟦C${i}⟧`, val);
});

const outDir = path.join(ROOT, 'docs/education/canton-dev/zh-cursor-bodies');
await mkdir(outDir, { recursive: true });
const outPath = path.join(outDir, `${slug}.md`);
await writeFile(outPath, `${body.trim()}\n`, 'utf8');
console.log(`wrote ${outPath} (${body.length} chars)`);
