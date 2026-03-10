import math
from collections import Counter
#find factorial of given number using iterative method
'''def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
def main():
    n=int(input("enter a number: "))
    print(factorial(n))
if __name__ == "__main__":
    main()
    
-------------------------------------------'''

#write a program to count number of digits in a given number
'''def count_digits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
def main():
    n=int(input("enter a number: "))
    print(count_digits(n))
if __name__=="__main__":
    main()
    -------------------------------------------'''

#given a number find the number of trailing zeros of its factorial
'''def trailing_zeros(n):
    res=0
    powerof5=5      #n!=n/5+n/25+n/125+....
    while n>=powerof5:
        res=res+n//powerof5
        powerof5=powerof5*5
    return res
def main():
    n=int(input("enter a number: "))
    print(trailing_zeros(n))
if __name__=="__main__":
    main()
-------------------------------------------'''

#write a programm to find gcd of two numbers
'''def gcd(a,b):
    min=0
    if a<b:
        min=a
    else:
        min=b
    for i in range(min,0,-1):
        if(a%i==0 and b%i==0):
            return i
def main():
    a=int(input("enter a number: "))
    b=int(input("enter another numner: "))
    print(gcd(a,b))
if __name__=="__main__":
    main()'''

#euclid's gcd 
'''def euclid_gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
def main():
    a=int(input("enter a number: "))
    b=int(input("enter another  number: "))
    print(euclid_gcd(a,b))
if __name__=="__main__":
    main()'''

#optimized euclid gcd
'''def optimized_euclid_gcd(a,b):
    while (a!=0 and b!=0):
        if (a>b):
            a=a % b
        else:
            b=b % a
    if (a!=0):
        return a
    else:
        return b
def main():
    a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    print(optimized_euclid_gcd(a,b))
if __name__== "__main__":
    main()'''

#programm to find lcm of two numbers
'''def lcm (a,b):
    res=max(a,b)
    while True:
        if res%a==0 and res%b==0:
            return res
        res=res+1
def main():
    a=int(input("enter anumber: "))
    b=int(input("enter aniother number: "))
    print(lcm(a,b))
if __name__=="__main__":
    main()'''

#optimized lsm using gcd 
'''def gcd(a,b):
    while (a!=0 and b!=0):
        if (a>b):
            a=a%b
        else:
            b=b%a
    if(a!=0):
        return a
    else:
        return b
def lcm(a,b):
    return (a*b)//gcd(a,b)
def main():
    a=int(input("enter a number;"))
    b=int(input("enter another number: "))
    print(lcm(a,b))
if __name__=="__main__":
    main()'''

#find whether the given number is prime or not
'''def is_prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def main():
    n=int(input("enter a number: "))
    print(is_prime(n))
if __name__=="__main__":
    main()'''

#another efficient approcach to check prime
'''def is_prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
def main():
    n=int(input("enter a number: "))
    print(is_prime(n))
if __name__=="__main__":
    main()'''
#another more effficinet approach to check prime or not
'''def prime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True
def main():
    n=int(input("enter a number: "))
    print(prime(n))
if __name__=="__main__":
    main()'''
# programm to find all prime numbers in a given range
'''def sieve_of_eratosthenes(n):
    prime=[False]*(n+1)
    for i in range(2,n+1):
        if (prime[i]==False):
            for j in range(i*i,n+1,i):
                prime[j]=True
    primes=[]
    for i in range(2,n+1):
        if (prime[i]==False):
            primes.append(i)
    return primes

def main():
    n=int(input("enter a number:"))
    print(sieve_of_eratosthenes(n))
if __name__=="__main__":
    main()'''

#print all divisors of a given number[BRUTE FIRCE APPROACH]
'''def all_divisors(n):
    divisors=[]
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    return divisors
def main():
    n=int(input("enter a number: "))
    print(all_divisors(n))
if __name__=="__main__":
    main()'''
