# Non-permanence and Buffer

Premium T-VER forestry/agriculture removal projectsมีความเสี่ยงจาก:
- project management
- land ownership/tenure changes
- fire
- pest/disease
- natural disasters
- other reversal risks

## Required concept

Project participant ต้องมี:
- Non-permanence Risk Assessment Report ในช่วง registration
- Non-permanence Risk Monitoring Report สำหรับ issuance/monitoring ตาม program rules
- VVB validation/verification ตามขั้นตอน

TGO หัก buffer credits ไป pooled buffer account ตาม risk criteria.

## Wiki rule

ห้าม hard-code buffer rate เป็นค่าตายตัว.

เก็บ:
- assessment_date
- risk_report_version
- verified_by
- buffer_rate_pct
- source_id
- effective_period

ถ้าไม่มีค่า:
`buffer_rate_pct: null`

และ output:
`net_before_buffer` เท่านั้น.

## Long-term monitoring

Current Premium T-VER guidance requires ongoing non-permanence monitoring obligations; projects with crediting period shorter than 45 years may still have periodic monitoring obligations to complete the 45-year horizon under applicable rules.
