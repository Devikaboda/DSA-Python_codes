
# print the name n times using recursion
'''def print_name(n):
    if n == 0:   
        return
    print("deva")
    print_name(n - 1)  # recursive call

def main():
    n = int(input("Enter a number: "))
    print_name(n)

if __name__ == "__main__":
    main()'''

#print the numbers from 1 to n using recursion
'''def print_numbers(i,n):
    if i>n:
        return
    print(i)
    print_numbers(i+1,n)
def main():
    n=int(input("enter a number: "))
    print_numbers(1,n)
if __name__=="__main__":
    main()'''

#print the numbers from n to 1 using recursion
''' print_numbers(i,n):
    if i<1:
        return 
    print(i)
    print_numbers(i-1,n)
def main():
    n=int(input("enter a number: "))
    print_numbers(n,n)
if __name__=="__main__":
    main()'''

#print the numbers from 1 to n using recursion concept of backtracking
''' print_numbers(i,n):
    if i<1:
        return
    print_numbers(i-1,n)
    print(i)
    
def main():
    n=int(input("enter a number: "))
    print_numbers(n,n)
if __name__=="__main__":
    main()'''

#print the numbers from n   to 1 using recursion concept of backtracking
'''
def print_numbers(i,n):
    if i>n:
        return
    print_numbers(i+1,n)
    print(i)
    
def main():
    n=int(input("enter a number: "))
    print_numbers(1,n)
if __name__=="__main__":
    main()'''

#to find sum of n natural numbers using recursion
'''def sum_n(i,sum):
    if i<1:
        print(sum)
        return
    sum_n(i-1,sum+i)
def main():
    n=int(input("enter a number: "))
    sum_n(n,0)
if __name__=="__main__":
    main()'''
#another approach using function
'''def sum_n(n):
    if n==0:
        return 0
    else:
        return n+sum_n(n-1)
def main():
    n=int(input("enter a number: "))
    print(sum_n(n))
if __name__=="__main__":
    main()'''
#reverse of array using recursion
'''def reverse(lst,l,r):
    if l>=r:
        return lst 
    else:
        lst[l],lst[r]=lst[r],lst[l]
        return reverse(lst,l+1,r-1)
        
def main():
    lst=list(map(int,input("enter the elements: ").split()))
    n=len(lst)
    print(reverse(lst,0,n-1))
if __name__=="__main__":
    main()'''
#another approach
'''def reverse(lst,i):
    n=len(lst)
    if i>n//2:
        return lst
    lst[i],lst[n-i-1]=lst[n-i-1],lst[i]
    return reverse(lst,i+1)
        
def main():
    lst=list(map(int,input("enter the elements: ").split()))
    
    print(reverse(lst,0))
if __name__=="__main__":
    main()'''
#print whether the string is palindrome or not using recursion
'''def palindrome(s,i):
    n=len(s)
    if i>n//2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return palindrome(s,i+1)
def main():
    str=input("enter a string: ")
    print(palindrome(str,0))
if __name__=="__main__":
    main()'''

#program to print fibanacci of a number using recursion
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
def main():
    n=int(input ("enter a number: "))
    print(fib(n))
if __name__=="__main__":
    main()
    
    
    
    
    

   

