
import math
# code to convert decimal to binary
'''def decimal_to_binary(n):
    b=' '
    while n>=1:
        x=n%2
        n=n//2
        b=str(x)+b
    return b
def main():
    n=int(input("enter a number: "))
    print(decimal_to_binary(n))
if __name__=="__main__":
     main()'''
#code to covert binary to decimal
'''def binary_to_decimal(n):
    res=0
    power_of_2=1
    for i in range(len(n)-1,-1,-1):
        if n[i]=='1':
            res=res+(power_of_2)
        power_of_2=power_of_2*2
    return res
def main():
    n=input("enter a binary number: ")
    print(binary_to_decimal(n))
if __name__=="__main__":
    main()'''

#when we want to switch on i th bit we use or(|)
'''def main():
    n=int(input("enter a number: "))
    i=int(input("enter the position of the bit: "))
    mask=1<<i
    print(n|mask)
if __name__=="__main__":
    main()'''
#when we want to switch off i th bit  then we use and(&)
'''def main():
    n=int(input("enter a number: "))
    i=int(input("enter the position of the bit: "))
    mask=~(1<<i)
    print(n & mask)
if __name__=="__main__":
    main()'''
#when we wnat to toggle the i th bit we use xor(^)
'''def main():
    n=int(input("enter a number: "))
    i=int(input("enter the position of the bit: "))
    t_mask=(1<<i)
    print(n ^ t_mask)
if __name__=="__main__":
    main()'''

#to check whwther the bit is on or off we use and(&)
'''def main():
    n=int(input("enter a number: "))
    i=int(input("enter the position of the bit: "))
    c_mask=1<<i
    if (n & c_mask)==0:
        print(f"the {i} th bit is off")
    else:
        print(f"the {i} th bit is on")
if __name__=="__main__":
    main()'''

#programm to find rightmost set bit
'''def right_most(n):
    m=1
    pos=0
    while(m & n)==0:
        m=m<<1
        pos=pos+1
    return pos
def main():
    n=int(input("enter a number: "))
    print(right_most(n))
if __name__=="__main__":
    main()'''

#efficient aproach
'''def right_most(n):
    return int(math.log(n ^( n & (n-1)),2))
def main():
    n= int(input("enter a number: "))
    print(right_most(n))
if __name__=="__main__":
    main()'''

#to count number of set bits in given number
'''def count_set_bits(n):
    count=0
    while (n!=0):
        n=n&(n-1)
        count=count+1
    return count
def main():
    n=int(input("enter a number: "))
    print(count_set_bits(n))
if __name__=="__main__":
    main()'''
# to find whether the given number is power of 2 or not
'''def power_of_2(n):
    if n==0:
        return False
    return (n & (n-1))==0
def main():
    n=int(input("enter a number: "))
    print(power_of_2(n))
if __name__=="__main__":
    main()'''
#lonely integer problem leetcode 136
''' lonely_integer(arr):
    s=set()
    for i in arr:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    return s.pop()
def main():
    arr=list(map(int,input("enter the array of numbers: ").split()))
    print(lonely_integer(arr))
if __name__=="__main__":
    main()'''

# another efficient approach to solve lonely integer problem
''' lonely_integer(arr):
    res=0
    for i in arr:
        res=res^i
    return res
def main():
    arr=list(map(int,input("enter the array of numbers: ").split()))
    print(lonely_integer(arr))
if __name__=="__main__":    
    main()'''
#nuber of trailing zeros in binary representation of a number
'''import math
def trailing_zeros(n):
    return int(math.log((n &(n-1))^n,2))
def main():
    n=int(input("enter a number: "))
    print(trailing_zeros(n))
if __name__=="__main__":
    main()'''
