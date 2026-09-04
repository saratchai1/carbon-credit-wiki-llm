---
source_id: PROJECT-G1-CALC-2024-04-30
title: Group 1 carbon calculation workbook
authority: Project calculation evidence
document_code: VSD_MOC1-30-04-24.xlsx
version: "2024-04-30 working/final calculation set"
published_or_effective_date: 2024-04-30
retrieved_on: 2026-09-04
status: ACTIVE
url: https://docs.google.com/spreadsheets/d/1hFdcZ_7cNkb4RQ4leCQCUuQYOPQvuCt1/edit
---

# Source Note — Group 1 Calculation Workbook

## Scope
Project calculation workbook supporting the ex-ante carbon figures reported in the PDD and validation package.

## Claims extracted
- Baseline: 0 tCO2e.
- Project area: 1,195.64 rai.
- Planted-tree density used in the workbook: 711 trees/rai.
- Tree MAI: 9.40 tCO2e/rai/year with SD ±4.60; report range shown as 196–885 trees/rai.
- Tree carbon change reaches 168,585.24 tCO2e at year 15.
- SOC component shown as 1,139.8434667 tCO2e in the workbook calculation.
- Project total at year 15: 169,725.0834667 tCO2e.
- Reported 15-year average: 11,315 tCO2e/year.
- Leakage: 0.

## Equation / parameter trace
- Tree component is arithmetically consistent with `1,195.64 rai × 9.40 tCO2e/rai/year = 11,239.016 tCO2e/year`.
- Workbook uses `44/12` to convert carbon to CO2.
- SOC input displays `0.26 tC/rai/year` and project area 1,195.64 rai, producing `1,139.8434667 tCO2e`.

## Important interpretation
The workbook presents the year-15 project total as the endpoint/cumulative stock-change estimate and divides that total by 15 for the annual average. Do not sum the displayed cumulative year rows as separate annual credits.

## Conflict / reconciliation required
The methodology/PDD text states default `dSOC = 0.26 tC/rai/year` from planting through planting year +20, but the workbook summary contributes 1,139.84 tCO2e of SOC to the 15-year endpoint rather than an obviously accumulated 15-year SOC amount. This implementation must be reconciled against the exact registered methodology equation and the validated workbook before any calculator hard-codes SOC behavior.

Status of this issue: `CONFLICT_REQUIRES_RECONCILIATION` for calculator implementation; it does not invalidate the fact that the validated project package reports 169,725.08 tCO2e ex ante.

## Applicability
Use for reproducing the registered ex-ante estimate only. It is not a Monitoring Report, Verification Report, or issuance record.

## Wiki pages affected
- `projects/group-1-mangrove-reforestation.md`
- `data/project-profile.yaml`
- `sources/source-registry.md`
- `log.md`
