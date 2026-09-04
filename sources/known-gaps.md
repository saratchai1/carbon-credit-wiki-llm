# Known Gaps

## Group 1 project status after 2026-09-04 ingest

The registered ex-ante configuration for **Greenhouse Gas Reduction with Mangrove Reforestation in Thailand (Group 1)** is now ingested and supports `PROJECT_ESTIMATE`-grade reproduction of the registered design estimate.

Available project evidence now includes:
- registered PDD / methodology-version lock,
- validated project area = 1,195.64 rai across 40 plots / 7 provinces,
- allocation-vs-accounting-area distinction,
- project strata and sampling design,
- carbon-pool inclusion choices,
- registered ex-ante MAI/workbook values,
- baseline/project-emission/leakage configuration,
- Validation Report and registration certificate,
- SD/Safeguards monitoring cadences,
- external shapefile package manifest.

## Group 1 remaining gaps before actual verified/certified credit claims

1. actual Monitoring Report for a completed monitoring period
2. tree-level/sample-plot measurements for the relevant monitoring dates
3. final monitoring-period uncertainty calculation and conservative deduction
4. Verification Report for actual removals
5. TGO issuance/certification evidence for the actual credit batch
6. non-permanence risk assessment and issuance-period buffer rate/result
7. raw shapefile ZIP content ingested or independently hashed/validated for CRS, geometry and feature schema
8. production reconciliation of SOC workbook implementation versus the registered methodology equation/text
9. planting dates/cohorts at sufficient detail for monitoring-period calculations
10. species composition and tree-level measurement-point evidence sufficient for ex-post allometry checks
11. activity evidence if future monitoring introduces burning/fuel emissions or changes the registered zero/not-considered assumptions

Until items 1–5 are available, do not report actual current credits as `VERIFIED_RESULT` or `CERTIFIED_CREDIT`.

## STC+VSD Standard T-VER Group 2 remaining gaps

The registered ex-ante configuration for `STC-VSD-STANDARD-TVER-GROUP-2` supports `PROJECT_ESTIMATE` reproduction, but not actual issued-credit claims.

Remaining gaps:
1. actual Monitoring Report for a completed monitoring period
2. monitoring-round tree/sample-plot data for the relevant dates
3. monitoring-period uncertainty/conservative treatment under the project-locked methodology/tool
4. Verification Report for actual removals
5. TGO issuance/certification evidence for the actual credit batch
6. raw `Shape.rar` and sample-plot archive independently unpacked/hashed and checked for CRS, geometry, feature schema and equivalence to the revised PDD boundary
7. complete species/row-level allometry provenance/domain checks before applying workbook equations to new measurements
8. evidence for any changes in project emissions/leakage from ex-ante assumptions
9. current TGO status/transition check before using `T-VER-S-METH-13-03` v01 for a new project/submission

Until items 1–5 are available, do not report actual current STC+VSD Group 2 credits as `VERIFIED_RESULT` or `CERTIFIED_CREDIT`.

## Methodology gap to monitor

TGO 2026 work plan lists the mangrove A/R methodology and relevant forestry tools for revision. The wiki must recheck current versions before any submission-grade work and distinguish current-tool rules from requirements locked by registered PDD/transition provisions.

`T-VER-S-METH-13-03` v01 is retained only as registered-project historical evidence; current new-project validity is not asserted by this ingest.
