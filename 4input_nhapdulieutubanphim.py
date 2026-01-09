 #input
a = input("bo m hoi gtri cua a :")
print(type(a))
"""ép kiểu 
int() ; ésp ra số nguyênp
float() ép sang số thực
str() ép chuỗi kí tự string"""
a = int(input("nhap cmm gtr cho t"))
print(type(a))
print(a)

# nhập nhiều giá trị trên 1 dòng
#b1 nhap cac so ra
p = input("nhap cac so :")
#B2 tách số
t = p.split()
#b3 sd hàm map để ép phần tử trong list , int float hay str
x , y , z = map(int, t)
print(x, y, z)

 #clean code doan tren
x , y , z , t = map(float, input("yuđbibid").split())
print(x + y - z * t)










  