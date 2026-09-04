# AGENTS.md — Mangrove Carbon Credit Wiki Contract

## 0. Canonical Git repository

Canonical repository: `saratchai1/carbon-credit-wiki-llm`  
Canonical branch: `main`

กฎถาวร:
- ก่อนตอบหรือแก้ Wiki ที่อาศัยสถานะล่าสุด ให้ sync/read `main` ล่าสุดก่อน
- เมื่อผู้ใช้ให้ข้อมูล Carbon-credit ที่มีคุณค่าถาวร ให้ ingest เข้า repository นี้ ไม่เก็บไว้แค่ chat/sandbox
- ทุกการ ingest ต้อง update relevant pages + `index.md` เมื่อโครงสร้างเปลี่ยน + `sources/source-registry.md` เมื่อมี source + `log.md`
- Raw source เป็น immutable; ถ้า source เปลี่ยน version ให้เพิ่ม version/source ID ใหม่และเชื่อม supersession
- ห้ามใช้ chat memory เป็นหลักฐานแทน repository/source file
- ถ้ามี concurrent change ให้ re-read latest `main` และ integrate; ห้าม force-overwrite โดยไม่ตรวจ diff
- Wiki maintenance ปกติ commit ลง `main` ได้โดยตรงใน repository เฉพาะนี้ เว้นแต่ผู้ใช้สั่งให้ใช้ branch/PR
- commit message แนะนำ: `wiki: ingest <source/topic>`, `wiki: update <topic>`, `calc: add <run-id>`, `maintenance: lint/index`
- Repository นี้เป็น public: ห้าม commit secrets, credentials, personal identifiers หรือ confidential raw sources

## 1. Mission

เป้าหมายคือทำให้คำถามเช่น:

- “แปลงนี้คาดว่าจะได้กี่ tCO2e?”
- “ข้อมูลที่มีพอขอเครดิตหรือยัง?”
- “ปีนี้เพิ่มขึ้นจากรอบก่อนเท่าไร?”
- “โดรน/LiDAR ใช้แทน field DBH ได้แค่ไหน?”
- “ตัวเลขนี้เป็น carbon stock, removal หรือ credit?”

ตอบได้แบบ **ตรวจสอบย้อนกลับได้, ไม่แต่งตัวเลข, ไม่ปะปนมาตรฐาน และรักษาหลักอนุรักษ์นิยม**

## 2. Source hierarchy

ใช้ลำดับความน่าเชื่อถือดังนี้:

1. **Current official TGO rules / methodology / tools / forms**
2. **Registered project PDD / validated methodology choice / verified Monitoring Report**
3. **Project primary evidence** เช่น GIS, field measurements, fuel logs, planting records
4. **Peer-reviewed research** ที่เข้าเงื่อนไขของ methodology/tool
5. **Derived model output** เช่น drone AI, satellite index, LiDAR-derived DBH
6. **LLM inference**

ห้ามยกระดับชั้น 5–6 ให้เป็นข้อเท็จจริงชั้น 1–3 โดยไม่มีหลักฐานรองรับ

## 3. Mandatory preflight before a calculation

ก่อนคำนวณทุกครั้ง:

1. ตรวจ methodology code/version ที่ project ใช้
2. ตรวจว่า version ยัง valid/current ตาม TGO
3. ถ้า TGO ออก version ใหม่หรืออยู่ใน transition:
   - หยุดการคำนวณแบบ `CERTIFIABLE`
   - ingest source ใหม่
   - update `standards/current-standard.md`
   - บันทึกผลใน `log.md`
4. ตรวจ project boundary และ area
5. ตรวจ baseline
6. ตรวจ selected carbon pools
7. ตรวจ monitoring period
8. ตรวจ allometric equation / biomass model ที่อนุญาต
9. ตรวจ uncertainty
10. ตรวจ project emissions และ leakage
11. ตรวจ non-permanence/buffer status

## 4. Output status vocabulary

ทุกคำตอบเชิงตัวเลขต้องมีสถานะหนึ่งในนี้:

- `SCREENING_ESTIMATE` — ค่าคัดกรอง/ประมาณเบื้องต้น
- `PROJECT_ESTIMATE` — ใช้ข้อมูลโครงการจริง แต่ยังไม่ผ่าน verification
- `VERIFICATION_READY_ESTIMATE` — calculation trace และ evidence ครบตามที่ wiki ตรวจได้ แต่ยังไม่ใช่เครดิตรับรอง
- `VERIFIED_RESULT` — มี Verification Report รองรับ
- `CERTIFIED_CREDIT` — ใช้คำนี้ได้เมื่อมี TGO issuance/certification evidence
- `NOT_CALCULABLE` — ข้อมูลไม่พอหรือ methodology status ไม่ชัด

ห้ามใช้ `CERTIFIED_CREDIT` จากการคำนวณของ LLM เพียงอย่างเดียว

## 5. Core accounting identities

สำหรับ T-VER-P-METH-13-02:

`ΔC_ACTUAL,t = ΔC_P,t - GHG_E,t`

`ΔC_P,t = ΔC_TREE_P,t + ΔC_SAP_P,t + ΔC_DW_P,t + ΔSOC_P,t`

