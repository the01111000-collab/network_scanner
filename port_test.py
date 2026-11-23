# ===== ทดลองเช็ค port ของเครื่องเดียว =====
# port เปรียบเหมือน "ประตู" ของเครื่อง แต่ละประตูมีบริการต่างกัน

import socket                           # เครื่องมือเชื่อมต่อเครือข่าย ใช้เคาะประตู port
import time                             # เครื่องมือจับเวลา

start_time = time.time()                # จดเวลาตอนเริ่ม

ports = [22, 53, 80, 443, 3389]         # port ที่จะเช็ค: 22=SSH, 53=DNS, 80=เว็บ, 443=เว็บปลอดภัย, 3389=รีโมทเดสก์ท็อป


def is_port_open(ip, port):             # ฟังก์ชันเช็คว่า port นี้เปิดไหม
    s = socket.socket()                 # สร้างช่องทางเชื่อมต่อ 1 อัน (เหมือนหยิบโทรศัพท์)
    s.settimeout(0.5)                   # รอได้แค่ครึ่งวินาที ไม่มีใครรับก็เลิก
    result = s.connect_ex((ip, port))   # ลองต่อไป ได้ 0 = ต่อติด, เลขอื่น = ต่อไม่ติด
    s.close()                           # วางสาย ปิดการเชื่อมต่อ
    return result == 0                  # True = port เปิด, False = port ปิด
for port in ports:                      # ไล่เช็คทีละ port
    result = is_port_open("192.168.1.1", port)          # เคาะประตู port นี้ของเราเตอร์
    print(f"Port {port}: {'Open' if result else 'Closed'}")  # ถ้าเปิดพิมพ์ Open ถ้าปิดพิมพ์ Closed



# บรรทัดทดลองที่ปิดไว้ ใช้เช็คทีละอันตอนเรียนรู้:
#result = is_port_open("192.168.1.222", 443)   # ลองเช็ค port 443 ของเครื่องที่น่าจะไม่มี
#print(result)                                 # ดูผล
#print(is_port_open("192.168.1.1", 80))        # เช็ค port 80 (เว็บ) ของเราเตอร์
#print(is_port_open("192.168.1.1", 443))       # เช็ค port 443 (เว็บปลอดภัย) ของเราเตอร์
#print(is_port_open("192.168.1.222", 80))      # เช็ค port 80 ของเครื่องที่น่าจะไม่มี




end_time = time.time()                  # จดเวลาตอนจบ
print(f"Time taken: {round(end_time - start_time, 2)}seconds")   # แสดงว่าใช้เวลาไปกี่วินาที
