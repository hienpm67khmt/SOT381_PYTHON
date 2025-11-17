W=float(input("Nhập số cân nặng của bạn (kg):"))
H=float(input("Nhập chiều cao của bạn (m):"))
bmi=W/(H*H)
if bmi < 18.5:
    print("Gầy")
elif bmi >= 18.5 and bmi <24.9:
    print("Bình thường")
else:
    print("Thừa cân")
