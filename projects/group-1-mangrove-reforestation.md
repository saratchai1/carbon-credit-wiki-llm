# Premium T-VER Mangrove Reforestation — Group 1

## Status

- Project lifecycle: `REGISTERED_PROJECT`
- Carbon-number status: `PROJECT_ESTIMATE` for ex-ante figures
- Actual issued-credit status: `NOT_EVIDENCED`
- Standard: Premium T-VER
- Registered methodology: T-VER-P-METH-13-02 v01
- Crediting period: 2023-10-01 to 2038-09-30 (15 years)
- Registration certificate date: 2024-06-21

Do **not** describe the registered 11,315 tCO2e/year ex-ante value as issued or certified credits. No Monitoring Report + Verification Report + TGO issuance evidence has been ingested for an actual monitoring period.

## Project identity

Thai: **โครงการปลูกป่าชายเลนช่วยโลกลดก๊าซเรือนกระจกในประเทศไทย (กลุ่ม 1)**  
English: **Greenhouse Gas Reduction with Mangrove Reforestation in Thailand (Group 1)**

Owner/developer: Department of Marine and Coastal Resources (DMCR)  
Co-developers: Siam TC Technology Co., Ltd. and Wisut Consultant Co., Ltd.

Primary project sources:
- `PROJECT-G1-PDD-2024-04-30-V06`
- `PROJECT-G1-CALC-2024-04-30`
- `PROJECT-G1-VALIDATION-2024-05-01-V01`
- `PROJECT-G1-SDG-SAFEGUARDS-2024-04-23-V01`
- `PROJECT-G1-CERTIFICATE-2024-06-21`
- `PROJECT-G1-SHAPEFILE-2024-06-11`

## Canonical project boundary

### Area semantics
- Allocated area: **1,472.13 rai** — administrative allocation; do not use automatically in carbon accounting.
- Final validated project area: **1,195.64 rai** (~191.30 ha) — accounting boundary.

The distinction is mandatory. Validation previously identified material problems with missing coordinates and an unclear boundary that had not removed non-participating area. The revised PDD corrected these issues. For calculations, default to 1,195.64 rai unless later verified project evidence formally changes the boundary.

### Province totals

| Province | Plots | Project area (rai) |
|---|---:|---:|
| Trat | 8 | 108.98 |
| Rayong | 4 | 121.94 |
| Nakhon Si Thammarat | 2 | 500.76 |
| Phang Nga | 15 | 168.46 |
| Satun | 8 | 252.25 |
| Pattani | 2 | 14.71 |
| Krabi | 1 | 28.54 |
| **Total** | **40** | **1,195.64** |

### Site-condition strata

| Stratum | Plots | Project area (rai) |
|---|---:|---:|
| Former shrimp ponds | 12 | 230.92 |
| Cleared / planting-ready | 24 | 449.25 |
| Accreting mudflat | 4 | 515.47 |
| **Total** | **40** | **1,195.64** |

These strata matter because the registered monitoring design uses stratified random sampling and satellite imagery to support canopy/area characterization.

## Registered ex-ante carbon estimate

### Headline
- 15-year ex-ante endpoint/total reported: **169,725.08 tCO2e**
- Reported average: **11,315 tCO2e/year**
- Baseline: **0 tCO2e** under the registered baseline conditions
- Leakage: **0 tCO2e** in the ex-ante package

### Tree component
Registered ex-ante parameters include:
- Area = 1,195.64 rai
- MAI = 9.40 tCO2e/rai/year for Rhizophora spp. in the initial estimate

Arithmetic trace:

`1,195.64 rai × 9.40 tCO2e/rai/year = 11,239.016 tCO2e/year`

Over 15 years:

`11,239.016 × 15 = 168,585.24 tCO2e`

### SOC component
The project PDD includes SOC as an optional pool and cites the default parameter:

`dSOC = 0.26 tC/rai/year`

with methodology text describing use from planting year through planting year +20 unless another value is demonstrated.

The project workbook contributes **1,139.8434667 tCO2e** as the SOC component to the reported 15-year endpoint:

`168,585.24 + 1,139.8434667 = 169,725.0834667 tCO2e`

Then:

`169,725.0834667 / 15 ≈ 11,315 tCO2e/year`

### SOC implementation warning
Status: `CONFLICT_REQUIRES_RECONCILIATION`

The PDD/methodology wording and workbook implementation must be reconciled before building a production carbon calculator. Do not independently reinterpret the default 0.26 tC/rai/year into a different 15-year SOC result and then call it the registered result. Preserve both:
1. the validated package's reported ex-ante value, and
2. the unresolved implementation question for calculator logic.

## Baseline and exclusions

The registered package treats baseline tree-carbon change as zero when the required conditions are met, including:
- pre-existing trees are not felled,
- pre-existing trees are not killed/destroyed by project implementation,
- pre-existing trees are not measured and counted as project-credit trees.

