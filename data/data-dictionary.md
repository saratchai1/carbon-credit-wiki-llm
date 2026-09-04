# Data Dictionary

## Project

| Field | Unit/type | Required |
|---|---|---|
| project_id | text | yes |
| standard | text | yes |
| methodology_code | text | yes |
| methodology_version | text | yes |
| project_start_date | date | yes |
| project_area_rai | rai | yes |
| boundary_file | path/id | yes |
| land_rights_evidence | source id | yes |
| baseline_evidence | source id(s) | yes |
| soc_included | bool | yes |
| deadwood_included | bool | yes |

## Stratum

| Field | Unit/type |
|---|---|
| stratum_id | text |
| area_rai | rai |
| basis | vegetation / crown cover / planting plan / disturbance |
| geometry | GIS reference |

## Tree measurement

| Field | Unit/type |
|---|---|
| monitoring_round | text |
| date | date |
| sample_plot_id | text |
| tree_id | text |
| species_scientific | text |
| diameter_cm | cm |
| height_m | m/null |
| measurement_point_method | enum |
| allometry_id | text |
| abg_kg_dry | kg |
| blg_kg_dry | kg |
| qa_status | enum |

## Planting cohort

| Field | Unit/type |
|---|---|
| cohort_id | text |
| planting_year | year |
| area_rai | rai |
| species_mix | text |
| soc_rate_tC_rai_yr | tC/rai/year |

## Activity emissions

| Field | Unit/type |
|---|---|
| date | date |
| category | burning/fuel |
| fuel_type | text/null |
| quantity | numeric |
| unit | text |
| ncv | MJ/unit |
| ef_co2 | kgCO2/TJ |
| source_id | text |

## Risk

| Field | Unit/type |
|---|---|
| assessment_date | date |
| report_id | source |
| buffer_rate_pct | %/null |
| verified | bool |
