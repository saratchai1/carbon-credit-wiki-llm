# Calculation Chain

## Accounting flow

```text
Field / Remote-sensing evidence
        ↓
Biomass / SOC / emissions / leakage components
        ↓
ΔC_P,t
        ↓
ΔC_ACTUAL,t = ΔC_P,t − GHG_E,t
        ↓
ΔC_AR,t = ΔC_ACTUAL,t − ΔC_BSL,t − LK_t
        ↓
Uncertainty / conservativeness
        ↓
Net removal before buffer
        ↓
Non-permanence risk / buffer
        ↓
Potential amount after buffer
        ↓
VVB verification + TGO certification
        ↓
Certified credit
```

## Required distinction

### Carbon stock
ปริมาณคาร์บอนที่มีอยู่ ณ เวลาใดเวลาหนึ่ง.

### Carbon-stock change
ความต่างระหว่างเวลา.

### Net GHG removal
ผลหลังหัก baseline, project emissions และ leakage.

### Potential credit
ค่าประเมินที่อาจนำไปขอรับรอง.

### Certified credit
จำนวนที่ได้รับการรับรอง/issuance โดย TGO.

## Core equation

`net_before_buffer = Σ[(tree + sapling + deadwood + soc) - (burning + fuel) - baseline - leakage]`

แต่ทุก component ต้องเป็นไปตาม methodology/tool ไม่ใช่ user-defined shortcut.
