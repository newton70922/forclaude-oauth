# 其他遊戲怎麼做（2026-11-28）

挑了跟我們最像的遊戲：維京題材的，還有「角色驅動、選擇有後果」的熱門作品。
依我們現有的功能分類，每類寫「它們怎麼做」和「我們可以怎麼用」。
資料多半來自攻略網站和評論，數字可能隨版本不同，看設計思路就好。

## 一、勇士的感情怎麼往前走

| 遊戲 | 做法 |
|---|---|
| 聖火降魔錄：風花雪月 | 支援等級分 C → B → A（主角另有 S）。在修道院的休息日，透過散步聊天、送禮、一起練唱來加。有些角色最多只到 B。 |
| Hades（黑帝斯） | 送「花蜜」加好感，送一次就換到一個「信物」，帶進下一輪會越用越強。好感卡關時，愛心上會出現鎖頭，代表要先完成一件事。花蜜很稀少，所以送給誰本身就是決定。 |
| 質量效應 2 | 每個隊員都有一個「忠誠任務」。做完，他在最終戰活下來的機會大很多。 |

**我們可以怎麼用**
- 五格進度（陌生 → 信任 → 立誓 → 心事 → 覺醒）跟風花雪月的 C/B/A/S 是同一個概念，方向是對的。
- Hades 的「鎖頭」值得學：好感夠了但心事還沒解，就在勇士頁上顯示「他有話想說」，讓玩家知道下一步在哪。試玩版已經這樣做了。
- Hades 讓「感情」和「戰力」綁在同一件事上：好感升了，就給一樣帶得走的東西。我們立誓時會教一招，方向一樣；覺醒時也可以給一個看得見的能力。

## 二、角色一多，怎麼照顧得過來

| 遊戲 | 做法 |
|---|---|
| 刺客教條：維京紀元 | 一次只走一個地區的故事，每段有自己的角色。走完的人住進聚落。 |
| 暗黑地牢 | 一次只帶 4 個人出門，其他人留在村子裡。村子的酒館、修道院幫留下的人消除壓力。 |
| 遠征：維京 | 同伴會對你的決定有反應，數值也跟著變。冷落同伴，之後的戰鬥會更難。 |

**我們可以怎麼用**
- 「身邊 3 個人」加上「其他人住在建築裡」，跟暗黑地牢的做法幾乎一樣。這是業界驗證過、行得通的做法。
- 暗黑地牢的建築是用來照顧沒出門的人。我們的建築可以讓住在裡面的勇士好感不掉，或掉得比較慢，跟你選的 A 剛好接得上。

## 三、最後一戰怎麼把前面的事叫回來

| 遊戲 | 做法 |
|---|---|
| 質量效應 2 | 最終任務「自殺任務」：誰活下來，取決於忠誠任務做了沒、船升級了沒，以及你把誰派去做哪件事。派錯人會死人。 |
| 旗幟傳說 | 沒有手動存檔，死了就是死了。官方設計講座說：「沒有正確的選擇，只有先後順序。」 |

**我們可以怎麼用**
- demo 的最後一戰就是照這個思路做的：前面的選擇決定戰場上有誰、強不強。
- 正式版的丹麥戰爭和諸神黃昏，已經有戰前會議和勇士回響，但還沒做到「派誰去哪裡，決定誰活下來」。這是很有份量的下一步。

## 四、資源怎麼產生壓力

| 遊戲 | 做法 |
|---|---|
| 旗幟傳說 | 「聲望」同時是錢和經驗：升級角色就沒錢買補給，補給不夠，族人開始餓死，士氣跟著掉，戰鬥就變難。所有系統咬在一起。 |
| 北境之地 | 冬天是最大的敵人：冬天前要存糧，冬天食物和木柴消耗變多。沒糧，人就不開心；不開心，人口就不會長。 |
| 冰汽時代 | 兩條人心值：希望和不滿。每簽一條法律都會動到其中一條或兩條。 |

