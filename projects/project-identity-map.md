# Project Identity Map

The wiki contains multiple project packages that reuse “Group 1” or “Group 2” wording. A group number alone is therefore **not a safe project identifier**.

## Premium T-VER — two distinct “Group 1” packages

| Field | `premium-tver-mangrove-group-1` | `premium-tver-moc1-stc-group-1` |
|---|---|---|
| Project page | [[group-1-mangrove-reforestation]] | [[moc1-stc-mangrove-reforestation]] |
| Thai title | โครงการปลูกป่าชายเลนช่วยโลกลดก๊าซเรือนกระจกในประเทศไทย (กลุ่ม 1) | โครงการฟื้นฟูป่าชายเลน เพื่อระบบนิเวศที่ยั่งยืนของประเทศไทย (กลุ่ม 1) |
| Source prefix | `PROJECT-G1-*` | `PROJECT-MOC1-STC-*` |
| Co-developers | Siam TC + Wisut Consultant | Siam TC |
| VVB in ingested validation | VGreen KU Co., Ltd. | Bureau Veritas Certification (Thailand) Ltd. |
| Plots | 40 | 19 |
| Validated/project area | 1,195.64 rai | 554.32 rai |
| Registered ex-ante average | 11,315 tCO2e/year | 5,739 tCO2e/year |
| Crediting period | 2023-10-01 to 2038-09-30 | 2023-10-01 to 2038-09-30 |
| Certificate date in source package | 2024-06-21 | 2024-06-21 |
| Project profile | `data/project-profile.yaml` | `data/project-profile-moc1-stc.yaml` |

## Standard T-VER — two distinct “Group 2” packages

| Field | `STC-STANDARD-TVER-GROUP-2` | `STC-VSD-STANDARD-TVER-GROUP-2` |
|---|---|---|
| Project page | [[standard-tver-group-2/README]] | [[standard-tver-group-2-stc-vsd/README]] |
| Thai title | โครงการฟื้นฟูป่าชายเลนเพื่อระบบนิเวศที่ยั่งยืนของประเทศไทย (กลุ่ม 2) | โครงการปลูกป่าชายเลนช่วยโลกลดก๊าซเรือนกระจกในประเทศไทย (กลุ่ม 2) |
| Drive folder | `1naQZbzf1ZsbmIoI62huW04946eICuglE` | `1Wj-tjfkkmgYdiCbJnA7CoXwjgMqHJbGg` |
| Co-developers | Siam TC | Siam TC + Visut Consultant |
| VVB in ingested validation | Bureau Veritas Certification (Thailand) Ltd. | VGreen KU |
| Plots | 50 | 22 |
| Project area | 9,005.55 rai | 6,775.53 rai |
| Registered ex-ante average | 84,652 tCO2eq/year | 63,689 tCO2eq/year |
| Crediting period | 2023-11-15 to 2033-11-14 | 2024-05-31 to 2034-05-30 |
| Project profile | `projects/standard-tver-group-2/project-profile.yaml` | `projects/standard-tver-group-2-stc-vsd/project-profile.yaml` |

## Mandatory disambiguation rule

Before using any project-specific number, resolve identity using at least one strong identifier:
1. exact Thai/English project title,
2. project/source ID prefix,
3. source folder or document ID,
4. plot ID + province/boundary,
5. VVB/project-party combination,
6. explicit project-profile path.

Never merge plot lists, boundaries, calculations, source notes, methodology assumptions or VVB findings across projects merely because they share the same group number or methodology code. No supersession relationship is assumed unless a source explicitly establishes one.
