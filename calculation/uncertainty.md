# Uncertainty and Conservative Deduction

อ้างอิง T-VER-P-TOOL-01-02 Version 01.

## Uncertainty

ใช้ confidence level 90% ตาม tool สำหรับ sampling uncertainty.

ตัวอย่างหลักการ:

`U = (error_at_90pct_confidence / mean) × 100`

ถ้า `U <= 10%` ไม่มี uncertainty deduction.

## Deduction table

| U | Deduction factor applied to uncertainty amount |
|---:|---:|
| U ≤ 10% | 0% |
| 10% < U ≤ 15% | 25% |
| 15% < U ≤ 20% | 50% |
| 20% < U ≤ 30% | 75% |
| U > 30% | 100% |

## Conservative adjustment

ให้:
- `mean` = parameter estimate
- `error_amount` = magnitude of uncertainty around mean
- `d` = deduction factor จากตาราง

`discount = d × error_amount`

สำหรับ project estimate:
`adjusted_project = mean - discount`

สำหรับ baseline:
`adjusted_baseline = mean + discount`

หลักคือทำให้ net credit ไม่ถูก overestimate.

## Important

อย่าสับสน:
- deduction factor = % ของ **uncertainty amount**
- ไม่ใช่ % ของ mean โดยตรง

ทุก calculation run ต้องเก็บ:
- sample size
- degrees of freedom
- t-value
- mean
- variance/SD
- 90% confidence error
- U%
- deduction factor
- adjusted value
