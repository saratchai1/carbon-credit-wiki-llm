# Ingest / Query / Lint Workflow

## Ingest

เมื่อมี source ใหม่:
1. ตั้ง source ID เช่น `TGO-METH-13-02-V01`
2. เก็บ raw หรือ URL manifest
3. สร้าง/แก้ source registry
4. แตก claims สำคัญ:
   - effective date
   - equations
   - applicability
   - monitoring requirements
   - optional/mandatory pools
   - parameters
5. compare กับ wiki ปัจจุบัน
6. update เฉพาะ pages ที่ได้รับผล
7. append log

## Query

ทุกคำถามเชิงคำนวณ:
1. version preflight
2. project-profile preflight
3. data-quality preflight
4. compute
5. uncertainty
6. status label
7. file run

## Lint

อย่างน้อยทุกครั้งที่ ingest methodology/tool:
- `python tools/wiki_lint.py`
- ตรวจ source freshness
- ตรวจ broken links
- ตรวจสูตร/หน่วย
- ตรวจ status terms

## Git persistence workflow

1. Read latest `main` from `saratchai1/carbon-credit-wiki-llm`.
2. Integrate source; do not replace historical raw evidence.
3. Update source registry and affected wiki pages.
4. Update `index.md` if page topology changes.
5. Append `log.md`.
6. Run wiki lint/calculation tests when affected.
7. Commit to `main` unless the user explicitly requests branch/PR review.
8. Re-read committed key files/commit to verify persistence.
