#!/usr/bin/env python3
"""產生試玩版：把 index.html 的 TRIAL 開關打開，輸出 trial/index.html。
試玩版發布到另一個 artifact，確認沒問題才把改動放進正式版。"""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / 'index.html').read_text(encoding='utf-8')
s2, n = re.subn(r'/\*TRIAL\*/false/\*TRIALEND\*/', '/*TRIAL*/true/*TRIALEND*/', s)
assert n == 1, n
s2 = s2.replace('<title>維京：斧與王冠</title>', '<title>斧與王冠 試玩版</title>', 1)
out = root / 'trial' / 'index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(s2, encoding='utf-8')
print('wrote', out)
