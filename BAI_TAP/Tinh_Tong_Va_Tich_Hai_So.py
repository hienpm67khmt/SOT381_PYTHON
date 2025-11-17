try:
    a = int(input("nhập số a: "))
    b = int(input("nhập số b: "))

    print("tổng của số a và số b là:", a + b)
    print("tích của số a và số b là:", a * b)

except ValueError:
    print("Lỗi: a hoặc b không phải là số!")
