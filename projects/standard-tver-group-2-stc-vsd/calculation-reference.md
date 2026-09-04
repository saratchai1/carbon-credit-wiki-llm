# Calculation Reference — STC + VSD Standard T-VER Group 2

## Source

Primary workbook: `MOC2_VSD-25-06-24.xlsx` / `STC-VSD-G2-CALC-XLSX`.

This is a project-specific ex-ante reference, not a generic calculator.

## Tree-level chain observed

`species + DBH + wood density (ρ) → AGB + BGB → dry biomass → carbon → CO2eq`

Observed workbook equations:

`AGB_kg = 0.251 × ρ × D^2.46`

`BGB_kg = 0.199 × ρ^0.899 × D^2.22`

`B_total_tdry = (AGB_kg + BGB_kg) / 1000`

`C_tC = B_total_tdry × 0.4715`

`C_tCO2e = C_tC × 44/12`

Do not assume the same allometry applies to every species or DBH range; the workbook contains species/wood-density/source information that must remain part of the evidence chain.

## Baseline strata

| Coast | FCD | Carbon stock per rai (tCO2eq/rai) | Area (rai) | Baseline tree carbon (tCO2eq) |
|---|---|---:|---:|---:|
| Gulf of Thailand | high | 54.57 | 1,821.64 | 99,406.8948 |
| Gulf of Thailand | medium | 29.39 | 975.86 | 28,680.5254 |
| Gulf of Thailand | low | 5.05 | 251.25 | 1,268.8125 |
| Andaman | high | 71.66 | 2,733.84 | 195,906.9744 |
| Andaman | medium | 41.24 | 847.43 | 34,948.0132 |
| Andaman | low | 18.91 | 145.51 | 2,751.5941 |
| **Total** |  |  | **6,775.53** | **362,962.8144** |

See `baseline-strata.csv`.

## Ex-ante increment

`6,775.53 rai × 9.4 tCO2eq/rai/year = 63,689.982 tCO2eq/year`

Preserve both representations:
- workbook exact: `63,689.982 tCO2eq/year`
- PDD/certificate reported: `63,689 tCO2eq/year`

At year 10:
- workbook exact net increment: `636,899.82 tCO2eq`
- PDD reported expected total: `636,899 tCO2eq`
- project tree carbon stock: `999,862.6344 tCO2eq`

See `projection.csv`.

## Accounting warning

These values are `PROJECT_ESTIMATE` outputs from registered/validated ex-ante documents. Do not infer actual issued credits from them.

Do not copy calculation inputs from [[../standard-tver-group-2/README]]: that separate Group 2 project has different area, baseline and registered quantity despite sharing the same methodology code.
