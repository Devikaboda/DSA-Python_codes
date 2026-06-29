#binary search
'''def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid  
        elif arr[mid]>target:
            high=mid-1      
        else:
            low=mid+1
    return -1
def main():
    arr=list(map(int,input("enter the array: ").split()))
    target=int(input("enter the target: "))
    print(binary_search(arr,target))
if __name__=="__main__":
    main()'''

#------------------------------------------------------------------

#lower boound arr[mid]>=target(see below problem that is lower bound is used in serch insert position )
#upper bound arr[mid]>target  thi is just information for you to learn the concept of lower and upper bound in binary search. 

#--------------------------------------------------------------------------------------------------------
#Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not,
# return the index where it would be if it were inserted in order (SEARCH INSERT POSITION PROBLEM)
'''def search_insert_position(arr,target):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid  
        elif arr[mid]>=target:
            ans=mid
            high=mid-1      
        else:
            low=mid+1
    return ans
def main():
    arr=list(map(int,input("enter the array: ").split()))
    target=int(input("enter the target: "))
    print(search_insert_position(arr,target))
if __name__=="__main__":
    main()'''

#-----------------------------------------------------------------------------------
#find first and last position of an element in a sorted array
#brute force approach time complexity is O(n) and space complexity is O(1)
'''def last_first_occurence(arr,target):
    first=-1
    last=-1
    for i in range(len(arr)):
        if arr[i]==target:
            if first==-1:
                first=i
            last=i
    return first,last
def main():
    arr=list(map(int,input("enter the array: ").split()))
    target=int(input("enter the target: "))
    print(last_first_occurence(arr,target))
if __name__=="__main__":
    main()'''

#optimal approach using binary search time complexity is O(log n) and space complexity is O(1)
'''def first_occurence(arr,target):
    low=0
    high=len(arr)-1
    first=-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            first=mid
            high=mid-1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return first
def last_occurence(arr,target):
    low=0
    high=len(arr)-1
    last=-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            last=mid
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return last
def main():
    arr=list(map(int,input("enter the array: ").split()))
    target=int(input("enter the target: "))
    print(first_occurence(arr,target),last_occurence(arr,target))
if __name__=="__main__":
    main()'''


#search the element in the rotated sorted array
"""def search_rotated_array(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
def main():
    arr=list(map(int,input("enter  rotated sorted array: ").split()))
    target=int(input("enter the target element: "))
    print(search_rotated_array(arr,target))
if __name__=="__main__":
    main()"""


#------------------------------------------------------------------------
#This problem is similar to Search in Rotated Sorted Array, but array  may contain duplicates. 
'''def search_rotated_arr_duplicates(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return True
        if (arr[low]==arr[mid] and arr[mid]==arr[high]):
            low+=1
            high-=1
            continue
        if arr[low]<=arr[mid]:
            if arr[low]<=target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return False
def main():
    arr=list(map(int,input("enter  rotated sorted array with duplicates: ").split()))
    target=int(input("enter the target element: "))
    print(search_rotated_arr_duplicates(arr,target))
if __name__=="__main__":
    main()'''

#--------------------------------------------------------------------
#finding the minimum element in a rotated sorted array
from numpy import inf


'''def find_minimium(arr):
    low=0
    high=len(arr)-1
    ans=float("inf")
    while low<=high:
        mid=low+(high-low)//2
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    return ans
def main():
    arr=list(map(int,input("enter a rotated sorted array: ").split()))
    print(find_minimium(arr))
if __name__=="__main__":
    main()'''

#------------------------------------
#finding single element in rotated sorted array
'''def find_single_element(arr):
    n=len(arr)
    low=1
    high=n-2
    if n==1:
        return arr[0]
    if arr[1]!=arr[0]:
        return arr[0]
    if arr[n-1]!=arr[n-2]:
        return arr[n-1]
    while low<=high:
        mid=low+(high-low)//2
        if (arr[mid]!=arr[mid+1]) and (arr[mid]!=arr[mid-1]):
            return arr[mid]
        if (mid%2==1 and arr[mid]==arr[mid-1]) or (mid%2==0 and arr[mid]==arr[mid]+1):
            low=mid+1
        else:
            high=mid-1
    return -1
def main():
    arr=list(map(int,input("enter rotated sorted arr :").split()))
    print(find_single_element(arr))
if __name__=="__main__":
    main()'''

