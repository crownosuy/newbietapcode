#input
a = input("bo m hoi gtri cua a :")
print(type(a))
"""ép kiểu 
int() ; ésp ra số nguyênp
float() ép sang số thực
str() ép chuỗi kí tự string"""
a = int(input("bo m hoi gtri cua a :"))
print(type(a))
# nhập nhiều giá trị trên 1 dòng
#b1 nhap cac so ra
p = input("nhap cac so :")
#B2 tách số
t = p.split()
#b3 sd hàm map để ép phần tử trong list , int float hay str
x , y , z = map(int, t)
print(x, y, z)

 #clean code
  x , y , z , t = map(float(input(" nhap cac so cmmmd :").split()))
  print( x + y *t - y )
  