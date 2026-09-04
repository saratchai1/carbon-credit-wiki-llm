# Premium T-VER Mangrove Reforestation — MOC1 / Siam TC

> **Project identity warning:** this is **not** the same project package as `projects/group-1-mangrove-reforestation.md`, even though both use “Group 1” wording and share a 2024-06-21 registration-certificate date. Never merge their boundaries, plot lists, VVB evidence, or carbon figures. See [[projects/project-identity-map]].

## Status

- Project ID: `premium-tver-moc1-stc-group-1`
- Lifecycle: `REGISTERED_PROJECT`
- Carbon-number status: `PROJECT_ESTIMATE` for registered ex-ante figures
- Actual issued-credit status: `NOT_EVIDENCED`
- Standard: Premium T-VER
- Registered methodology: T-VER-P-METH-13-02 v01
- Crediting period: 2023-10-01 to 2038-09-30 (15 years)
- Registration certificate date: 2024-06-21
- Project planting/maintenance commitment described in validation evidence: 30 years

Do **not** describe 5,739 tCO2e/year as issued credits. The ingested package contains registration/ex-ante evidence, not a completed Monitoring Report + Verification Report + TGO issuance record for an actual monitoring period.

## Project identity

Thai: **โครงการฟื้นฟูป่าชายเลน เพื่อระบบนิเวศที่ยั่งยืนของประเทศไทย (กลุ่ม 1)**  
English: **mangrove reforestation for sustainable environment in Thailand (group 1)**

Owner/developer: Department of Marine and Coastal Resources (DMCR)  
Co-developer: Siam TC Technology Co., Ltd.

Independent VVB in the ingested validation report: **Bureau Veritas Certification (Thailand) Ltd.**

Primary sources:
- `PROJECT-MOC1-STC-PDD-2024-06-12-V03`
- `PROJECT-MOC1-STC-CALC-2024-06-13`
- `PROJECT-MOC1-STC-VALIDATION-2024-06-13-V02`
- `PROJECT-MOC1-STC-SDG-SAFEGUARDS-2024-01-30-V01`
- `PROJECT-MOC1-STC-CERTIFICATE-2024-06-21`
- `PROJECT-MOC1-STC-SHAPEFILE-2024-06-14`

## Canonical project boundary

### Area semantics

- Administrative/allocated area in calculation workbook: **750.65 rai**
- Final project area used by the validated/certificate ex-ante calculation: **554.32 rai** (~88.69 ha)
- Number of project plots: **19**
- Provinces: **8**

Use **554.32 rai** for this registered ex-ante package unless later verified project evidence formally changes the accounting boundary. Do not substitute the 750.65 rai allocated area.

### Province totals

| Province | Plots | Project area (rai) |
|---|---:|---:|
| Pattani | 2 | 10.69 |
| Phang Nga | 2 | 13.14 |
| Rayong | 10 | 176.42 |
| Surat Thani | 1 | 157.55 |
| Chachoengsao | 1 | 98.75 |
| Prachuap Khiri Khan | 1 | 30.49 |
| Satun | 1 | 48.48 |
| Krabi | 1 | 18.80 |
| **Total** | **19** | **554.32** |

### Site-condition strata from workbook

| Site condition | Plots | Project area (rai) |
|---|---:|---:|
| Former shrimp/aquaculture ponds | 9 | 108.34 |
| Cleared / planting-ready area | 7 | 170.88 |
| Accreting mudflat | 3 | 275.10 |
| **Total** | **19** | **554.32** |

Structured plot-level data: `data/project-moc1-stc-plots.csv`.

## Registered ex-ante carbon estimate

### Headline

- Baseline: **0 tCO2e** in the registered ex-ante package
- Leakage: **0 tCO2e** in the registered ex-ante package
- Reported average: **5,739 tCO2e/year**
- 15-year registered ex-ante total/endpoint: **86,085.90 tCO2e**

### Tree component

The validated workbook block uses:

- Project area `A = 554.32 rai`
- Tree sequestration increment `9.4 tCO2e/rai/year`

Arithmetic trace:

`554.32 × 9.4 = 5,210.608 tCO2e/year`

Over 15 years:

`5,210.608 × 15 = 78,159.12 tCO2e`

### SOC component

The workbook applies:

- `dSOC = 0.26 tC/rai/year`
- carbon-to-CO2 conversion `44/12`

Annual SOC contribution:

`554.32 × 0.26 × (44/12) = 528.4517333 tCO2e/year`

Over 15 years:

`528.4517333 × 15 = 7,926.776 tCO2e`

### Combined ex-ante figure

`78,159.12 + 7,926.776 = 86,085.896 tCO2e`

Average:

`86,085.896 / 15 = 5,739.0597333 tCO2e/year`

Rounded registration/certificate value: **5,739 tCO2e/year**.

## Legacy calculation block inside the workbook

Status: `SUPERSEDED_WITHIN_PROJECT_PACKAGE`

