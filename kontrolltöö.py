#5 задание
k=7
c=2
a=0
g=0
b=0
while g==0:
    a=k - c
    k=a
    b+=1
    if a==1:
        g+=1
print(a,b)
#1 задание
a = ["  ^---^   "]
b = [" ( o o )  "]
c = ["  ! = !/) "]
n=int(input("Введите количество зверьков "))
for i in a+b+c:
    print(i*n)
    if n > 10:
        break
#2 задание
p = int(input("Показатель степени: "))
n = int(input("Предел: "))
 
i = 1
while i ** p <= n:
    print(i ** p, end=' ')
    i += 1
    if i <= 0:
        break
print("Последнее число,"
      " возведенное в степень:", i - 1)
#3 задание
#-----
#4 задание
a = 0
j = 0
for i in range (8):
 a = a + 3
 j += 2
 print (a,"час =",j ,"клеток")
 print (end =" ")