Optional sapling and dead-wood pools are not included in the registered calculation described by the PDD. Tree aboveground and belowground biomass are included. SOC is included.

## Project emissions

The PDD describes:

`GHG_E,t = GHG_Burning,t + GHG_Fuel,t`

For this project package:
- biomass-burning emissions are not considered because project preparation/management does not use burning,
- fossil-fuel emissions are not considered under the stated small-project treatment.

This is a registered-project assumption/configuration. If future monitoring evidence shows burning or a methodology/rule change alters treatment, re-evaluate rather than reusing zero blindly.

## Carbon MRV design

### Sampling
Registered approach: **stratified random sampling**.

Satellite imagery supports canopy-cover assessment and stratification. The three site-condition classes above are materially different and should remain explicit in the digital data model.

### Tree measurements
For the registered PDD monitoring approach:
- tree species is recorded,
- tree size/height is measured in sample plots,
- trees below the DBH threshold are handled using D0/root-collar diameter as described in the PDD,
- for planted trees with diameter >=4.5 cm and height >1.3 m, DBH at 1.3 m is used in the PDD description,
- Komiyama et al. (2005) equations are described for aboveground/belowground biomass in the PDD sampling method.

Important: the current wiki also contains newer/general TGO measurement-tool rules. Before an actual verification-period calculation, preflight the current tool/version and the PDD-locked requirements. Do not silently replace the registered measurement convention.

### Monitoring cadence
Keep separate cadences by purpose:

| Purpose | Documented cadence |
|---|---|
| Tree-carbon MRV in PDD | at least every 3 years |
| SDG 10 employment/income | annually |
| SDG 13 growth indicator in SD/Safeguards | every 5 years |
| SDG 14 survival/area/ecological monitoring | annually, including satellite imagery |

These are not conflicting when treated as separate monitoring obligations.

### Uncertainty
Sampling uncertainty is part of the registered accounting approach. If uncertainty exceeds 10%, apply the conservative deduction required by the applicable T-VER tool/table. Never report a point estimate as verification-ready without the uncertainty trace.

## Digital MRV data model implied by the PDD

A system intended to support this project should preserve at least:

`project -> boundary version -> plot -> stratum -> sample plot -> monitoring event -> tree -> species -> measurement point method -> D0/DBH -> height -> allometry -> AGB/BGB -> carbon stock -> stock change -> uncertainty -> deductions -> net removal`

Remote-sensing/AI evidence should attach to the relevant boundary/stratum/monitoring event and must not bypass the field/allometry/uncertainty chain unless a methodology-approved calibrated model supports it.

## Satellite / drone / LiDAR role

Allowed/supporting uses include:
- boundary QA,
- stratification,
- canopy cover,
- survival/change screening,
- sampling support,
- QA/QC,
- secondary variables in a validated double-sampling/calibration workflow.

Do not use `tree_count -> tCO2e` or `NDVI/canopy -> tCO2e` directly without methodology-compatible calibration, ground truth and uncertainty evidence.

## Sustainable development / safeguards

Project package includes at least:
- SDG 10: employment/income generation,
- SDG 13: increased carbon sequestration / growth,
- SDG 14: mangrove increase/restoration and survival/growth monitoring.

Annual satellite-based project-area/ecological monitoring is explicitly documented for SDG 14.

## Credit sharing described in PDD

Framework recorded in the PDD:
- Siam TC: up to 85%,
- Wisut Consultant: up to 5%,
- DMCR: at least 10%,
- or as otherwise agreed.

The PDD further describes part of the DMCR share supporting local coastal-community conservation through local authorities. Treat this as project-governance evidence, not as proof of the final allocation of any specific future issuance batch.

## Validation status

VVB: VGreen KU Co., Ltd.  
Validation opinion: **CERTIFY**.

Validation findings included 2 Material Misstatements, 1 lower-level Misstatement and 19 Nonconformities. The report states that clarifications/evidence were provided and PDD revision 06 dated 2024-04-30 addressed and closed the issues.

Boundary findings `MM 01` and `MM 02` are retained in this wiki because they are important QA lessons for GIS and carbon calculation.

## Current evidence gaps

The following are not yet evidenced in the source set ingested on 2026-09-04:
- actual Monitoring Report for a completed crediting/monitoring period,
- Verification Report for actual removals,
- TGO issuance/certification record for actual credits,
- non-permanence risk result and final buffer rate for an issuance period,
- raw shapefile content hash/CRS/feature-level validation inside this GitHub repo,
- reconciled production implementation of SOC calculation logic.

Until those are added, actual current credits must not be reported as `CERTIFIED_CREDIT`.

## Source notes

- [[sources/project-g1-pdd-2024-04-30]]
- [[sources/project-g1-calculation-workbook-2024-04-30]]
- [[sources/project-g1-validation-2024-05-01]]
- [[sources/project-g1-sdg-safeguards-2024-04-23]]
- [[sources/project-g1-certificate-2024-06-21]]
- [[sources/project-g1-shapefile-manifest-2024-06-11]]
