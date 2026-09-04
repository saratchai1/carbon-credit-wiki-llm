#!/usr/bin/env python3
"""
High-level arithmetic for T-VER-P-METH-13-02 after subcomponents
have already been calculated under the applicable methodology/tools.

This tool NEVER certifies carbon credits.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

REQUIRED_COMPONENTS = ("tree", "sapling", "deadwood", "soc")
REQUIRED_EMISSIONS = ("burning", "fuel")

def num(v, name):
    if v is None:
        raise ValueError(f"Missing required value: {name}")
    if not isinstance(v, (int, float)):
        raise ValueError(f"{name} must be numeric")
    return float(v)

def calculate(data: dict) -> dict:
    meth = data.get("methodology", {})
    if meth.get("code") != "T-VER-P-METH-13-02":
        raise ValueError("This core calculator is locked to T-VER-P-METH-13-02")

    pc = data.get("project_carbon_change_tco2e", {})
    pe = data.get("project_emissions_tco2e", {})

    project_change = sum(num(pc.get(k), f"project_carbon_change_tco2e.{k}") for k in REQUIRED_COMPONENTS)
    project_emissions = sum(num(pe.get(k), f"project_emissions_tco2e.{k}") for k in REQUIRED_EMISSIONS)
    baseline = num(data.get("baseline_net_removal_tco2e"), "baseline_net_removal_tco2e")
    leakage = num(data.get("leakage_tco2e"), "leakage_tco2e")

    actual = project_change - project_emissions
    net_before_buffer = actual - baseline - leakage

    result = {
        "calculation_id": data.get("calculation_id"),
        "methodology": meth,
        "project_carbon_change_tco2e": project_change,
        "project_emissions_tco2e": project_emissions,
        "actual_net_project_removal_tco2e": actual,
        "baseline_net_removal_tco2e": baseline,
        "leakage_tco2e": leakage,
        "net_anthropogenic_removal_before_buffer_tco2e": net_before_buffer,
        "estimated_after_buffer_tco2e": None,
        "warning": "Estimate only. Not VVB verification or TGO-certified carbon credit."
    }

    rate = data.get("buffer_rate_pct")
    if rate is not None:
        rate = num(rate, "buffer_rate_pct")
        if not 0 <= rate <= 100:
            raise ValueError("buffer_rate_pct must be between 0 and 100")
        result["buffer_rate_pct"] = rate
        result["estimated_after_buffer_tco2e"] = net_before_buffer * (1 - rate / 100.0)
    else:
        result["buffer_rate_pct"] = None

    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_json")
    ap.add_argument("-o", "--output")
    args = ap.parse_args()

    data = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    result = calculate(data)
    out = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(out + "\n", encoding="utf-8")
    else:
        print(out)

if __name__ == "__main__":
    main()
