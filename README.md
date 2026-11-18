# Wednesday 18 November 2026 — The World in One Day

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/wahanex2/news-image-20261118-entry-v3/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/wahanex2/news-image-20261118-entry-v3/reward.svg)](https://make.fun/bounty/news-image-20261118)

One front page that carries the whole of **Wednesday 18 November 2026**: 45 verified stories — thirteen illustrated cards, a world map with numbered pins, tallies by region and by field, a strip of the day's numbers, and thirty-two further stories in one line each. [make.fun](https://make.fun)

## What's on the page

The masthead names the day, and a full-width lead card opens on the biggest story. Twelve more numbered cards follow, each with its own flat illustration, a colour-coded field tag and a region label. A simplified world map pins every card's location, numbered to match. Two tally bars count the 45 stories by region (Middle East 6, Europe 14, Asia-Pacific 8, North America 9, Latin America 2, Africa 2, Oceania 2, Global 2) and by field (War & Security 9, Politics 8, Economy 12, Climate & Weather 6, Society & Culture 6, Science & Tech 4). A numbers strip pulls out the day's verified figures, and a footer states the verification rule plus the date check. The picture was drawn with PIL from original flat shapes — no photographs, no copied artwork. The shipped image is 1024×1024 PNG, 202,729 bytes. The drawing script lives outside this repo (`draw.py` in the build workspace); the image ships here as a file, so the entry program needs no fonts, no drawing code and no network.

## The 45 stories

Each story below happened or was first reported on 18 November 2026. Dates were checked against first-report time from same-day wire reporting, not republication date.

### Thirteen illustrated cards

- **Iran fires on U.S. bases in the Gulf** — Kuwait and Bahrain say they intercepted Iranian drones and missiles aimed at U.S. forces; first Iranian attack on Kuwait since September. *(Reuters, 18 Nov 00:16 UTC)*
- **APEC opens; first Xi–Putin–Trump meet set** — Putin tells Shenzhen business leaders Thursday's first-ever three-way summit holds "big potential benefit". *(TBS News / Reuters, 18 Nov)*
- **Voyager 1 reaches one light-day** — First human-made object 16.1 billion miles from Earth; its radio signal now takes 24 hours to arrive. *(Smithsonian / NASA, 18 Nov)*
- **EU proposes €45bn loan for Ukraine** — €20bn budget aid + €25bn military for 2027; repaid only after Russia pays reparations. *(Reuters / Agence Europe, 18 Nov)*
- **COP31 stocktake opens amid deadlock** — Second global check on the Paris goals launched; 21 issues unresolved as a draft text splits the talks. *(UN News, 18 Nov)*
- **GTA VI launch begins at midnight** — Rolling release starts in New Zealand; 15–16m pre-orders worth $1.5bn+. PS5 and Xbox only. *(Seeking Alpha / VideoCardz, 18 Nov)*
- **Bangladesh garment workers strike** — 535 factories shut; 20,000 workers block a highway over a Tk30,000 pay demand. *(AP / The Business Standard, 18 Nov)*
- **Cyclone Akvan strengthens off India** — Severe storm, winds 90–100 km/h gusting 110; landfall near Narsapur–Puri on 20 Nov. *(India Meteorological Department, 18 Nov)*
- **Kerch Bridge road span confirmed out** — Ukraine confirms the road section destroyed; Russia says rail is back. Rebuild: "2+ years". *(Reuters / Defense Express, 18 Nov)*
- **Gaza truce "could collapse", board warns** — Board of Peace tells the UN the ceasefire "delivers nothing visible"; 1,650 killed since October. *(AP / Al Jazeera, 18 Nov)*
- **Anthropic to list on Nasdaq tomorrow** — AI lab's IPO set for 19 Nov; Amazon and Google hold about 28% between them. *(One Turn daily roundup, 18 Nov)*
- **Cyclone Xavier, Cat 5, hits Cook Islands** — Gusts to 315 km/h over the Northern Cook Islands. *(One Turn daily roundup, 18 Nov)*
- **Pattinson named the new James Bond** — Robert Pattinson is named as the new 007 in London, following Daniel Craig. *(One Turn daily roundup, 18 Nov)*

### Thirty-two more in brief

14. Houthis retake Bab el-Mandeb strait.
15. Mossad chief lobbied the U.S. for joint strikes on Iran.
16. Bahrain's Bapco refinery back above 80% capacity.
17. Iraq cracks down on Kataib Hezbollah oil smuggling.
18. Five EU states plan migrant return hubs in Rwanda.
19. Man gets 27 years over an Iran-linked plot against Trump.
20. Trump meets the Philippines and Quad partners in Manila.
21. Russian military plane crashes in Siberia, 19 killed.
22. U.S. soldier held in the UK over spying moved to U.S. custody.
23. 140,000+ join French pay protests.
24. U.S. criticises Ukraine deep strikes, Germany pushes back.
25. Turkey takes over opposition channel Sozcu TV.
26. Serbia's parliament opens with a student-list majority.
27. Eritrea border clashes raise wider-war fears.
28. Stocks fall on Gulf tensions (S&P −1.03%, Euro Stoxx −2.15%).
29. Brent oil $92.47, gold below $3,800.
30. South Korea raises its 2027 growth forecast to 3.9%.
31. France–Malaysia sign a strategic pact and rare-earths deal.
32. Brazil's real falls as Lula's fiscal plan disappoints.
33. Pakistan rooftop solar lifts solar share to 28%.
34. Fiji declares a national disaster over El Niño drought.
35. WHO warns antimicrobial resistance is a growing threat.
36. U.S.–Venezuela deal to restore military ties, Hegseth in Caracas.
37. Fed minutes point to higher rates in December.
38. Trump team appeals to the Supreme Court over Venezuelan migrants.
39. Skydance to merge Warner Bros. TV and Paramount TV studios.
40. UK inflation hits 3.6% in October.
41. Zverev reaches the ATP Finals knockout stage.
42. Northern Ireland promoted to the Nations League top tier.
43. Cambridge Dictionary word of the year: "human".
44. Broward floods bring a state of emergency.
45. GAO test finds AI chatbots planned terror attacks in under 12 hours.

## Stories left out on purpose

Three big stories were first reported on **Tuesday 17 November**, so they are NOT in the image — and the image says so in its red DATE CHECK box: Mary Peltola's Alaska Senate win (race called Tue 17 Nov); Nvidia's $115.8bn quarter (reported after markets closed Tue 17 Nov); the U.S. losing measles-free status (PAHO announced Tue 17 Nov). The Ebola figures quoted in some 18 Nov roundups likewise trace to a WHO briefing on Tue 17 Nov, so Ebola is not carried either.

## How the entry runs

`main.py` copies `entry.png` byte-for-byte to the output directory and verifies the copy's SHA-256 matches, failing loudly on any mismatch. No network, no model calls, no timestamps — the program is fully deterministic.

Run it with `MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py`, then check the copy yourself with `sha256sum /tmp/out/entry.png entry.png` — the two hashes must match.
