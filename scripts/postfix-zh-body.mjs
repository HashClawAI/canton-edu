#!/usr/bin/env node
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const slug = process.argv[2];
const file = path.join(process.cwd(), 'docs/education/canton-dev/zh-cursor-bodies', `${slug}.md`);
let t = await readFile(file, 'utf8');
const fixes = [
  ['Canton 网络', 'Canton Network'],
  ['代币标准', 'Token Standard'],
  ['集成 Guide', '集成指南'],
  ['Exchange 集成 Guide', '交易所集成指南'],
  ['钱包-kernel', 'wallet-kernel'],
  ['钱包-集成-guide', 'wallet-integration-guide'],
  ['exchange-集成', 'exchange-integration'],
  ['splice-钱包', 'splice-wallet'],
  ['交易 History Ingestion', '交易历史摄取'],
  ['fault tolerance', '容错'],
  ['validator-node-operations', 'validator-node-operations'],
  ['集成 架构', '集成架构'],
  ['集成 工作流', '集成工作流'],
  [' aims ', ' 旨在 '],
  [' shows ', ' 展示 '],
  [' build on ', ' 基于 '],
  [' thus ', ' 因此 '],
  [' other than ', ' 除…之外 '],
  [' In other words', '换言之'],
  ['This registers', '这会注册'],
  ['while keeping', '同时保留'],
  ['Option 1', '选项 1'],
  ['Option 2', '选项 2'],
  ['Option 3', '选项 3'],
  ['Option 4', '选项 4'],
  ['(recommended)', '（推荐）'],
  ['Release notes are reproduced verbatim from the', '发布说明逐字摘自'],
  ['Below are the release notes for the Wallet SDK versions', '以下为 Wallet SDK 各版本的发布说明'],
];
for (const [a, b] of fixes) t = t.split(a).join(b);
await writeFile(file, `${t}\n`);
console.log('postfix', slug);