The same workbook also contains an older/alternative block using:

- Area = **535.46 rai**
- Tree = **5,033.324 tCO2e/year**
- SOC = **510.4718667 tCO2e/year**
- Combined = **5,543.7958667 tCO2e/year**
- 15-year total = **83,156.938 tCO2e**

Do **not** use this block as the current registered result. The validation report and TGO registration certificate support the 554.32-rai / 5,739-tCO2e/year package. Preserve the 535.46-rai block only as calculation history/provenance.

## Baseline, emissions and leakage

The project package treats the baseline tree-carbon change as zero under its stated eligibility/baseline conditions. Ex-ante leakage is reported as zero. The workbook also shows project-emission term `GHG_E,t = 0` in the registered prediction block.

Do not carry these zeros into an actual monitoring-period calculation without checking the monitoring evidence and current methodology/tool requirements.

## Species and biomass evidence

Validation evidence states that planted species are mangrove tree species and includes examples such as:
- Rhizophora mucronata — โกงกางใบใหญ่
- Rhizophora apiculata — โกงกางใบเล็ก
- Avicennia marina — แสมทะเล
- Avicennia alba — แสมขาว
- Bruguiera gymnorhiza — พังกาหัวสุมดอกแดง
- Excoecaria agallocha — ตาตุ่มทะเล

The validation report references Komiyama et al. (2005) mangrove allometry and provides species wood-density values. However, the exact equation text/range must be verified against the source PDF/primary publication before a production calculator promotes it to an approved allometry registry entry. Treat the current extraction as `REFERENCE_ONLY`, not automatically `VERIFICATION_READY`.

## Carbon MRV design

### Sampling

The registered project approach describes **stratified random sampling** for project carbon assessment and **repeated measurement** in sample plots for change over time.

Important validation-stage nuance: because the baseline was assessed as zero, the validation report notes that baseline stratification/sample plots had not yet been established for baseline measurement. Do not interpret “no baseline sample plots” as meaning future project monitoring does not require sampling.

### Tree measurements

DBH is a material monitoring variable in the validation evidence. Species identity and biomass-model applicability must remain traceable per measured tree/sample plot.

For actual calculations, preflight the PDD-locked requirements and the current TGO tool/version. Do not infer `tree count -> tCO2e` directly.

### Remote sensing / drone / LiDAR

Supporting roles include:
- boundary and area QA,
- stratification,
- canopy/cover monitoring,
- survival/change screening,
- sample targeting,
- QA/QC,
- calibrated secondary variables where methodology-compatible.

Do not use `tree_count -> tCO2e` or `NDVI/canopy -> tCO2e` directly without an approved/calibrated model, ground truth and uncertainty trace.

## Sustainable development / safeguards

The SD/Safeguards report confirms the project had started on **2023-10-01**. Evidence extracted includes:
- SDG 13 climate action / increased carbon sequestration: growth of planted seedlings monitored every **5 years**,
- SDG 14 life below water / mangrove ecosystem restoration,
- employment/income indicator monitored **annually**.

Keep carbon-MRV cadence separate from SDG indicator cadence; they serve different reporting purposes.

## Validation status

VVB: Bureau Veritas Certification (Thailand) Ltd.  
Validation report: 2024-06-13, version 2, validating PDD version 3 dated 2024-06-12.

The report records **Certify with Comment**, with the comment linked to the project’s use of the 9.4 tCO2e/rai/year Rhizophora increment for the ex-ante estimate.

Registration certificate evidence dated 2024-06-21 confirms Premium T-VER registration and the 5,739 tCO2e/year ex-ante figure.

## Project duration vs crediting period

Keep these fields separate:
- project planting/maintenance commitment described in validation evidence: **30 years**,
- crediting period: **15 years** (2023-10-01 to 2038-09-30).

A project can remain under maintenance after the crediting period represented in this registration package.

## Current evidence gaps

Not yet evidenced in this ingest:
- completed Monitoring Report for an actual crediting/monitoring period,
- Verification Report for actual removals,
- TGO issuance/certification evidence for an actual credit batch,
- final non-permanence risk/buffer result for an issuance period,
- inspected shapefile archive contents, CRS and feature-level geometry validation,
- verified parameter-domain/range evidence for the Komiyama equations quoted in the validation package.

Until those are added, current actual credits must not be reported as `CERTIFIED_CREDIT`.

## Source notes

- [[sources/project-moc1-stc-pdd-2024-06-12]]
- [[sources/project-moc1-stc-calculation-workbook-2024-06-13]]
- [[sources/project-moc1-stc-validation-2024-06-13]]
- [[sources/project-moc1-stc-sdg-safeguards-2024-01-30]]
- [[sources/project-moc1-stc-certificate-2024-06-21]]
- [[sources/project-moc1-stc-shapefile-manifest-2024-06-14]]
- `raw/project-moc1-stc-drive-manifest-2024-06-14.md`
