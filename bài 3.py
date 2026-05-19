print("--- HOSPITAL TRIAGE SYSTEM ---")
# input
# tên bệnh nhân str
# Tuổi bệnh nhân int
patient_name = input("Enter patient's full name: ")
patient_age = int(input("Enter patient's age: "))
# output
# Họ tên
# Tuổi
# Kết quả phân luồng

# phân tích 

# Đầu tiên
# Nhập tên và tuổi
# B2 kiểm tra điều kiện
# Tuổi < 0
# Tuổi > 150
# b3 phân loại
# Tuổi < 6 → ưu tiên bệnh nhi
# Tuổi >= 80 → ưu tiên người cao tuổi
# Còn lại → khám thường
# b4 In phiếu khám
if patient_age < 0 or patient_age > 150:
    print("ERROR: Invalid age (0-150).")
else:
    if patient_age < 6:
        priority = "PRIORITY: Pediatric patient - Send to Pediatrics Department."

    elif patient_age >= 80:
        priority = "PRIORITY: Elderly patient - Wheelchair support and send to Geriatrics Department."

    else:
        priority = "NORMAL CHECKUP: Please take a queue number and wait."

    print("\n--- ELECTRONIC MEDICAL TICKET ---")
    print("Patient Name:", patient_name)
    print("Patient Age:", patient_age)
    print("Result:", priority)


