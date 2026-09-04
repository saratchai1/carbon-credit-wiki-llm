# Raw Sources

โฟลเดอร์นี้เก็บ source ที่ผู้ใช้ให้มาโดยตรง และควรใช้เป็น immutable layer.

ปัจจุบัน:
- `llm-wiki-pattern.md` — source pattern ที่ใช้กำหนดสถาปัตยกรรม

เอกสาร TGO/Verra ยังไม่ copy full document เข้ามาใน package นี้; ใช้ manifest ใน `sources/source-registry.md`.
เมื่อจะ ingest PDF จริง ให้เก็บไฟล์ต้นฉบับแบบ immutable พร้อม source ID/version/hash.
