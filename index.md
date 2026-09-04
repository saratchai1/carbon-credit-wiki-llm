# Index

## Core
- [[README]] — วิธีใช้ wiki
- [[AGENTS]] — กฎสำหรับ LLM agent
- [[architecture/wiki-architecture]] — raw/wiki/schema
- [[architecture/ingest-workflow]] — ingest/query/lint

## Projects
- [[projects/project-identity-map]] — mandatory disambiguation map because two distinct Premium T-VER project packages use “Group 1” wording
- [[projects/group-1-mangrove-reforestation]] — `premium-tver-mangrove-group-1`; 40 plots / 1,195.64 rai / 11,315 tCO2e/year ex-ante
- [[projects/moc1-stc-mangrove-reforestation]] — `premium-tver-moc1-stc-group-1`; 19 plots / 554.32 rai / 5,739 tCO2e/year ex-ante
- [[projects/standard-tver-group-2/README]] — Registered Standard T-VER Group 2; project-specific methodology lock, baseline, sequestration, POM, allometry, monitoring, spatial evidence and validation/registration

## Standard / Methodology
- [[standards/current-standard]] — standard ที่ตั้งเป็น default และ version watch
- [[standards/other-standards]] — มาตรฐานอื่น ห้ามปะปน
- [[methodologies/T-VER-P-METH-13-02]] — ระเบียบวิธีปลูกป่าชายเลน
- [[methodologies/T-VER-S-METH-13-03]] — Standard T-VER large-scale sustainable forestation; Group 2 historical project lock
- [[methodologies/eligibility-checklist]] — checklist ก่อนคำนวณ

## Calculation
- [[calculation/calculation-chain]] — สมการหลัก
- [[calculation/tree-biomass-and-carbon]] — biomass/tree carbon
- [[calculation/soil-organic-carbon]] — SOC
- [[calculation/project-emissions]] — burning/fuel
- [[calculation/baseline-and-leakage]] — baseline/leakage
- [[calculation/uncertainty]] — sampling uncertainty/conservative deduction
- [[calculation/credit-status]] — estimate vs verified vs certified

## Monitoring / MRV
- [[monitoring/field-measurement]] — field DBH/species/sample plots
- [[monitoring/remote-sensing-ai-lidar]] — drone/satellite/LiDAR
- [[monitoring/qa-qc]] — QA/QC

## Risk
- [[risk/non-permanence-buffer]] — risk and buffer

## Data
- [[data/data-dictionary]] — field definitions
- [[data/evidence-hierarchy]] — evidence tiers
- `data/project-profile.yaml` — profile for `premium-tver-mangrove-group-1`
- `data/project-profile-moc1-stc.yaml` — profile for `premium-tver-moc1-stc-group-1`
- `data/project-moc1-stc-plots.csv` — 19-plot structured boundary/condition table for MOC1/STC
- `data/tree_measurements.csv` — template
- `data/planting_cohorts.csv` — template
- `data/activity_emissions.csv` — template

## Sources
- [[sources/source-registry]]
- [[sources/known-gaps]]
- `raw/project-g1-drive-source-manifest-2026-09-04.md` — immutable external-source provenance snapshot
- [[sources/project-g1-pdd-2024-04-30]]
- [[sources/project-g1-calculation-workbook-2024-04-30]]
- [[sources/project-g1-validation-2024-05-01]]
- [[sources/project-g1-sdg-safeguards-2024-04-23]]
- [[sources/project-g1-certificate-2024-06-21]]
- [[sources/project-g1-shapefile-manifest-2024-06-11]]
- `raw/project-moc1-stc-drive-manifest-2024-06-14.md` — immutable external-source provenance snapshot for MOC1/STC
- [[sources/project-moc1-stc-pdd-2024-06-12]]
- [[sources/project-moc1-stc-calculation-workbook-2024-06-13]]
- [[sources/project-moc1-stc-validation-2024-06-13]]
- [[sources/project-moc1-stc-sdg-safeguards-2024-01-30]]
- [[sources/project-moc1-stc-certificate-2024-06-21]]
- [[sources/project-moc1-stc-shapefile-manifest-2024-06-14]]
- `raw/project-g2-drive-source-manifest-2026-09-04.md` — immutable external-source provenance snapshot for Standard T-VER Group 2
- [[sources/stc-standard-tver-group2-drive]] — Group 2 registration/PDD/calculation/validation/GIS source bundle

## Templates
- [[templates/project-profile]]
- [[templates/calculation-run]]
- [[templates/source-note]]

## Tools
- `tools/calc_core.py` — high-level arithmetic; does not certify credits
- `tools/wiki_lint.py` — internal wiki lint

## Logs
- [[log]]
- `runs/` — immutable calculation-run records
