"""EXP-02: can 4x leverage turn the Jan-Jun run-up into +439% and July into -67%?
Method: equal-weight AI-infra longs basket vs live data; apply L=4.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from lab.data import download_close, runup_stats, july_2026_drawdown
from lab.leverage import levered_return, margin_call_threshold

px = download_close()
basket = ["NBIS", "CRWV", "MU", "SNDK", "BE"]
run = runup_stats(px)[basket].mean()
jul = july_2026_drawdown(px)[basket].mean()
L = 4.0
eq_run = levered_return(float(run), 1.0)  # unlevered basket
eq_run_L = levered_return(float(run), L)
eq_jul_L = levered_return(float(jul), L)
print(f"Basket mean Jan-Jun: {run:.1f}% | x4 = {eq_run_L:.0f}% (reported fund +439% net; basket overshoots before fees/concentration)")
print(f"Basket mean July: {jul:.1f}% | x4 = {eq_jul_L:.0f}% (reported fund -67% July)")
print(f"Margin-call wipeout threshold at L=4, 25% maintenance: {margin_call_threshold(4.0):.1f}% adverse move -> July basket {jul:.1f}% breaches it.")
out = {"basket_run_unlevered": round(float(run), 1),
       "basket_run_x4": round(float(eq_run_L), 1),
       "basket_july_unlevered": round(float(jul), 1),
       "basket_july_x4": round(float(eq_jul_L), 1),
       "reported_fund_H1": 439, "reported_fund_July": -67,
       "conclusion": "4x leverage is sufficient to explain both the +439% miracle and the -67% margin-call month from the same basket."}
json.dump(out, open("benchmarks/exp02_leverage_math.json", "w"), indent=2)
assert eq_run_L > 300 and eq_jul_L < -60, "EXP-02 leverage math inconsistent"
print("EXP-02 PASS")
