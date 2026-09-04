---
source_id: STC-VSD-G2-DRIVE-FOLDER
source_type: project_primary_evidence_bundle
project_id: STC-VSD-STANDARD-TVER-GROUP-2
retrieved_on: 2026-09-04
status: ACTIVE_REFERENCE
raw_copy_policy: EXTERNAL_REFERENCE_ONLY_PUBLIC_REPO
---

# Source Note — Standard T-VER Group 2 (Siam TC + Visut) Google Drive bundle

## Critical disambiguation

This source is **not** the existing project `STC-STANDARD-TVER-GROUP-2` from Drive folder `1naQZbzf1ZsbmIoI62huW04946eICuglE`.

Two different registered Standard T-VER projects currently use “Group 2” wording in the Wiki:

| Wiki project ID | Drive folder | Project area | Plots | Reported annual ex-ante quantity | Crediting period |
|---|---|---:|---:|---:|---|
| `STC-STANDARD-TVER-GROUP-2` | `1naQZbzf1ZsbmIoI62huW04946eICuglE` | 9,005.55 rai | 50 | 84,652 tCO2eq/year | 2023-11-15 to 2033-11-14 |
| `STC-VSD-STANDARD-TVER-GROUP-2` | `1Wj-tjfkkmgYdiCbJnA7CoXwjgMqHJbGg` | 6,775.53 rai | 22 | 63,689 tCO2eq/year | 2024-05-31 to 2034-05-30 |

**Never merge their boundaries, crediting periods, baseline values, calculation workbooks or expected quantities.**

## Project identity

- Thai: โครงการปลูกป่าชายเลนช่วยโลกลดก๊าซเรือนกระจกในประเทศไทย (กลุ่ม 2)
- English: Greenhouse Gas Reduction with Mangrove Reforestation in Thailand (Group 2)
- Standard: Standard T-VER
- Project form: bundled, large-scale
- Owner/developer: กรมทรัพยากรทางทะเลและชายฝั่ง (DMCR)
- Co-developers: บริษัท สยาม ทีซี เทคโนโลยี จำกัด and บริษัท วิสุทธิ คอนซัลแตนท์ จำกัด
- Project plots: 22
- Project area used for registered calculation: 6,775.53 rai
- Provinces: Chumphon, Phang Nga, Trang, Satun, Samut Songkhram, Pattani, Krabi, Phuket
- Crediting period: 31 May 2024 – 30 May 2034
- Registration certificate observed date: 28 Aug 2024

## Methodology lock

- `T-VER-S-METH-13-03` v01 — Large Scale Sustainable Forestation Project
- `T-VER-S-TOOL-01-01` v01 — Calculation for Carbon Sequestration in Tree

This is a project-specific historical/registered lock. It does not establish current 2026 eligibility of this Standard T-VER version for a new project.

## Registered ex-ante quantity

- Baseline tree carbon stock in workbook: **362,962.8144 tCO2eq**
- Project tree carbon stock at year 10: **999,862.6344 tCO2eq**
- Workbook exact net increment over 10 years: **636,899.82 tCO2eq**
- PDD reported 10-year expected removal: **636,899 tCO2eq**
- Workbook exact one-year increment: **63,689.982 tCO2eq/year**
- PDD/certificate reported expected quantity: **63,689 tCO2eq/year**
- Project calculation uses project area 6,775.53 rai and mangrove increment input 9.4 tCO2eq/rai/year.
- Ex-ante leakage in the PDD calculation is reported as 0 tCO2eq.

These figures are `PROJECT_ESTIMATE` values from registered/validated ex-ante evidence. They are not actual monitoring-period `VERIFIED_RESULT` and not `CERTIFIED_CREDIT` issuance evidence.

## Calculation workbook evidence

`MOC2_VSD-25-06-24.xlsx` contains individual-tree records including species, tag, DBH, wood density, aboveground biomass, belowground biomass, total dry biomass, carbon factor and tCO2eq conversion.

Observed workbook components:
- `CF = 0.4715 tC/t dry biomass`
- `44/12` molecular conversion
- AGB equation observed in sheets: `0.251 × ρ × D^2.46`
- BGB equation observed in sheets: `0.199 × ρ^0.899 × D^2.22`

Equation applicability must be checked by species/row/source. Do not apply these universally to new measurements without provenance/domain checks.

## Baseline stratification / satellite precedent

The PDD uses Landsat-8 Forest Canopy Density (FCD) information to support baseline stratification and sample allocation.

Strata split by:
- Gulf of Thailand vs Andaman coast; and
- FCD high `>65%`, medium `30–65%`, low `<30%` canopy cover.

The PDD describes vegetation, bare-soil and shadow-index inputs in the FCD workflow. This is evidence for:

`satellite → stratification/sample design → field measurement → carbon calculation`

It is not evidence for direct `NDVI/FCD/tree-count → carbon credit` conversion.

## Field and monitoring precedent

Sample plots described:
- 40 × 40 m = 1 rai
- 20 × 40 m = 0.5 rai

Tree measurements include tree count, species, tag, GBH and DBH.

For Rhizophora where prop roots rise above the normal 1.30 m DBH point, the PDD states diameter is measured **30 cm above the prop-root point**.

Monitoring parameters observed:
- project coordinates: every 5 years
- tree carbon stock `CTT_t`: every 5 years
- tree diameter/DBH survey: every 3 years
- burned area: every 5 years using field and/or satellite/aerial evidence
- fossil-fuel-use evidence: at least monthly

## Validation evidence

VGreen KU Validation Report dated 1 Jul 2024 reviewed PDD revision 02 dated 25 Jun 2024 at a reasonable level of assurance.

It records:
- 4 Material Misstatements
- 2 Misstatements
- 4 Nonconformities
- all addressed/closed in the revised project documentation

Reusable QC lessons:
1. exclude water/channel areas not participating in the project boundary;
2. reconcile sample-plot areas/coordinates across GIS, PDD and workbook;
3. recalculate baseline/project totals whenever project area changes;
4. verify tree tag ↔ species mapping;
5. do not include species/allometric equations unsupported by field evidence; an earlier Casuarina/สนทะเล treatment was challenged;
6. verify botanical/growth-form descriptions;
7. keep monitoring parameters aligned with the selected methodology/tool.

## Co-benefit evidence

The Co-benefit Report describes increased green area and biodiversity from mangrove planting/restoration over the 6,775.53-rai project. Keep co-benefit claims separate from carbon quantity calculations.

## Source folder

- Google Drive folder: https://drive.google.com/drive/folders/1Wj-tjfkkmgYdiCbJnA7CoXwjgMqHJbGg
- Raw external-source manifest: `raw/project-g2-stc-vsd-drive-source-manifest-2026-09-04.md`
