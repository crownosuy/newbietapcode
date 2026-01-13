#if để xác nhận điều kiện
#có thể kết hợp với and or not để có nhiều đk
if 389 > 32554:
    print("disscord mess")
#else sd trong th condition ben trong if sai
n = 30
if n % 3 ==1 or n % 5 == 1:
    print("VJH")
else:
    print("UIU")
# elif nwmf giữ else và if và dùng cho nhiều đk
#vd kiểm tra tháng có 30 hay 31 hay 28 ngày
t = 2
if t == 1 or t == 3 or t == 5 or t ==7 or t == 8 or t == 10 or t == 12:
    print(31)
elif t == 4 or t == 6 or t == 9 or t == 11:
    print(30)
else:
    print(28)
#toán tử 3 ngôi
#varỉable =statement if condition else statement
a , b = 100 , 200
crow = "deo" if a > b else "ngu lon" 
print(crow)
#if long nhau(nesred if)
#ktra n co phai chu cos 2 chu so chi het cho 3 5 6 k ?
n = int(input("nhap cmm gtri n: ")) 
if n >= 10 and n <= 99:
    if n % 3 == 0 and n % 5 == 0 and n % 6 == 0:
        print("ngon luon")
    else:
        print("s m ngu the ha con")
else:
    print("dum d gion")
  
