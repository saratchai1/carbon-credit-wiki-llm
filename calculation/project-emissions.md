# Project Emissions

## Main equation

`GHG_E,t = GHG_Burning,t + GHG_Fuel,t`

## Biomass burning

ต้องใช้ TGO tool ที่เกี่ยวข้องสำหรับ non-CO2 emissions จาก burning.

เก็บ event:
- date
- reason
- area
- biomass basis
- source evidence
- CH4/N2O calculation trace

## Fossil fuel

ใน methodology มีสมการรูปแบบ:

`GHG_Fuel = Σ[FC_i × (NCV_i × 10^-6) × EF_CO2,i] × 10^-3`

โดย:
- `FC_i` = fuel consumption
- `NCV_i` = net calorific value
- `EF_CO2,i` = emission factor

ต้องตรวจ unit ให้ตรงกับ source parameter.

## Small project treatment

T-VER-P-METH-13-02 ระบุว่าโครงการขนาดเล็กไม่ต้องคำนวณ fossil fuel emissions จาก project activities.

อย่า apply exemption จนกว่าจะยืนยัน project scale ตาม rule/version ที่ใช้จริง.