# [EFFIECIENT APPROACH] to find all divisors of a given number
'''def all_divisors(n):
    divisors=[]
    for i in range(1,int(math.sqrt(n))+1):
        if (n%i==0):
            divisors.append(i)
    for i in range(int(math.sqrt(n)),0,-1):
        if (n%i==0 and i!=n//i):
             divisors.append(n//i)
    return divisors
def main():
    n=int(input("enter a number: "))
    print(all_divisors(n))
if __name__=="__main__":
    main()'''

#program to print prime factors of a given number
'''def prime_factors(n):
    i=2
    while(i<int(math.sqrt(n))+1):
        while(n%i==0):
            print(i)
            n=n//i
        i=i+1
    if n>1:
        print(n)
def main():
    n=int(input("enter a number: "))
    prime_factors(n)
if __name__=="__main__":
    main()'''

#program to find the reverse of a number
'''def reverse_number(n):
    rev=0
    while n>0:
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return rev
def main():
    n=int(input("enter a number: "))
    print(reverse_number(n))
if __name__=="__main__":
    main()'''

#another apporach by deva

'''
def reverse_number(n):
    rev=[]
    while n>0:
        dig=n%10
        rev.append(str(dig))
        n=n//10
    return int("".join(rev))
def main():
    n=int(input("enter a number: "))
    print(reverse_number(n))
if __name__=="__main__":
    main()'''

#to check whther a number is palindrome or not
'''def reverse_number(n):
    rev=[]
    
    while n>0:
        dig=n%10
        rev.append(str(dig))
        n=n//10
    return int("".join(rev))
def main():
    n=int(input("enter a number: "))
    t=n
    r=reverse_number(n)
    if t == r:
        print(True)
    else:
        print(False)
    
if __name__=="__main__":
    main()'''
#progranm to print whether a number is armstrong number or not
'''def armstrong(n):
    sum=0
    #order=len(str(n))
    order=int(math.log10(n)+1)
    while n>0:
        r=n%10
        sum=sum+r**order
        n=n//10
    return sum
def main():
    n=int(input("enter a number: "))
    
    if n==armstrong(n):
        print(True)
    else:
        print(False) 
if __name__=="__main__":
    main()'''

#leetcode roman to integer problem
'''def roman_int(s):
    d={"I" :1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    res=0
    n=len(s)
    for i in range(n):
        if i<n-1 and d[s[i]] < d[s[i+1]] :
            res=res-d[s[i]]
        else:
            res=res+d[s[i]]
    return res
def main():
    s=input("enter a string: ")
    print(roman_int(s))
if __name__=="__main__":
    main()'''

#longest common prefix leetcode 14
'''def common_prefix():
    str=["flower","flow","flight"]
    pref="flower"
    res=""
    n=len(str)
    for i in range(n):
        if len(str[i])<len(pref):
            pref=str[i]
    
    
    for j in range(len(pref)):
        for i in range(n):
            if pref[j]!=str[i][j]:
                return res
        res=res+pref[j]
    return res

        
def main():
    
    print(common_prefix())

if __name__=="__main__":
    main()'''
#leetcode 136  to find single element
'''def single(lst):
    n=len(lst)
    res=[]
    if len(lst)==1:
        return lst[0]
    for i in range(n):
        if lst[i] not in res:
            res.append(lst[i])
        else:
            res.remove(lst[i])
    return res[0]
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(single(lst))
if __name__=="__main__":
    main()'''
#another approach using hashing ttechnique of dictionary
def single(lst):
    freq=Counter(lst)     #Counter(lst) creates a dictionary-like object
    for num,cnt in freq.items():       # loop through (element, frequency)

        if cnt==1:
            return num

    
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(single(lst))
if __name__=="__main__":
    main()

# another efficient approach
""" def single(lst):
    n=len(lst)
    res=0
    for i in range(n):
        res=res^ lst[i]
    return res
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(single(lst))
if __name__=="__main__":
    main()
 """







