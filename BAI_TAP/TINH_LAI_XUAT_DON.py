tien=int(input("Nhập số tiền gửi:"))
lai=float(input("Nhập vào lãi suất (%/năm):"))
thang=int(input("Nhập vào số tháng gửi:"))
tien_lai=(tien*lai*thang)/12
if tien_lai.is_integer():
    tien_lai = int(tien_lai)

print("Tiền lãi là:",round(tien_lai,3))
