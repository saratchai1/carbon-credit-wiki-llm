# Log

## [2026-09-04] init | Mangrove Carbon Credit LLM Wiki
- Instantiated persistent LLM wiki from user-provided LLM Wiki pattern.
- Set Premium T-VER / T-VER-P-METH-13-02 v01 as default methodology.
- Added version preflight because TGO 2026 work plan lists methodology/tool revisions.
- Added core formulas, carbon pools, SOC default, uncertainty deduction, field/remote-sensing MRV rules, non-permanence/buffer separation.
- Added project data templates, source registry, core arithmetic tool and wiki lint.
- Project-specific data not yet ingested.

## [2026-09-04] persistence | Canonical GitHub repository
- Canonical durable repository set to `saratchai1/carbon-credit-wiki-llm`.
- `main` is the durable source of truth for current Wiki state.
- Future relevant project information should be integrated with provenance, index/source-registry maintenance, conflict tracking, and append-only log entries.
- Sandbox files and chat memory are not evidence of repository state.
- Repository is public; do not commit secrets or confidential raw material.

## [2026-09-04] ingest | Premium T-VER Mangrove Group 1 project package
- Ingested the user-provided Google Drive package for `Greenhouse Gas Reduction with Mangrove Reforestation in Thailand (Group 1)` into the durable wiki.
- Added `projects/group-1-mangrove-reforestation.md` as the canonical project page.
- Populated `data/project-profile.yaml` from the registered/validated project package instead of leaving it as a blank template.
- Registered project status: Premium T-VER, T-VER-P-METH-13-02 v01, 40 plots in 7 provinces, crediting period 2023-10-01 to 2038-09-30.
- Locked the accounting boundary at 1,195.64 rai; preserved 1,472.13 rai only as allocated area. Validation boundary findings MM 01/MM 02 were retained as QA history.
- Recorded project strata: former shrimp ponds 12 plots/230.92 rai; cleared/planting-ready 24/449.25; accreting mudflat 4/515.47.
- Recorded registered ex-ante estimate: tree component 168,585.24 tCO2e over 15 years; workbook SOC component 1,139.8434667 tCO2e; total 169,725.0834667 tCO2e; reported average 11,315 tCO2e/year.
- Explicitly classified the 11,315 tCO2e/year figure as `PROJECT_ESTIMATE`, not issued/certified credits; no actual Monitoring Report, Verification Report or TGO issuance evidence has been ingested.
- Recorded PDD MRV design: stratified random sampling, satellite support for stratification/canopy, tree aboveground+belowground pools, SOC included, optional sapling/deadwood excluded, uncertainty deduction requirement, and separate monitoring cadences.
- Recorded SD/Safeguards cadences: SDG 10 annual, SDG 13 growth every 5 years, SDG 14 annual satellite/ecological monitoring; kept separate from the PDD tree-carbon MRV cadence of at least every 3 years.
- Added source notes for PDD, calculation workbook, Validation Report, SD/Safeguards report, TGO certificate, and shapefile package manifest.
- Added immutable external-source manifest `raw/project-g1-drive-source-manifest-2026-09-04.md` with observed Drive file IDs/metadata.
- Added a calculator hard-stop warning `CONFLICT_REQUIRES_RECONCILIATION` for the SOC workbook implementation versus methodology/PDD wording; preserved the validated reported ex-ante value without inventing a replacement formula.
- Updated `sources/source-registry.md`, `sources/known-gaps.md`, and `index.md`.
- Shapefile ZIP binary contents/hash/CRS/feature schema were not independently inspected in this ingest; geometry equivalence must be validated before claiming a specific GIS copy is authoritative.

## [2026-09-04] ingest | Registered Standard T-VER Group 2 source bundle
- Ingested Google Drive folder `1naQZbzf1ZsbmIoI62huW04946eICuglE` as primary evidence for Standard T-VER Group 2.
- Added project-specific methodology lock: `T-VER-S-METH-13-03` v01 + `T-VER-S-TOOL-01-01` v01.
- Added project pages for baseline, project sequestration, field measurement/POM, allometry, monitoring, spatial sample plots and validation/registration evidence.
- Recorded 50 plots, 9,005.55 rai, 6 provinces and crediting period 15 Nov 2023–14 Nov 2033.
- Recorded registered ex-ante calculation: baseline 546,011.7485 tCO2eq; year-10 project value 1,392,533.4485 tCO2eq; net 846,521.70 tCO2eq; annual average 84,652.17 tCO2eq/year; certificate rounded value 84,652 tCO2eq/year.
- Recorded carbon-pool exclusions: SOC, deadwood and litter.
- Recorded project-specific field/POM rule for Rhizophora and Komiyama et al. 2005 ABG/BLG equations.
- Recorded boundary GPS monitoring every 5 years plus disease/insect and encroachment risk monitoring.
- Added source IDs for registration certificate, Validation Report, PDD copy, calculation workbook, sample-plot CSV and shapefile archive.
- Added immutable external-source manifest `raw/project-g2-drive-source-manifest-2026-09-04.md`; raw PDFs/GIS binaries/PII were not copied into the public repo.
- Conflict `C-001` resolved in favor of certificate + Validation Report + workbook: 84,652 is annual (rounded), 846,521.70 is 10-year net total.
- Conflict `C-002` remains `VERSION_IDENTITY_UNCONFIRMED`: Validation Report cites PDD v2 dated 23 Jun 2024 while Drive contains files named V2(22-8-24); no byte-level comparison performed.

## [2026-09-04] ingest | MOC1 / Siam TC Premium T-VER project package
- Ingested the user-provided Google Drive folder `18JoPb5Ci3_OrZziLyKSsNSDom4AnWe6z` as a distinct project package: `premium-tver-moc1-stc-group-1`.
- Added project page, dedicated YAML profile, 19-plot structured CSV, six source notes, source-registry entries and immutable external-source manifest.
- Recorded validated project area 554.32 rai across 19 plots / 8 provinces; allocated area 750.65 rai is kept separate.
- Recorded registered ex-ante arithmetic: tree 5,210.608 + SOC 528.4517333 = 5,739.0597333 tCO2e/year; 86,085.896 tCO2e over 15 years; certificate rounds to 5,739 tCO2e/year.
- Preserved the workbook’s 535.46-rai / 5,543.7958667-tCO2e/year / 83,156.938-tCO2e legacy calculation block as `SUPERSEDED_WITHIN_PROJECT_PACKAGE` rather than deleting it.
- Added `projects/project-identity-map.md` because an existing, separate `PROJECT-G1-*` package also uses “Group 1” wording. No supersession/merge relationship is assumed between the two project packages.
- Recorded VVB as Bureau Veritas Certification (Thailand) Ltd. with `CERTIFY_WITH_COMMENT`, and separated the 30-year maintenance context from the 15-year crediting period.
- Recorded MRV design: stratified random sampling, repeated measurement, DBH as material variable, and Komiyama reference as `REFERENCE_ONLY` pending exact equation/range verification.
- Original binaries were not mirrored into this public repository because they may contain personal/contact information; stable Drive IDs/URLs are preserved in the raw external-source manifest and source notes.
- Actual Monitoring Report, Verification Report, issuance evidence, final buffer result and inspected shapefile geometry are still missing; actual credits remain `NOT_EVIDENCED`.
