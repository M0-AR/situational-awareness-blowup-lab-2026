# Situational Awareness 2026: How 4× Leverage Turned +439% into −67% in 30 Days
## A Reproducible Forensic Replication of the $45B → $10B AI Hedge-Fund Blowup — Verified on Live Market Data

> **New repo, from scratch. No local code reused. Every number below re-downloads public Yahoo Finance data and can be reproduced with `docker compose up`.**

[![Reproduce](https://img.shields.io/badge/reproduce-docker%20compose%20up-blue)]()
[![Data](https://img.shields.io/badge/data-Yahoo%20Finance%20live-green)]()
[![Status](https://img.shields.io/badge/EXP--01..04-PASS-green)]()

---

## Abstract

In H1 2026, Situational Awareness LP — an AI-infrastructure hedge fund founded in Sep 2024 by 24-year-old ex-OpenAI researcher Leopold Aschenbrenner — reported **+439% net (1,551% since inception)** and peaked at **~$45B AUM**, then lost **−67% in July 2026 alone**, falling to **~$10B** after a forced $16B public-book sale to Citadel at a discount, amid prime-broker margin calls (Goldman Sachs, JPMorgan, Bank of America) and a subsequent SEC probe. Reported leverage: **~400% (4×)**.

This lab asks three falsifiable questions and answers them with live data:

1. **Did the claimed holdings actually fall the claimed amount in July 2026?** Yes — see EXP-01.
2. **Is 4× leverage mathematically sufficient to explain both +439% and −67%?** Yes — see EXP-02/03.
3. **Is this a new phenomenon or the same recipe (LTCM 1998 → Amaranth 2006 → Archegos 2021 → SA 2026)?** Same recipe, faster, with two novel quantitative signatures we document: a **correlation spike (0.44→0.81)** and a **100% vulture-bounce** — see EXP-04.

All experiments pass on data downloaded October 2026 (Yahoo Finance, auto-adjusted closes).

### Verified headline table (live, auto-adjusted)

| Ticker | Represents | 30-Jun-2026 → 31-Jul-2026 (live) |
|---|---|---|
| NBIS (Nebius) | compute | **−31.1%** |
| CRWV (CoreWeave) | compute | **−27.9%** |
| MU (Micron) | memory | **−28.7%** |
| SNDK (SanDisk) | memory | **−46.6%** |
| 000660.KS (SK Hynix) | memory | **−35.2%** |
| BE (Bloom Energy) | power | **−32.0%** |
| INTC (Intel) | chips | **−35.4%** |
| IREN | BTC-miner→DC | −19.5% |
| ADBE (Adobe, **short leg**) | shorted software | **+22.1%** (short squeeze) |
| SOXX (semiconductor index) | benchmark | −21.2% |
| QQQ | benchmark | −6.6% |

Jan-02 → Jun-30 run-up (same source): SNDK **+726%**, MU **+266%**, NBIS **+207%**, BE **+207%**, CRWV **+25%**, ADBE **−38.5%** — i.e. the long-short was winning both legs before it violently reversed. That asymmetry is the whole story.

**Benchmark outputs:** [`benchmarks/exp01_july_drawdown.json`](benchmarks/exp01_july_drawdown.json),
[`benchmarks/exp02_leverage_math.json`](benchmarks/exp02_leverage_math.json),
[`benchmarks/exp03_doublekill.json`](benchmarks/exp03_doublekill.json),
[`benchmarks/exp04_hidden_patterns.json`](benchmarks/exp04_hidden_patterns.json).

---

## 1. What happened (sourced narrative, every claim cited)

* **Who:** Leopold Aschenbrenner (b. Germany, doctors' family; skipped grades, high school at 15, Columbia at 15, valedictorian 2021 at 19 in econ/math/stats; OpenAI Superalignment; fired for alleged leaking; ex-FTX Future Fund ties). Sources: CNBC 31-Jul-2026; Invezz 31-Jul-2026; Mossfire post-mortem 01-Aug-2026.
* **Thesis → fund:** 165-page June-2024 essay *Situational Awareness* (AGI → chips + data centers + power). Fund launched late-2024/early-2025 at ~$5M→$200M+ seed; backers: Collison brothers (Stripe), Nat Friedman (GitHub), Daniel Gross, Jane Street. Sources: CNBC; Reuters 30-Jul-2026.
* **Book:** Long AI infra (Nebius, CoreWeave, SanDisk, Micron, SK Hynix, Bloom Energy, miners-to-DC) + short software (Adobe et al.). Q1-2026 13F: Nebius, SanDisk, Micron, CoreWeave top. Sources: CNBC Faber Report 30-Jul-2026; WSJ via Reuters.
* **Miracle:** +439% H1-2026 letter (24-Jul-2026), 1,551% since inception; $225M → $45B reported; $45B peak early-July. Sources: FT via Yahoo 03-Aug-2026; Investing.com 03-Aug-2026; BI letter 31-Jul-2026.
* **Reversal:** July-2026 semis −30%; book longs −35–50% in a month; shorts rose. −67% July (confirmed in 31-Jul investor letter: *"we let you down"*). Margin calls Jul 29; marketed book overnight; Millennium/Jane Street passed; Citadel bought ~$16B long+short book Jul 30 at discount (~10% reported). Retained ~$10B (incl. ~$5B private Anthropic, unlevered cash equities). Sources: Reuters; Bloomberg 30-Jul-2026; WSJ 30-Jul-2026; CNBC Griffin letter 21-Aug-2026 (Citadel shed >80% risk via 100+ blocks >$4B; flagship +5.9% July).
* **Aftermath:** SEC subpoenas to prime brokers (trades, borrowing, lender comms); no wrongdoing alleged; fund continues hybrid public-private, re-entered options smaller. Sources: TechCrunch/ValueAddVC 24-Aug-2026. Fed/BoE Jane-Street spillover scrutiny Sep-2026 (ZeroHedge/FT) — context only.
* **Irony preserved:** a fund named *Situational Awareness* was unprepared for the situation where it was wrong on timing — the risk-management moral of this paper.

> Full source list with URLs is in [`papers/PAPER.md`](papers/PAPER.md) § References. No paywalled source is quoted beyond fair-use facts.

## 2. Contributions (what is new here vs. press retellings)

1. **Live-data forensic replication** — four runnable experiments that re-derive the blowup from public prices, not press quotes.
2. **Leverage sufficiency proof** — equal-weight AI-infra basket Jan-Jun mean **+286%** (×4 = **+1,145%** gross → +439% net after fees/concentration/timing is plausible); July mean **−33.2%** (×4 = **−133%** full-hold → realized −67% implies intra-month deleveraging, consistent with the Citadel block).
3. **Double-kill quantification** — longs −31.6% mean + short ADBE +22.1% with w_short∈[0.2,0.4], L=4 gives **−144% to −162%** full-hold; the gap to −67% *is* the fire-sale cushion. This is the cleanest evidence the fund did not hold to month-end.
4. **Two hidden patterns (verified):**
   * **P1 — Crowded-correlation spike:** mean pairwise correlation of 7 infra longs **0.44 (H1) → 0.81 (July)**. Diversification evaporated exactly when leverage needed it.
   * **P2 — Vulture-bounce:** **7/7 (100%)** basket names green 2 weeks after the Jul-30 block (NBIS +47.4%, CRWV +42.4%, SNDK +28.2%). Forced seller marked the bottom — Citadel's alpha was liquidity provision, not stock-picking.
5. **Fragility ranking across 30 years** — LTCM (25×) → Amaranth (~5× concentrated) → Archegos (5–8× TRS, $160B gross record) → SA (4×, largest AUM blowup in 5 years at $45B). Same four threads: extreme leverage, concentration, overconfidence, liquidity-vanish. SA adds a fifth: **disclosure-huntability** (13F/letters/Twitter made the book targetable; Aschenbrenner's own "bank run" language, 31-Jul letter).
6. **Zero-buffer theorem (4× edition):** at 4× with 25% maintenance margin, equity ratio = 1/4 = 25% → **zero adverse-move buffer**. Any down month triggers calls. The fund's leverage *was* the margin call.

## 3. Method (so a referee can redo it in 10 minutes)

```
docker compose up            # runs EXP-01..04, writes benchmarks/*.json
# or without docker:
pip install -r requirements.txt
python3 experiments/01_verify_holdings_drawdown.py
python3 experiments/02_leverage_439_to_minus67.py
python3 experiments/03_longshort_doublekill.py
python3 experiments/04_hidden_patterns_benchmark.py
```

* **Data:** `yfinance` auto-adjusted closes, tickers `NBIS CRWV MU SNDK BE INTC IREN 000660.KS ADBE SOXX NVDA QQQ`, windows `2025-01-01→2026-10-03`, July window `2026-06-30→2026-07-31` (23 trading days), bounce window `Jul-30→Aug-14`. Cache: `data/raw/close_cache.csv` (refresh with `download_close(refresh=True)`).
* **Best-practice compliance:** single-purpose modules (`src/lab/data.py|leverage.py|metrics.py`), deterministic windows, JSON benchmarks as test oracles, `assert` gates in every experiment (fail loudly if live data disagrees), Dockerfile pinning `python:3.12-slim`. Follows reproducible-quant checklist (data provenance, no hand-typed prices, seed-free deterministic math).
* **What we do NOT claim:** exact fund weights (undisclosed; we use equal-weight basket + sensitivity over w_short and L). Private Anthropic (~$5B) is excluded from public-book math — correctly, since it was not sold.

## 4. Results in one page

* **EXP-01 PASS:** all five gates green on live data (NBIS<−20, SNDK<−35, Hynix<−25, ADBE>+15, SOXX<−15).
* **EXP-02 PASS:** 4× explains both tails. Gross +1,145% vs reported +439% net leaves ample room for fees, timing, short drag, and concentration — no miracle needed beyond direction + leverage.
* **EXP-03 PASS:** full-hold double-kill (−144%..−162%) brackets realized −67% from above; deleveraging band L∈[1.5,2.5] hits −67%±25. The Citadel sale *is* the missing variable.
* **EXP-04 PASS:** correlation spike confirmed (0.44→0.81); bounce 100% hit rate; history table reproduces the "same recipe, same buyer" regularity (Citadel bought Amaranth 2006 *and* SA 2026).

## 5. Hidden patterns — discussion (the PhD seed)

* **Why did shorts rise exactly when longs fell?** July-2026 was a momentum-unwind + AI-rotation: Morgan Stanley TMT momentum −53.5% vs SOX −30% (Mossfire). Software shorts were consensus-AI-hedge; rotation squeezed them. A long-short book that is *both* legs of the same momentum factor is not hedged — it is **doubled**.
* **Why did Citadel win?** Not prediction but **balance-sheet**: all-night diligence (Griffin + Salame + Beeson + quants + counsel Jul 29–30), 10%-ish discount, 100+ blocks to distribute. Classic *vulture investing* (legal, non-charitable). Cliff Asness's line — *"angels coming, Grim Reaper knocking"* — applies verbatim.
* **Transparency paradox (P4, hypothesis):** SA published its book into papers/13Fs/letters/tweets; market hunted it. Next crowded AI book will hide leverage (total-return swaps like Archegos, off-balance-sheet neocloud debt). Testable prediction: falling 13F informativeness of AI thematic funds post-2026.
* **Systemic warning:** a <2-year fund obtaining 4–5× from three top primes signals loose prime-brokerage risk appetite for AI. Layers above (retail levered ETFs, miner-to-DC debt, neocloud GPU stockpiling on credit) remain unmeasured — future work §6.

## 6. Limitations & future work

* Weights/prime terms/fee drag undisclosed → sensitivity bands, not point estimates.
* Yahoo splits/dividends auto-adjusted; Korean close timing vs US block differs by hours — direction unaffected.
* No intraday margin-call tape; −67% attribution uses month-end proxies.
* Next: (a) options-implied crowding pre-July, (b) prime-brokerage haircut panel, (c) 13F-huntability index, (d) neocloud credit chain mapping.

## 7. How to cite / share

```bibtex
@software{sablowup2026,
  title  = {Situational Awareness 2026: forensic replication of a 4x-leverage blowup on live data},
  year   = {2026},
  note   = {EXP-01..04, benchmarks/*.json, docker compose up},
}
```

## 8. File map

```
docker-compose.yml  Dockerfile  requirements.txt
src/lab/{data,leverage,metrics}.py
experiments/01_verify_holdings_drawdown.py
experiments/02_leverage_439_to_minus67.py
experiments/03_longshort_doublekill.py
experiments/04_hidden_patterns_benchmark.py
benchmarks/*.json   data/raw/close_cache.csv
papers/PAPER.md     METHODOLOGY.md
```

## 9. Disclaimer

Educational research only. Not investment advice. Public data, fair-use facts, no insider material. Verify independently via `docker compose up`.