**我們可以怎麼用**
- 盤點時說的「錢和糧用不完」，可以學北境之地：讓冬天真的吃糧。
- 旗幟傳說的「一種貨幣有兩種用途，只能選一種」，可以套在名聲上。現在名聲只是用來花，可以改成同時是「勇士願不願意來」的門檻。
- 冰汽時代的「希望／不滿」，跟我建議把名聲、惡名、忠誠合成兩條，是同一個方向。

## 五、領地和建築

| 遊戲 | 做法 |
|---|---|
| 刺客教條：維京紀元 | 蓋建築會帶來新的居民和他的故事；材料主要靠突襲。 |
| 暗黑地牢 | 建築就是照顧人的地方；升級用的材料，要從地牢裡帶回來。 |
| 北境之地 | 每塊地只能蓋有限的建築，冬天前要先安排好人手。 |

**我們可以怎麼用**
- 「建築帶來勇士」：清單在下面，等你確認。
- 建築數量要少，每一棟都要跟人有關。

## 六、國法和治理

| 遊戲 | 做法 |
|---|---|
| 冰汽時代 | 法典分兩條路線，簽了就不能撤。開發者說，他們想做出「溫水煮青蛙」的感覺：一條一條簽下去，回頭才發現走得多遠。 |
| 王國風雲 3 | 有實力的封臣沒被放進議會，對你的好感就大扣分；好感太低，就會結黨反你。 |

**我們可以怎麼用**
- 我們的國法目前是一年一條、各自獨立。可以學冰汽時代，排成兩條路線，例如「舊神與傳統」和「王權與法律」，簽到後面會改變結局。
- 冊封雅爾可以學王國風雲：封了誰，沒被封的勇士會吃醋。這也剛好接上勇士的感情線。

## 七、選擇怎麼呈現

| 遊戲 | 做法 |
|---|---|
| 王權（Reigns） | 四條數值（教會、人民、軍隊、國庫）。拖動卡片時，只告訴你會動到哪幾條，不告訴你多少。任何一條滿了或空了，國王就完了。 |
| 旗幟傳說 | 後果常常出乎意料，沒有標準答案。 |

**我們可以怎麼用**
- 我們現在很多選項都直接寫出「銀幣 +30、忠誠 −5」，選擇變成算數學。可以學王權：只提示「會影響哪方面」，不寫數字。這也符合你訂的「隱藏機制不寫說明文字」。
- 這點要小心，改太多會讓玩家覺得不透明。可以先挑劇情事件試，商店、建設這類照舊寫數字。

## 八、重玩性

| 遊戲 | 做法 |
|---|---|
| Hades | 一輪很短；每輪回來，劇情和感情都會往前一點。死掉也有進度。 |
| 王權 | 國王死了換下一任，同一個王朝慢慢解鎖新卡片。 |

**我們可以怎麼用**
- 我們已經有出身、傳承、通關記號、檢查點，方向對了。
- 少的是「一局短一點」：demo 的 20 分鐘一局，可以考慮做成正式版的一個獨立模式。

## 建築和勇士的對應（建議，等你確認）

| 建築 | 住進來的勇士 | 為什麼 |
|---|---|---|
| 擴建長屋 | 布拉吉 | 詩人在長屋裡唱歌 |
| 鐵匠鋪 | 古德倫 | 她就是鐵匠 |
| 兵營 | 哈康 | 帶新兵的老兵 |
| 練武場 | 阿斯特麗德 | 教盾牆 |
| 瞭望塔 | 埃納 | 獵人的眼睛 |
| 祭壇 | 烏娜 | 草藥和祭祀 |
| 蒸氣浴 | 拉格納 | 讓狂戰士冷靜下來，剛好接上他的心事 |
| 先祖石 | 托爾芬 | 他的心事就是一座墳 |
| 議事廳 | 古托姆 | 打仗前畫陣形的人 |
| 符文師小屋 | 艾瑟斯坦 | 會讀會寫的人 |
| 市集 | 克努特 | 什麼門路都有 |
| 龍頭船塢 | 赫羅爾夫 | 紅帆船 |
| 糧倉、碼頭 | （沒有） | 一般建築 |
| — | 比約恩、西格麗德 | 照現在的劇情加入，不綁建築 |

