# ===== ขั้นที่ 3: วนลูปสแกนหลายเครื่อง + จับเวลา =====

import subprocess                       # เครื่องมือสั่งรันคำสั่ง ping
import time                             # เครื่องมือจับเวลา


def is_online(target):                  # ฟังก์ชันเช็คว่าเครื่องเปิดอยู่ไหม
    # ping 1 ครั้ง รอไม่เกิน 500 มิลลิวินาที (-w 500) จะได้ไม่ต้องรอนานถ้าเครื่องไม่มีอยู่
    result = subprocess.run(["ping", "-n", "1", "-w", "500", target], capture_output=True, text=True)
    #print(result.stdout)               # (ปิดไว้) ใช้ส่องดูผลลัพธ์ ping ตอนทดลอง
    if "TTL" in result.stdout:          # มีคำว่า TTL = เครื่องตอบกลับ
        return True                     # ตอบว่าเปิดอยู่
    else:                               # ไม่มี
        return False                    # ตอบว่าปิดอยู่

prefix = "192.168.1."                   # ส่วนหน้าของ IP เดี๋ยวเอาเลขท้ายมาต่อ

start_time = time.time()                # จดเวลาตอนเริ่ม

for i in range(1, 6):                   # วนเลข 1 ถึง 5 (ลองแค่ 5 เครื่องก่อน)
    target = f"{prefix}{i}"             # ต่อเป็น IP เต็ม เช่น "192.168.1.3"
    print(f"Scanning {target}...")      # บอกว่ากำลังสแกนเครื่องไหน
    if is_online(target):               # ถ้าเครื่องเปิดอยู่
        print(f"{target} is online.")   # แสดงว่าออนไลน์
    else:                               # ถ้าไม่เปิด
        print(f"{target} is offline.")  # แสดงว่าออฟไลน์

end_time =time.time()                   # จดเวลาตอนจบ

print(f"scan finished in {round(end_time - start_time, 2)} seconds")   # แสดงว่าใช้เวลาไปกี่วินาที (ทศนิยม 2 ตำแหน่ง)
