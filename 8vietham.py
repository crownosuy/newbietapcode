#function
def tong(a, b):
    res = a + b
    return res
x , y = 345678987654 , 234567898753
print(tong(x, y))
def ditmemay(name1, name2, name3):
    print("địt cụ mày " , name1, name2 ,name3)
print(ditmemay("thái", "mạnh", "linh"))
#default ảgument
def in4(fb, job = "coder"):
    print(fb , job)
def check(p):
  if p % 3 == 0 and p % 5 == 0:
    return True
  else:
      return False
#code chạy ctr
if __name__ == '__main__':
    #code
    c , d = map(int, input().split())
    print(tong(c , d))
#keywork argument
    ditmemay(name2 = "g" , name3 = "GH" , name1 = "7")
#default ảgument
    in4("crow zt" )
#hamf tinhs giai thuawf
def gt(n):
    crow = 1
    for i in range(1 , n+1):
        crow *= i
    return crow
print(gt(6))
#a^b
def mu (a , b):
    g = 1
    for i in range(b):
        g *= a
    return g 
print(mu(5, 54))

p = int(input())
if check(p):    
        print("Y")
else:
         print("N")