#to find peak element in an array
'''def find_peak_ele(arr):
    n=len(arr)
    if n==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    low=1
    high=n-2
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low=mid+1
        elif arr[mid]>arr[mid+1]:
            high=mid-1
        else:
            high=mid-1
    return -1
def main():
    arr=list(map(int,input("enter arr of elements: ").split()))
    print(find_peak_ele(arr))
if __name__=="__main__":
    main()
 '''
#-------------------------------------------------------------------

#program tp find the square root of a number using binary search
'''def find_square_root(n):    
    low=0
    high=n
    ans=-1
    while low<=high:
        mid=low+(high-low)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
def main():
    n=int(input("enter a number: "))
    print(find_square_root(n))        
if __name__=="__main__":
    main()'''

#-------------------------------------------------------
#program to find  smallest divisor given a threshold
#The problem requires the ceiling of each division result. 
# Since integer division // gives the floor value,
#  I used the formula (num + divisor - 1) // divisor,
#  which efficiently computes ceil(num/divisor) without using math.ceil(). 
# This avoids floating-point operations and works in O(1) time for each numbe
'''def find_smallest_divisor(arr,threshold):
    low=1
    high=max(arr)
    ans=-1
    while low<=high:
        mid=low+(high-low)//2
        total=0
        for num in arr:
            total+= (num + mid - 1) // mid
        if total <= threshold:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def main():
    arr=list(map(int,input("enter the array: ").split()))
    threshold=int(input("enter the threshold: "))
    print(find_smallest_divisor(arr,threshold))
if __name__=="__main__":
    main()'''

#-------------------------------------------------------------------------
#to find the least capacity to ship packages within D days
"""def least_capacity_to_ship(weights,D):
    low=max(weights)
    high=sum(weights)
    ans=-1
    while low<=high:
        mid=low+(high-low)//2
        days=0
        total=0
        for weight in weights:
            if total+weight> mid:
                days+=1
                total=weight
            else:
                total+=weight
        if days<D:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def main():
    weights=list(map(int,input("enter the weights: ").split()))
    D=int(input("enter number of days: "))
    print(least_capacity_to_ship(weights,D))
if __name__=="__main__":
    main()

"""
#------------------------------------------------------------------------
#to find the k th missing positive number
#brute force approach time complexity is O(n) and space complexity is O(1)
'''def kth_missing_postive_number(arr,k):
    for i in range(len(arr)):
        if arr[i]<=k:
            k+=1
        else:
            break
    return k
def main():
    arr=list(map(int,input("enter the array: ").split()))
    k=int(input("enter the value of k: "))
    print(kth_missing_postive_number(arr,k))
if __name__=="__main__":
    main()'''

#optimall approach using binary search time complexity is O(log n) and space complexity is O(1)
"""def kth_missing_positive_number(arr,k):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        missing=arr[mid]-(mid+1)
        if missing<k:
            low=mid+1
        else:
            high=mid-1
    return high+k+1
    #or return low+k
def main():
    arr=list(map(int,input("enter the array: ").split()))
    k=int(input("enter the value of k: "))
    print(kth_missing_positive_number(arr,k))
if __name__=="__main__":
    main()"""

#----------------------------------------------------------------------
#program to find split array largest sum
#this is similar to painters partition problem and book allocation problem 
#this is also similar to least capacity to ship packages within D days problem
def split_array_largest_sum(arr,k):
    low=max(arr)
    high=sum(arr)
    res=-1
    while low<=high:
        mid=low+(high-low)//2
        allocation=1
        total=0
        for num in arr:
            if total+num>mid:
                allocation+=1
                total=num
            else:
                total+=num
        if allocation<=k:
            res=mid
            high=mid-1
        else:
            low=mid+1
    return res
def main():
    arr=list(map(int,input("enter the array: ").split()))
    k=int(input("enter the value of k: "))
    print(split_array_largest_sum(arr,k))
if __name__=="__main__":
    main()
        
    
        


    