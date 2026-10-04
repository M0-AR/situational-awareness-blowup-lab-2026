"""Live-market data layer. All numbers come from Yahoo Finance (public data).
No hand-typed prices: every experiment re-downloads and caches.
"""
import os
import pandas as pd
import yfinance as yf

CACHE = os.path.join(os.path.dirname(__file__), "../../data/raw/close_cache.csv")

LONGS = ["NBIS", "CRWV", "MU", "SNDK", "BE", "INTC", "IREN", "000660.KS"]
SHORTS = ["ADBE"]
BENCH = ["SOXX", "NVDA", "QQQ"]
ALL = LONGS + SHORTS + BENCH


def download_close(start="2025-01-01", end="2026-10-03", refresh=False) -> pd.DataFrame:
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    if os.path.exists(CACHE) and not refresh:
        try:
            df = pd.read_csv(CACHE, index_col=0, parse_dates=True)
            if len(df) > 100:
                return df
        except Exception:
            pass
    px = yf.download(ALL, start=start, end=end, auto_adjust=True, progress=False)["Close"]
    px.to_csv(CACHE)
    return px


def pct_window(px: pd.DataFrame, a: str, b: str) -> pd.Series:
    sub = px.loc[a:b]
    return (sub.iloc[-1] / sub.iloc[0] - 1) * 100


def july_2026_drawdown(px: pd.DataFrame) -> pd.Series:
    return pct_window(px, "2026-06-30", "2026-07-31")


def runup_stats(px: pd.DataFrame) -> pd.Series:
    return pct_window(px, "2026-01-02", "2026-06-30")
