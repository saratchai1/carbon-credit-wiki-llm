# Immutable External Source Manifest — Group 1 Drive Package

Ingest date: 2026-09-04  
External folder: https://drive.google.com/drive/folders/1awaITaYergWM0l2_Yn4_mWu3tsB9Omc4

Purpose: immutable provenance snapshot of the externally stored source package used for the first Group 1 project ingest. This file records observed metadata and URLs; it does not claim that binary contents have been copied into GitHub.

## Observed files

| Drive file ID | Title | MIME / role | Observed modified time | Notes |
|---|---|---|---|---|
| `1BThFVV48V1fqh3Q-j4mo_q7qBn9spt_S` | Premium T-VER Cer 3 2567-3 VSD&STC กลุ่ม 1.pdf | PDF / registration certificate | 2024-08-26T11:11:05Z | TGO certificate text extracted through Drive connector |
| `1BljOhXs0lrQ25KC_P3g9EJqbc5VEBtet` | 003 T-VER-P-F006-SDG-VSD-MOC1-23-04-24.pdf | PDF / SD & Safeguards | 2024-08-26T10:29:47Z | Text extracted through Drive connector |
| `1M7fWvmuZoAng7wf_STzsNnc1pYNeRXZL` | T-VER-P-F003-PDD Ver 02-MOC1-VSD-30-04-2024.pdf | PDF / PDD | 2024-06-14T04:27:01Z | Text extracted through Drive connector; validation report identifies reviewed project revision 06 dated 2024-04-30 |
| `1Gn7Sych0MNkSMJ4UY0dTmpoLbNXASRPL` | T-VER-P-F003-PDD Ver 02-MOC1-VSD-30-04-2024.docx | DOCX / PDD companion | 2024-06-14T04:26:21Z | Listed in folder; not separately used as primary extraction source in this ingest |
| `1WmnpkUJooPTS55p9yQmL8CgIwAiIUBoA` | รายงานการตรวจสอบความใช้ได้ กลุ่ม 1 แก้ไข.pdf | PDF / Validation Report | 2024-06-14T03:07:47Z | Text extracted through Drive connector |
| `1bt6v-8fvTcf2vbX7FV1dSI5WgmnNbwLr` | Shapefile.zip | ZIP / GIS package | 2024-06-11T09:41:55Z | Drive-reported size 3,595,907 bytes; binary contents/hash/CRS not inspected in this ingest |
| `1hFdcZ_7cNkb4RQ4leCQCUuQYOPQvuCt1` | VSD_MOC1-30-04-24.xlsx | XLSX / carbon calculation workbook | 2024-06-06T09:23:16Z | Structured workbook content extracted through Drive connector |
| `1wTq5Q0Vsa0OWKbqIn2X9EMhrXlgT8XXX` | หนังสือรับรอง STC & VSD.pdf | PDF / supporting certificate | 2024-04-24T06:14:05Z | Connector returned no extractable text in this ingest; no substantive claims were derived from it |

## Derived source notes created from this package

- `sources/project-g1-pdd-2024-04-30.md`
- `sources/project-g1-calculation-workbook-2024-04-30.md`
- `sources/project-g1-validation-2024-05-01.md`
- `sources/project-g1-sdg-safeguards-2024-04-23.md`
- `sources/project-g1-certificate-2024-06-21.md`
- `sources/project-g1-shapefile-manifest-2024-06-11.md`

## Integrity rule

If any external file is replaced or materially changed, do not overwrite this manifest. Add a new dated manifest/source ID and explicitly record supersession/conflict in `sources/source-registry.md` and `log.md`.
