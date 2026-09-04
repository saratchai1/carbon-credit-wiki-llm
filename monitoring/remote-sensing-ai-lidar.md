# Remote Sensing, AI and LiDAR

## Allowed/strong use cases

### Satellite
- project boundary/area
- baseline historical evidence
- crown cover
- stratification
- disturbance/change detection
- monitoring support

### Drone
- high-resolution canopy
- planting/survival support
- tree-location inventory
- sample-plot targeting
- QA evidence

### LiDAR / point cloud
- tree structure
- height
- candidate stem/DBH proxy
- sample allocation
- monitoring consistency

## TGO tool compatibility

T-VER-P-TOOL-01-02 explicitly allows satellite/aerial imagery for area-related monitoring and gives remote-sensing-derived variables (e.g. NDVI) as an example of a secondary variable in double sampling when correlation/calibration are adequate.

TGO also publishes reference guidance on remote sensing + AI for forestry/agriculture carbon assessment.

## Hard rule

Remote sensing is **not automatically a carbon-credit calculator**.

Do not do:

`detected_trees × average_CO2_per_tree = carbon credit`

unless the average/model is methodology-valid, calibrated, uncertainty-controlled, and appropriate to monitoring period.

## Model evidence packet

ทุก model ที่ส่งผลต่อ carbon:
- model_name/version
- source data
- acquisition date
- spatial resolution
- preprocessing
- training/validation dataset
- field calibration IDs
- accuracy/error metrics
- bias check
- uncertainty
- out-of-domain rules
- reviewer
- approval status

## Preferred architecture

Remote sensing → stratification / secondary variable / QA  
Field measurements → primary biomass calibration  
Statistical model → project estimate  
T-VER uncertainty → conservative result
