"""" 
vong lap for va ham range
rfor i in ange(start , stop , step)
"""
for i in range(0 ,238 ):
    print(i, "i luv u ! please don't kill my heart")
# s = 1^1 + 2^2 +3^3 +.... n^n 
n = 1000
s = 0
for i in range(1 , n + 1):
    s += i ** i
print(s)
'''break va continue
break kthuc lenh ngay vf luôn vòng lặp khi nó đến đk
continue đc dug fđể bỏ qua vòng lặp hiện tại để đến vong lặp tếp theo

'''
#tu 1 den 10 chia het cho 7 thi ènd
for i in range(1 ,11):
    print(i , end = "discỏd mess" )
    if i % 7 == 0:
        break
    print('end')
#continue
for i in range(1 , 100 , 5):
    print("từ ngày mất em") 
    continue
    print("discord mess")
#vongf for loongf nhau
for i in range(3):
    for j in range(4):
        print( i , j)
# vong lap while :cx đ bt mô tả như nào nma nó sẽ chạy đến khi k thỏa mãn nx thì thôi
n = 1
while n<= 100:
    print(n)
    n += 2
else:
    print("end")

#yeu xu nhap so duong, nhap so am or so 0 thi nhập lai
while True:
    n = int(input("Nhajp n"))
    if n > 0:
        break
#đếm số,
n = 12345678
dem = 0
while n != 0:
    dem += 1
    n //= 10 
print("disscord mess " , dem)
#or
n =3456789 #esp thanh chuoi ki tu
print(len(str(n)))

#tính tổng chữ số,
n = 12345678
sam = 0
while n != 0:
    sam += n % 10
    n //= 10 
print("disscord mess " , sam)
#lat ngc so nguyen
n =12345678987654
lat = 0
while n != 0:
    lat = lat * 10 + n % 10
    n //= 10
print(lat)


