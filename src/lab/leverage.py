"""Leverage mechanics: the exact math that turned +439% into -67%."""
import pandas as pd


def levered_return(asset_return_pct: float, leverage: float) -> float:
    """Linear approximation used by prime-broker margin accounts.
    L=4.0 means 400% gross exposure: +10% asset -> +40% equity (before costs).
    """
    return asset_return_pct * leverage


def margin_call_threshold(leverage: float, maintenance_margin: float = 0.25) -> float:
    """Adverse asset move (negative %) that wipes equity to maintenance margin.
    Equity ratio E = 1/L - adverse_move. Solve E = maintenance_margin.
    """
    return -((1.0 / leverage) - maintenance_margin) * 100


def double_kill_attribution(long_ret: float, short_ret: float,
                            w_long: float = 1.0, w_short: float = 0.3,
                            leverage: float = 4.0) -> dict:
    """Long-short book where shorts rise against you.
    Net asset return = w_long*long_ret - w_short*short_ret (short leg).
    Equity return = net * leverage.
    Defaults mirror reporting: ~2/3 public book long AI infra, ~30% short software.
    """
    net = w_long * long_ret - w_short * short_ret
    equity = net * leverage
    return {"net_asset_pct": round(net, 2),
            "equity_pct": round(equity, 2),
            "long_contrib": round(w_long * long_ret * leverage, 2),
            "short_contrib": round(-w_short * short_ret * leverage, 2)}
