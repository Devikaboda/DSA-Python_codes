import math
from functools import reduce
'''a=10
b=20
print(a+b)
print(a,b,sep=",",end="??")'''

#print whether the given number is prime or not
'''n=int(input("enter a number: "))
for i in range(2,n+1):
    if n%i==0:
        break
if i==n:
    print(f"{n} prime number ")
else:
    print(f"{n}  is not a prime")'''

#lambda function

'''r=(lambda x,y:x**y)(3,2)
print(r)

fun=lambda a,b:a*b
res=fun(7,8)
res1=fun(2,3)
print(res)
print(res1)'''

'''
#filter
lst=[1,2,3,4,5,6]
l=list(filter(lambda x:x%2==0,lst))
print(l)
#reduce
r=(reduce(lambda x,y:x+y,lst))
print(r)
#map
m=list(map(lambda x:x**2,lst))
print(m)'''

#program to print table using lambda functions
'''def fun(num):
    return lambda x:x*num
n=int(input("enter a number: "))
math_table=fun(n)
for i in range(1,11):
    print(f"{n} x {i} =",math_table(i))'''

#STRING TRANSLATION
s="Error 404 Was Foznd"
table=s.maketrans("abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ","0123456789")
s_table=s.translate(table)
print(s)
print(s_table)

