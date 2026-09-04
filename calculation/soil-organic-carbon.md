# Soil Organic Carbon (SOC)

SOC เป็น optional carbon pool ใน T-VER-P-METH-13-02.

## Default equation

`ΔSOC_P,t = (44/12) × Σ(A_cohort × dSOC × duration_year)`

สำหรับ default methodology:
- `dSOC = 0.26 tC/rai/year`
- เริ่มจากปีปลูก
- ใช้ถึงปีปลูก + 20 ปี
- หลัง 20 ปี default `dSOC = 0`

ที่มาของ default ใน methodology: IPCC 2013 Wetlands Supplement (1.62 tC/ha/year ≈ 0.26 tC/rai/year).

## Cohort logic

ถ้าปลูกต่างปีกัน ต้องคิดเป็น cohort:
- cohort A: 2025, 40 rai
- cohort B: 2026, 60 rai

ในแต่ละ monitoring year ให้คิด SOC เฉพาะ cohort ที่อายุไม่เกิน 20 ปี.

## Do not

- ห้ามรวม SOC ถ้า PDD/project configuration ไม่เลือก pool นี้
- ห้ามนับ SOC ซ้ำจากทั้ง default และ field-measured rate
- ห้ามใช้ default เกิน 20 ปีโดยอัตโนมัติ
