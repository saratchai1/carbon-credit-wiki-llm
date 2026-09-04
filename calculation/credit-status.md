# Credit Status

## SCREENING_ESTIMATE
ใช้ default/assumption เพื่อดู feasibility. ไม่ควรใช้ใน proposal ที่อ้างว่าเป็นเครดิตจริง.

## PROJECT_ESTIMATE
ใช้ primary project data แต่ยังไม่ผ่าน VVB.

## VERIFICATION_READY_ESTIMATE
wiki ตรวจว่า:
- formula trace ครบ
- source trace ครบ
- methodology version lock
- uncertainty complete
- required evidence present

แต่ยังไม่ใช่ verified/certified.

## VERIFIED_RESULT
มี VVB Verification Report รองรับ.

## CERTIFIED_CREDIT
ใช้ได้เมื่อมี TGO certification/issuance evidence.

## Buffer

รายงานอย่างน้อย 2 ค่าเมื่อมี buffer rate:
- `net_before_buffer`
- `estimated_after_buffer`

ห้ามเรียกค่า after-buffer ว่า certified จนมี issuance.