`GHG_E,t = GHG_Burning,t + GHG_Fuel,t`

`ΔC_AR,t = ΔC_ACTUAL,t - ΔC_BSL,t - LK_t`

ผลรวมช่วง monitoring period:

`ΔC_AR = Σ ΔC_AR,t`

**อย่าข้ามขั้น** จาก tree biomass ไปเป็น carbon credit โดยตรง

## 6. Carbon-stock rules

Tree carbon stock:

`C_TREE = (44/12) × CF_TREE × B_TREE`

`B_TREE = A × b_TREE`

เมื่อแบ่งชั้นภูมิ:

`b_TREE = Σ(W_i × b_TREE,i)`

สำหรับการวัดซ้ำแปลงเดิม:

`ΔC_TREE = (44/12) × CF_TREE × ΔB_TREE`

ใช้ uncertainty และ conservative deduction ตาม `calculation/uncertainty.md`

## 7. SOC rule

SOC เป็น **optional pool** ใน T-VER-P-METH-13-02.

Default ที่ methodology ระบุ:

- `dSOC = 0.26 tC/rai/year`
- ใช้ตั้งแต่ปีปลูกจนถึงปีปลูก + 20 ปี
- หลังจากนั้น default = 0
- แปลง C → CO2 ด้วย `44/12`

ห้ามเปิด SOC โดยอัตโนมัติ. ต้องมี `soc_included: true` ใน project profile.

## 8. Allometry rule

ห้าม LLM เลือกสมการ allometric เพราะ “นิยมใช้” อย่างเดียว.

ต้องมี:
- `allometry_id`
- species/group applicability
- source
- parameter range
- ex-ante / ex-post suitability
- approval/justification status

ถ้าค่าต้นไม้หลุดช่วงที่สมการรองรับ ให้ flag `OUT_OF_DOMAIN`.

## 9. Mangrove DBH measurement

ทั่วไป DBH = 1.30 m จากพื้นดิน หรือทำตามเงื่อนไขของสมการที่เลือก.

สำหรับ `Rhizophora spp.` ตาม T-VER-P-TOOL-01-07:
- วัดที่ **30 cm เหนือรากค้ำจุนบนสุด**
- หรือใช้จุดวัดตามเงื่อนไขสมการ allometry ที่ได้รับเลือก

เก็บ `measurement_point_method` ทุกต้น.

## 10. Remote sensing / AI / LiDAR

อนุญาตให้ใช้เพื่อ:
- project area
- stratification
- crown cover
- change detection
- sampling support
- secondary variable ใน double sampling
- QA/QC

ห้ามแปลง:
`tree_count → tCO2e`
หรือ
`NDVI/canopy → tCO2e`
โดยตรง เว้นแต่มี model/calibration/approval ที่ methodology รองรับและมี uncertainty trace.

AI output ต้องเก็บ:
- model/version
- date
- source imagery
- ground-truth set
- error metrics
- calibration status
- QA reviewer

## 11. Buffer and non-permanence

`ΔC_AR` ไม่เท่ากับ “เครดิตที่ project ถือใช้ได้” เสมอไป.

Premium T-VER removal projects ต้องมี non-permanence risk assessment/monitoring และ TGO จะกัน buffer credits ตามเกณฑ์ที่เกี่ยวข้อง.

ห้ามเดา buffer rate. ถ้าไม่มี rate ที่อ้างอิงได้:
- รายงาน `net_before_buffer`
- ตั้ง `buffer_rate = UNKNOWN`
- อย่าคำนวณ `estimated_after_buffer`

## 12. Ingest operation

เมื่อ source ใหม่เข้ามา:
1. เก็บ raw แบบ immutable
2. สร้าง source note
3. update page ที่ได้รับผล
4. update `sources/source-registry.md`
5. update `index.md`
6. append `log.md`
7. ถ้า source ขัดกับของเดิม ให้ mark `SUPERSEDED` / `CONFLICT`
8. ห้ามลบ historical claim โดยไม่บันทึกเหตุผล

## 13. Query operation

เมื่อถูกถาม:
1. อ่าน `index.md`
2. อ่าน pages ที่เกี่ยวข้อง
3. อ่าน project profile
4. อ่าน latest calculation run ถ้าเป็น follow-up
5. ตอบพร้อม:
   - status
   - methodology/version
   - period
   - formula trace
   - inputs
   - outputs
   - uncertainty
   - exclusions
   - missing evidence
6. ถ้าคำตอบมีคุณค่าในระยะยาว ให้ file กลับเข้า wiki

## 14. Lint operation

ตรวจอย่างน้อย:
- broken internal links
- orphan pages
- methodology-version drift
- stale sources
- conflicting units
- missing source IDs
- calculations without run IDs
- undocumented assumptions
- `CERTIFIED_CREDIT` claims without issuance evidence
- numeric values with no units

## 15. Hard stops

ตอบ `NOT_CALCULABLE` เมื่อ:
- project boundary ไม่ชัด
- methodology/version ไม่ชัด
- units ไม่ชัด
- allometry ไม่มีแหล่งอ้างอิง
- baseline ไม่พอ
- monitoring dates ไม่พอสำหรับ change calculation
- source conflict กระทบผลลัพธ์และยัง resolve ไม่ได้
