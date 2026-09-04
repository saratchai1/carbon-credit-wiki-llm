---
code: T-VER-P-METH-13-02
version: "01"
effective_from: 2023-03-01
authority: TGO
checked_on: 2026-09-04
---

# T-VER-P-METH-13-02 — Mangrove Afforestation/Reforestation

## Project outline

กิจกรรมเพิ่มการกักเก็บคาร์บอนจากการปลูกป่าชายเลนในพื้นที่:
- ที่ไม่เคยเป็นป่า (afforestation)
- ที่เคยเป็นป่าแต่ถูกทำลาย (reforestation)

ครอบคลุม biomass เหนือดิน/ใต้ดิน และอาจเลือกไม้ตาย/SOC ตามเงื่อนไข.

## Applicability

1. ปลูก ดูแล และจัดการป่าปลูกอย่างเหมาะสม
2. มีสิทธิใช้ประโยชน์ที่ดินตามกฎหมาย
3. baseline ก่อนโครงการต้องไม่ใช่ป่า:
   - canopy cover ของต้นไม้ที่เมื่อโตเต็มที่สูงไม่น้อยกว่า 3 m
   - เฉลี่ยน้อยกว่า 30% ของพื้นที่
4. พืชที่ปลูกและฟื้นฟูต้องเป็นชนิดพืชป่าชายเลนมากกว่า 90% ของพื้นที่โครงการ
5. ถ้าพืชชนิดอื่นเกิน 10% ต้องไม่ทำให้ hydrology ใน/นอกโครงการเปลี่ยนแปลง

## Project conditions

- รวมหลายพื้นที่เป็นโครงการเดียวได้
- ไม่มีการทำไม้ออกทั้งหมดใน 10 ปีนับจากเริ่มโครงการ
- ต้องเป็น additional activity ตามเงื่อนไข methodology/program
- soil disturbance ต้องไม่เกิน 10% ในกรณีที่ methodology ระบุ เช่น organic soils หรือพื้นที่ที่ก่อนโครงการมีการจัดการเพิ่ม SOC

## Project start date

วันที่เริ่มปลูกหรือหว่านเมล็ดในพื้นที่โครงการ  
ไม่รวมการเตรียมพื้นที่ เช่น กำจัดวัชพืช/ขุดหลุม

## Carbon pools

| Pool | Treatment |
|---|---|
| Aboveground biomass | ประเมิน |
| Belowground biomass | ประเมิน |
| Sapling | ทางเลือกใน calculation component ตาม tool |
| Dead wood | ทางเลือก |
| Litter | ไม่ประเมินใน methodology นี้ |
| Soil organic carbon | ทางเลือก |

## Project emissions

พิจารณา:
- non-CO2 จาก biomass burning
- fossil-fuel CO2 จาก machinery สำหรับโครงการขนาดใหญ่

สำหรับโครงการขนาดเล็ก methodology ระบุว่าไม่ต้องคำนวณ fossil-fuel emissions จาก project activities.

กิจกรรมที่ methodology กำหนดเป็นไม่มีนัยสำคัญ/ให้เป็นศูนย์ ได้แก่:
- ตัดพืชล้มลุกและไม้พุ่ม
- ใส่ปุ๋ย
- การย่อยสลายซากพืชและรากฝอย
- การสร้างถนนในพื้นที่โครงการและการขนส่งจากกิจกรรมโครงการ

## Baseline

`ΔC_BSL,t = ΔC_TREE_BSL,t + ΔC_SAP_BSL,t + ΔC_DW_BSL,t`

baseline carbon stock/change อาจกำหนดเป็น 0 ได้เมื่อเข้าเงื่อนไขของ tool ที่เกี่ยวข้อง.

## Actual project removal

`ΔC_ACTUAL,t = ΔC_P,t - GHG_E,t`

`ΔC_P,t = ΔC_TREE_P,t + ΔC_SAP_P,t + ΔC_DW_P,t + ΔSOC_P,t`

## Project emissions

`GHG_E,t = GHG_Burning,t + GHG_Fuel,t`

## Leakage

ถ้า project activity ทำให้เกิดการเคลื่อนย้าย/บุกรุกพื้นที่ใหม่จากกิจกรรมเกษตร ต้องคำนวณ:

`LK_t = LK_AGR,t`

โดยใช้ tool ที่เกี่ยวข้อง.

## Net anthropogenic removal

`ΔC_AR,t = ΔC_ACTUAL,t - ΔC_BSL,t - LK_t`

ช่วงหลายปี:

`ΔC_AR = Σ ΔC_AR,t`

## SOC default

เมื่อเลือก SOC:

`ΔSOC_P,t = (44/12) × Σ(A_t × dSOC_t × 1 year)`

default:
- `dSOC = 0.26 tC/rai/year`
- ตั้งแต่ปีปลูกจนถึงปีปลูก + 20 ปี
- หลังจากนั้น `dSOC = 0`
- methodology อ้างอิง IPCC 2013 Wetlands Supplement

ใช้ค่าอื่นได้เมื่อพิสูจน์ตามแหล่ง/วิธีที่ methodology อนุญาต.

## Monitoring

ต้องติดตามอย่างน้อย:
- project location
- project area
- selected carbon-pool parameters
- tree/sapling/deadwood changes ตาม tool
- SOC ถ้าเลือก
- emissions/leakage ที่เกี่ยวข้อง

Project area สามารถติดตามจาก field survey และ satellite/aerial imagery.
