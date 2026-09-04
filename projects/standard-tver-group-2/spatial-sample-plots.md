# Group 2 — Spatial Sample Plots

## Available evidence

The Google Drive source folder contains:
- `sample_plot-coordinate(10-4-67).csv`
- `Shpfile.rar`
- PDD appendices with project-boundary and sample-plot coordinates

The CSV schema observed is:

`name,x,y,order,group`

Plot-point names include site/group prefixes such as `PKH`, `PNH`, `RNH`, `SKH`, `STH` and others, with four ordered corner points for many sample plots.

## CRS hard stop

The retrieved CSV itself does **not** explicitly state the CRS/EPSG in its header. The numeric values look like projected coordinates, but the Wiki must not guess the CRS.

Before overlaying these points with drone, satellite, LiDAR or web-map data:
1. confirm CRS from the shapefile metadata, PDD or original GIS workflow;
2. record the CRS/EPSG in the derived dataset;
3. preserve the original coordinate values unchanged;
4. document any reprojection.

## Public-repository handling

The raw coordinate table and shapefile are not copied into this public repository in this ingest. The Wiki stores provenance and schema only. Retrieve the source by its Drive file ID when an authorized spatial analysis is required.

Source: [[../../sources/stc-standard-tver-group2-drive]].
