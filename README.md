# Mangrove Carbon Credit LLM Wiki

Persistent LLM-maintained wiki สำหรับ **การประเมินและคำนวณคาร์บอนเครดิตของโครงการปลูกป่าชายเลน** โดยตั้งค่าเริ่มต้นให้สอดคล้องกับ **Premium T-VER — T-VER-P-METH-13-02: Afforestation/Reforestation of degraded mangrove habitats**.


> **Canonical repository:** `https://github.com/saratchai1/carbon-credit-wiki-llm`  
> Git `main` ของ repository นี้คือ durable source of truth ของ Wiki; ไฟล์ใน sandbox และ chat memory ไม่ใช่หลักฐานถาวรของสถานะ Wiki.

> สถานะความรู้ในชุดนี้: ตรวจสอบแหล่งทางการถึง 2026-09-04  
> Wiki นี้เป็น calculation/MRV knowledge base ไม่ใช่ใบรับรองเครดิต และไม่แทนการ Validation/Verification โดย VVB หรือการรับรองของ TGO

## หลักสำคัญ

1. **Raw source คือ source of truth** — ห้าม LLM แก้ต้นฉบับ
2. **Wiki คือความรู้ที่ compile แล้ว** — LLM เป็นผู้ดูแล สรุป เชื่อมโยง และปรับให้ทันสมัย
3. **ทุกการคำนวณต้อง trace ได้** — ทุก input ต้องมีหน่วย แหล่งที่มา วันที่ และสถานะ QA
4. **ห้ามเดาค่าที่ขาด** — ถ้าข้อมูลไม่พอ ให้ตอบ `NOT_CALCULABLE` พร้อมรายการข้อมูลที่ต้องเพิ่ม
5. **ห้ามเรียกค่าประเมินว่า certified carbon credit** จนกว่าจะมีหลักฐานการ issuance จาก TGO
6. **ก่อนทุก certified-grade run ต้องตรวจ version ระเบียบวิธีล่าสุดจาก TGO**

## Quick start สำหรับ LLM Agent

1. อ่าน `AGENTS.md`
2. อ่าน `index.md`
3. ตรวจ `standards/current-standard.md`
4. สร้าง/อัปเดต `data/project-profile.yaml`
5. ตรวจ checklist ที่ `methodologies/T-VER-P-METH-13-02.md`
6. คำนวณตาม `calculation/calculation-chain.md`
7. บันทึก calculation trace ตาม `templates/calculation-run.md`
8. append `log.md`
9. ถ้ามี source ใหม่ ให้ ingest ตาม `architecture/ingest-workflow.md`

## ผลลัพธ์ที่ Wiki รองรับ

- Project eligibility / methodology fit
- Baseline
- Tree & sapling biomass/carbon
- Optional dead wood
- Optional soil organic carbon (SOC)
- Project emissions
- Leakage
- Uncertainty deduction
- Net anthropogenic removals
- Buffer-credit handling (เมื่อมี risk-derived buffer rate)
- MRV evidence mapping ระหว่าง field / drone / satellite / LiDAR
- Data gaps และ audit trail

## ขอบเขต

เวอร์ชันแรกนี้ **เน้น Premium T-VER ของประเทศไทย**. มาตรฐานอื่น เช่น Verra VM0033 ถูกแยกไว้เป็น reference และห้ามนำสมการข้ามมาตรฐานมาปะปนโดยอัตโนมัติ.
