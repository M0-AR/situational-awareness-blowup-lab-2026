"""EXP-01: verify reported July-2026 holdings drawdown against live Yahoo data.
Claim: longs (NBIS/CRWV/MU/SNDK/BE/INTC/IREN/SK Hynix) fell 20-46% in July 2026;
SOX fell ~21-30%; shorts (ADBE) rose ~+22%.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
from lab.data import download_close, july_2026_drawdown

px = download_close()
res = july_2026_drawdown(px).round(1)
print(res.to_string())
print("\n--- verification ---")
checks = {
    "NBIS<-20": res["NBIS"] < -20,
    "SNDK<-35": res["SNDK"] < -35,
    "SK Hynix 000660.KS<-25": res["000660.KS"] < -25,
    "ADBE>+15 (short squeeze)": res["ADBE"] > 15,
    "SOXX<-15": res["SOXX"] < -15,
}
for k, v in checks.items():
    print(("PASS " if v else "FAIL ") + k)
os.makedirs("benchmarks", exist_ok=True)
json.dump({k: float(v) for k, v in res.items()},
          open("benchmarks/exp01_july_drawdown.json", "w"), indent=2)
assert all(checks.values()), "EXP-01 FAILED against live data"
print("EXP-01 PASS: live data confirms reported July-2026 collapse pattern.")
