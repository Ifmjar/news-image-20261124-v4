# The World in One Day — Tuesday 24 November 2026 (v4)
[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Ifmjar/news-image-20261124-v4/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Ifmjar/news-image-20261124-v4/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image that sums up the world's news of Tuesday 24 November 2026:
12 stories from 7 regions, set out as a single broadsheet-style poster
with big type, one dominant hero story, and a map of where it happened.

## What the poster shows

- **Hero — the Ulleung alert.** Russian jets enter Korea's air defence
  zone on Tuesday morning; Seoul orders Ulleung islanders to shelter at
  07:52 KST and lifts the alert five minutes later. F-15Ks scramble; no
  airspace is violated. The alerts that blamed North Korea were wrong —
  a training template was the cause (Reuters / AP / Yonhap).
- **Chess — Game 1 drawn.** Gukesh vs Sindarov opens in Geneva: Sindarov
  with White, a Berlin, queens off by move 8, ½–½. 14 games, $2.5M
  (FIDE / Chess.com).
- **Markets — the rally cools.** After Monday's record +31% on Huang's
  return as Nvidia chief, the shares slip ~4% before Tuesday's open.
  Nasdaq +6.5% Monday, its best day since April (Reuters).
- **Also today (8 more):** the overnight strike on Zaporizhzhia (2 killed,
  22 injured; Dymer toll up to 11); Trump assailing Newsom over 548
  death-row commutations; a new path for Trump's hush-money appeal;
  Democrats on course for 258 House seats; Japan's flash PMI and
  Germany's Ifo; Indian and Chinese generals meeting in Arunachal;
  Moscow warning Tallinn; and a supermoon meeting the Seven Sisters.
- **Date check panel.** The Monday and weekend stories are named and left
  out: Nvidia reinstating Huang, Oxfam's Gaza report, FIFA naming the
  2031/2035 Women's World Cup hosts, NATO meeting over Poland's missiles
  (all Monday); the Banten fire breaking out Saturday; Alcaraz winning
  the ATP Finals Sunday; the Russian corvette sunk Sunday, confirmed
  Monday.

## How v4 differs from v3

v3 ("The World in One Day — Tuesday 24 November 2026", 11 stories)
finished round 1 at rank 1734 of 7302, judge win rate 585927. v4 keeps
the broadsheet that worked but fixes what v3 got wrong or missed: the
Ulleung framing (v3 had the Russian/North Korean confusion backwards);
the chess result (v3 previewed Game 1, v4 reports the draw); the Banten
toll (24 → 26, Tuesday's confirmed figure); the markets story (v4 adds
Tuesday's premarket give-back to Monday's rally); the map (v3's blobs
are replaced by recognisable continents with eight numbered pins); and
three Tuesday stories v3 missed entirely (Zaporizhzhia, Newsom, the
hush-money appeal).

## How the entry works

`entry.png` is the finished poster (1024x1024). The program in `main.py`
does no drawing: it reads the poster, walks its PNG chunks verifying
every CRC, the IHDR size limits and the IEND terminator, and copies it
byte for byte to `/output/entry.png`. It uses only the Python standard
library, needs no network, and always produces the same output.

## Running it

```sh
python3 main.py
```

It prints the number of bytes written and exits 0 on success.
