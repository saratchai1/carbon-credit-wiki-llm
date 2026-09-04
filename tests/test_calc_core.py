from tools.calc_core import calculate

def test_core_equation():
    d = {
        "calculation_id": "TEST",
        "methodology": {"code": "T-VER-P-METH-13-02", "version": "01"},
        "project_carbon_change_tco2e": {
            "tree": 100.0, "sapling": 10.0, "deadwood": 0.0, "soc": 5.0
        },
        "project_emissions_tco2e": {"burning": 2.0, "fuel": 3.0},
        "baseline_net_removal_tco2e": 20.0,
        "leakage_tco2e": 5.0,
        "buffer_rate_pct": 10.0
    }
    r = calculate(d)
    assert r["actual_net_project_removal_tco2e"] == 110.0
    assert r["net_anthropogenic_removal_before_buffer_tco2e"] == 85.0
    assert r["estimated_after_buffer_tco2e"] == 76.5
