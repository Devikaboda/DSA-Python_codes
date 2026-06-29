#Consider an array of distinct integers. Your task is to determine and count all triplets in the array such that
#the sum of two elements in the triplet is equal to the third element.
#Write a function or algorithm to efficiently solve this problem.
"""def find_triplets(arr):
    n=len(arr)
    s=set(arr)
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]+arr[j]) in s:
                c+=1
    return c
def main():
    arr=list(map(int,input("enter arr of elements: ").split()))
    print(find_triplets(arr))

if __name__=="__main__":
    main()"""

#-----------------------------------------------------------------------------

#two sum II problem 
"""def two_sum_II(arr,target):
    n=len(arr)
    left=0
    right=n-1
    while left<right:
        s=arr[left]+arr[right]
        if s==target:
            return [left,right]
        elif s<target:
            left+=1
        else:
            right-=1
    return []
def main():
    arr=list(map(int,input("enter arr of elements: ").split()))
    target=int(input("enter the target value: "))
    print(two_sum_II(arr,target))
if __name__=="__main__":
    main()"""



