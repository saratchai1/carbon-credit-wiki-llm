# Index

## Core
- [[README]] — วิธีใช้ wiki
- [[AGENTS]] — กฎสำหรับ LLM agent
- [[architecture/wiki-architecture]] — raw/wiki/schema
- [[architecture/ingest-workflow]] — ingest/query/lint

## Projects
- [[projects/project-identity-map]] — mandatory disambiguation map because multiple project packages reuse Group 1 / Group 2 wording
- [[projects/group-1-mangrove-reforestation]] — `premium-tver-mangrove-group-1`; 40 plots / 1,195.64 rai / 11,315 tCO2e/year ex-ante
- [[projects/moc1-stc-mangrove-reforestation]] — `premium-tver-moc1-stc-group-1`; 19 plots / 554.32 rai / 5,739 tCO2e/year ex-ante
- [[projects/standard-tver-group-2/README]] — `STC-STANDARD-TVER-GROUP-2`; 50 plots / 9,005.55 rai / 84,652 tCO2eq/year ex-ante
- [[projects/standard-tver-group-2-stc-vsd/README]] — `STC-VSD-STANDARD-TVER-GROUP-2`; 22 plots / 6,775.53 rai / 63,689 tCO2eq/year ex-ante

## Standard / Methodology
- [[standards/current-standard]] — default standard and version watch
- [[standards/other-standards]] — other standards; do not mix
- [[methodologies/T-VER-P-METH-13-02]] — Premium T-VER mangrove methodology
- [[methodologies/T-VER-S-METH-13-03]] — Standard T-VER historical project locks; multiple projects, never mix parameters
- [[methodologies/eligibility-checklist]] — checklist before calculation

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
- `projects/standard-tver-group-2/project-profile.yaml` — profile for `STC-STANDARD-TVER-GROUP-2`
- `projects/standard-tver-group-2-stc-vsd/project-profile.yaml` — profile for `STC-VSD-STANDARD-TVER-GROUP-2`
- `data/tree_measurements.csv` — template
- `data/planting_cohorts.csv` — template
- `data/activity_emissions.csv` — template

## Sources
- [[sources/source-registry]]
- [[sources/known-gaps]]
- `raw/project-g1-drive-source-manifest-2026-09-04.md` — Group 1 external-source provenance
- [[sources/project-g1-pdd-2024-04-30]]
- [[sources/project-g1-calculation-workbook-2024-04-30]]
- [[sources/project-g1-validation-2024-05-01]]
- [[sources/project-g1-sdg-safeguards-2024-04-23]]
- [[sources/project-g1-certificate-2024-06-21]]
- [[sources/project-g1-shapefile-manifest-2024-06-11]]
- `raw/project-moc1-stc-drive-manifest-2024-06-14.md` — MOC1/STC external-source provenance
- [[sources/project-moc1-stc-pdd-2024-06-12]]
- [[sources/project-moc1-stc-calculation-workbook-2024-06-13]]
- [[sources/project-moc1-stc-validation-2024-06-13]]
- [[sources/project-moc1-stc-sdg-safeguards-2024-01-30]]
- [[sources/project-moc1-stc-certificate-2024-06-21]]
- [[sources/project-moc1-stc-shapefile-manifest-2024-06-14]]
- `raw/project-g2-drive-source-manifest-2026-09-04.md` — Standard T-VER Group 2 / STC provenance
- [[sources/stc-standard-tver-group2-drive]] — Standard T-VER Group 2 / STC source bundle
- `raw/project-g2-stc-vsd-drive-source-manifest-2026-09-04.md` — distinct Standard T-VER Group 2 / STC+VSD provenance
- [[sources/stc-vsd-standard-tver-group2-drive]] — Standard T-VER Group 2 / STC+VSD source bundle

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
