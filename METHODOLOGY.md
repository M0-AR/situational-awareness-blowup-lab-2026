# METHODOLOGY — zero-to-hero verification protocol (used here, reusable)

1. **Claim ledger:** extract every falsifiable number from press (439%, $45B→$10B, −67%, 4×, $16B block, holdings list).
2. **One-search-at-a-time:** single websearch call, backoff on 429, fallback to DuckDuckGo-lite fetch; then rotate tools with *different keywords* (searxng / duckduckgo / openresearch web+news / paper-search arxiv+semantic+crossref+openalex / wiki / agent-reach_search web / kaggle / gitmcp docs / gsd_websearch). Voting across sources.
3. **Live-data first:** no hand-typed prices. `yfinance` download → cache CSV → all math from cache. Assertions fail loudly if data disagrees.
4. **Bracket unknowns:** undisclosed weights → grids (w_short, L), not point estimates.
5. **Benchmarks as oracles:** `benchmarks/*.json` written by experiments; README quotes only those files.
6. **Reproduce in one command:** `docker compose up` (python:3.12-slim, requirements.txt).
7. **Publishable paper:** README = short paper; papers/PAPER.md = full draft; both cite every source with date+URL.
