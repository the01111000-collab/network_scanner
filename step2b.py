# ===== ขั้นที่ 2b: เอาการ ping มาห่อเป็นฟังก์ชัน จะได้เรียกใช้ซ้ำได้ =====

import subprocess                       # เครื่องมือสั่งรันคำสั่งของ Windows (เช่น ping)

def is_online(target):                  # สร้างฟังก์ชันชื่อ is_online รับ IP เข้ามา 1 ตัว
    # ping 1 ครั้ง แล้วเก็บผลลัพธ์เป็นตัวหนังสือไว้
    result = subprocess.run(["ping", "-n", "1", target], capture_output=True, text=True)

    if "TTL" in result.stdout:          # ถ้ามีคำว่า TTL = เครื่องตอบกลับ
        return True                     # ส่งคำตอบกลับไปว่า "เปิดอยู่"
    else:                               # ถ้าไม่มี
        return False                    # ส่งคำตอบกลับไปว่า "ปิดอยู่"

print(is_online("192.168.1.1"))         # ทดสอบกับเราเตอร์ (น่าจะได้ True)
print(is_online("192.168.1.222"))       # ทดสอบกับ IP ที่น่าจะไม่มีเครื่อง (น่าจะได้ False)
print(is_online("10.255.255.1"))        # ทดสอบกับ IP นอกวง (น่าจะได้ False)
