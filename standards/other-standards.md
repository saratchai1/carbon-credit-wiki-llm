# Other Standards

## Verra VM0033

Verra มี `VM0033 Methodology for Tidal Wetland and Seagrass Restoration v2.1` ซึ่งครอบคลุม tidal wetland restoration และสามารถเกิด removals จาก biomass และ soil organic carbon.

**ห้ามนำสมการ/เงื่อนไขของ VM0033 มารวมกับ Premium T-VER โดยอัตโนมัติ.**

ถ้าจะเปลี่ยน standard:
1. สร้าง `standards/verra-vm0033/`
2. ingest methodology/modules/tools ทั้งชุด
3. สร้าง calculation chain แยก
4. ห้าม reuse buffer/additionality/leakage rules จาก T-VER โดยไม่มี mapping ที่ตรวจสอบแล้ว
