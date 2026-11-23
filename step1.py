# ===== ขั้นที่ 1: ดูชื่อและ IP ของเครื่องตัวเอง =====

import socket                           # เครื่องมือเกี่ยวกับเครือข่าย


hostname = socket.gethostname()         # ถามว่าคอมเครื่องนี้ชื่ออะไร
my_ip = socket.gethostbyname(hostname)  # เอาชื่อเครื่องไปถามต่อว่า IP Address (บ้านเลขที่ในเครือข่าย) คืออะไร

print("ชื่อเครื่อง: " + hostname)        # แสดงชื่อเครื่องบนจอ
print("IP Address: " + my_ip)           # แสดง IP ของเครื่องบนจอ


# บันทึกช่วยจำ: 2 คำสั่งที่ใช้ในไฟล์นี้
#socket.gethostname()                   # -> ได้ชื่อเครื่อง
#socket.gethostbyname()                 # -> แปลงชื่อเครื่องเป็น IP
