# Field Measurement

## Minimum per tree

- project_id
- stratum_id
- sample_plot_id
- tree_id
- species_scientific
- species_thai
- measurement_date
- DBH_cm / diameter_cm
- height_m ถ้าสมการต้องใช้
- measurement_point_method
- allometry_id
- QA status
- recorder
- coordinate ถ้ามี

## Rhizophora

ใช้ measurement point ที่ 30 cm เหนือ highest prop root ตาม T-VER-P-TOOL-01-07 หรือเงื่อนไขของสมการที่เลือก.

### Registered Standard T-VER precedent

The validated 2024 STC+VSD Standard T-VER Group 2 PDD independently states the same operational pattern: when Rhizophora prop roots are above the normal 1.30 m DBH point, measure diameter **30 cm above the prop-root point**.

This is project precedent, not authority to ignore the methodology/tool/allometry selected by another project.

## Plot

เก็บ:
- plot geometry
- plot area rai
- permanent/repeated plot flag
- stratum
- establishment method
- photos
- field form source

### STC+VSD registered-project plot precedent

The PDD describes sample plots of:
- `40 × 40 m` = 1 rai;
- `20 × 40 m` = 0.5 rai.

Recorded tree information includes tree count, species, tree tag, GBH and DBH. The calculation workbook stores individual-tree species/DBH/wood-density/biomass/carbon fields.

## QA

อย่างน้อย:
- impossible DBH
- duplicate tree_id
- wrong species/allometry mapping
- missing measurement point
- DBH outside allometry domain
- inconsistent unit
- t1/t2 plot mismatch

Validation-derived additions from STC+VSD Group 2:
- tree tag ↔ species must reconcile with field evidence;
- species ↔ allometry must reconcile with actual field presence;
- sample-plot area and coordinates must reconcile across GIS/PDD/workbook;
- any boundary revision requires recalculation of dependent project totals.