作法：勇士不在你身邊時，就住在自己的建築裡。有建築的人，好感不會掉，建築效果也會變強。
沒蓋那棟建築的勇士，好感會照你選的 A 慢慢下降。

## 資料來源

- 刺客教條：維京紀元
  - [GamesRadar：渡鴉嶺建築](https://gamesradar.com/assassins-creed-valhalla-settlement-ravensthorpe-guide)
  - [TechRadar：約姆斯維京](https://techradar.com/how-to/how-to-recruit-jomsvikings-in-assassins-creed-valhalla)
  - [Twinfinite：結盟地圖](https://twinfinite.net/guides/assassins-creed-valhalla-alliance-map-explained-where-to-pledge-first/)
- 旗幟傳說
  - [RPG Site：選擇之痛](https://www.rpgsite.net/feature/7365-the-banner-saga-and-the-pain-of-choice)
  - [GDC 敘事設計報告](https://media.gdcvault.com/gdc2020/GameNarrativeReview/Benjamin%20Mora-Davison%20-%20The%20Banner%20Saga-paper.pdf)
  - [Gamepressure：補給](https://www.gamepressure.com/thebannersaga/supplies/za5d10)
- 質量效應 2
  - [Wikipedia：自殺任務](https://en.wikipedia.org/wiki/Suicide_Mission_(Mass_Effect_2))
  - [GameSpot：最佳結局](https://www.gamespot.com/articles/mass-effect-2-suicide-mission-how-to-get-the-best-ending/1100-6491482/)
- 遠征：維京
  - [Gamepressure：隊友與決定](https://www.gamepressure.com/expeditions-viking/party-members-and-your-decisions/z39bb6)
  - [Wccftech 評測](https://wccftech.com/review/expeditions-viking/amp/)
- 北境之地
  - [PC Gamer 評測](https://www.pcgamer.com/northgard-review/)
  - [TheGamer：新手技巧](https://www.thegamer.com/northgard-beginners-tips/)
- Hades
  - [RPG Site：花蜜與信物](https://rpgsite.net/feature/10266-hades-nectar-guide-who-to-give-nectar-to-for-keepsakes)
  - [itch.io：Hades 的循環與劇情](https://itch.io/blog/774695/to-hell-and-back-again-a-look-at-loops-and-arcs-in-hades)
- 聖火降魔錄：風花雪月
  - [RPG Site：支援系統](https://www.rpgsite.net/feature/8759-fire-emblem-three-houses-dialogue-choices-consequences-and-support-guide-walkthrough)
  - [iMore：休息日](https://www.imore.com/how-get-most-out-your-free-days-fire-emblem-three-houses)
- 王國風雲 3
  - [Gamepressure：封臣](https://www.gamepressure.com/crusader-kings-3/vassals/z0f0fd)
  - [ACOUP：王國風雲 3](https://acoup.blog/2022/10/07/collections-teaching-paradox-crusader-kings-iii-part-iii-constructivisting-a-kingdom/)
- 王權
  - [Game Developer：王權的敘事設計](https://gamedeveloper.com/design/game-design-deep-dive-creating-an-adaptive-narrative-in-i-reigns-i-)
  - [Gamereactor 評測](https://embed.gamereactor.eu/reigns-review/)
- 冰汽時代
  - [PC Gamer：開發者談法典](https://www.pcgamer.com/frostpunk-developers-on-hope-misery-and-the-ultimately-terrifying-book-of-laws)
- 暗黑地牢
  - [TV Tropes：暗黑地牢](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/DarkestDungeon)
  - [Game Informer：生存指南](https://www.gameinformer.com/b/features/archive/2016/01/21/darkest-dungeon-survival-guide.aspx)
