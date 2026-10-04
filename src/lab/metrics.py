"""Standard risk metrics."""
import numpy as np
import pandas as pd


def max_drawdown(equity: pd.Series) -> float:
    peak = equity.cummax()
    dd = (equity / peak - 1) * 100
    return float(dd.min())


def sharpe(daily_rets: pd.Series, rf: float = 0.0) -> float:
    ex = daily_rets - rf
    if ex.std() == 0:
        return 0.0
    return float(ex.mean() / ex.std() * (252 ** 0.5))


def concentration_hhi(weights: pd.Series) -> float:
    w = weights / weights.sum()
    return float((w ** 2).sum())
