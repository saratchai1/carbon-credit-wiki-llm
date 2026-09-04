# Tree Biomass and Carbon

อ้างอิงหลัก: T-VER-P-TOOL-01-02 และ T-VER-P-TOOL-01-07.

## 1. Sample plot → biomass

สำหรับแต่ละต้น:
1. ตรวจ species
2. ตรวจ measurement point
3. วัด DBH และ/หรือ height ตาม allometry
4. ใช้ allometric equation ที่ผ่าน applicability
5. คำนวณ ABG
6. คำนวณ BLG ด้วย root allometry หรือ root:shoot ratio ที่ยอมรับ

ในป่าชายเลน belowground biomass ตาม tool รวมรากที่อยู่ใต้ดินและรากเหนือผิวดินในความหมายที่เกี่ยวข้อง.

## 2. Plot biomass

`b_TREE,p,i = (b_ABG,p,i + b_BLG,p,i) / plot_area_rai`

หน่วย: ton dry weight / rai

## 3. Stratum mean

`b_TREE,i = mean(b_TREE,p,i)`

## 4. Project mean

`b_TREE = Σ(W_i × b_TREE,i)`

`W_i = A_i / A`

## 5. Total biomass

`B_TREE = A × b_TREE`

## 6. Convert biomass to CO2-equivalent carbon stock

`C_TREE = (44/12) × CF_TREE × B_TREE`

- `CF_TREE`: tC / t dry weight
- `B_TREE`: t dry weight
- result: tCO2e

**CF_TREE ห้ามเดา**. ต้องมาจาก source ที่ tool ยอมรับ.

## 7. Change from repeated measurement

`ΔC_TREE = (44/12) × CF_TREE × ΔB_TREE`

`ΔB_TREE = A × Δb_TREE`

`Δb_TREE = Σ(W_i × Δb_TREE,i)`

เหมาะเมื่อ remeasure plots เดิมและ structure ยังสัมพันธ์กัน.

## 8. Difference of two independent stock estimates

`ΔC_TREE = C_TREE,t2 - C_TREE,t1`

ใช้ uncertainty propagation ตาม T-VER-P-TOOL-01-02.

## 9. Definitions

### Tree
ใน T-VER-P-TOOL-01-02:
- woody perennial
- height > 1.30 m
- diameter at 1.30 m ≥ 4.50 cm
- ยกเว้น shrub

### Sapling
- height > 1.30 m
- diameter at 1.30 m < 4.50 cm

## 10. Rhizophora measurement point

สำหรับ `Rhizophora spp.` ตาม T-VER-P-TOOL-01-07:
- วัด diameter ที่ 30 cm เหนือรากค้ำจุนบนสุด
- หรือทำตาม measurement condition ของ allometric equation ที่เลือก

เก็บ field:
`measurement_point_method = RHIZOPHORA_30CM_ABOVE_HIGHEST_PROP_ROOT`

## 11. Allometry selection

สำหรับ ex-post ไม่ควรเลือกสมการเพียงเพราะเป็นสมการ mangrove ที่มีชื่อเสียง.

Tool กำหนดหลักเรื่อง:
- species/group fit
- environmental similarity
- national inventory / established commercial use / sufficient samples & R²
- หรือทำ demonstration/validation ตาม tool

ทุกสมการต้องอยู่ใน `data/allometry-registry.yaml`.
