# Wiki Architecture

โครงสร้างนี้ดัดแปลงจากแนวคิด LLM Wiki ที่ผู้ใช้ให้มา: แยก **raw sources**, **LLM-generated wiki**, และ **schema/agent contract** เพื่อให้ความรู้สะสมและบำรุงรักษาได้ ไม่ต้องค้นและสังเคราะห์ใหม่ทั้งหมดทุกคำถาม.

## Layers

### 1) Raw
- เอกสารต้นฉบับ
- ห้ามแก้ไข
- ถ้า download/replace source ให้เพิ่ม source ใหม่ ไม่เขียนทับโดยไม่ log

### 2) Wiki
- markdown ที่ LLM สร้าง
- สรุปสูตร, definitions, decisions, data gaps, status
- cross-link ระหว่างหัวข้อ

### 3) Schema
- `AGENTS.md`
- กำหนด conventions, source hierarchy, calculation status, ingest/query/lint

## Why this matters for carbon credit

การคำนวณคาร์บอนเครดิตมี versioned methodology, project-specific PDD, monitoring data, uncertainty, validation/verification และ issuance status. ถ้าใช้ RAG อย่างเดียว LLM อาจหยิบ version เก่า/ใหม่ปนกัน. Persistent wiki จึงต้องเก็บ **version, date, applicability, supersession และ source provenance** เป็นส่วนหนึ่งของความรู้.
