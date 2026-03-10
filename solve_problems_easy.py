#program to find largest element in list of elements
'''def largest_ele(lst):
    largest=lst[0]
    n=len(lst)
    for i in range(1,n):
        if lst[i]>lst[0]:
            largest=lst[i]
    return largest
def main():
    lst=list(map(int,input("enter  list of elements: ").split()))
    print(largest_ele(lst))
if __name__=="__main__":
    main()'''

#programm to find second largest element in an list
'''def second_largest(lst):
    largest=lst[0]
    second_lar=-1
    n=len(lst)
    for i in range(1,n):
        if lst[i]> lst[0]:
            largest=lst[i]
    
    for i in range(n):
        if lst[i]>second_lar and lst[i]!=largest:
            second_lar=lst[i]
    return second_lar
def main():
    lst=list(map(int,input("enter the list of elements: ").split()))
    print(second_largest(lst))
if __name__=="__main__":
    main()'''
# another approach of second largest element
'''def second_largest(lst):
    largest=second_lar=float("-inf")
    n=len(lst)
    for i in range(n):
        if lst[i]>=largest:
            second_lar=largest
            largest=lst[i]
        if lst[i]<largest and lst[i]>second_lar:
            second_lar=lst[i]
        if second_lar == float("-inf"):
            return largest, None

    return largest,second_lar
def  main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(second_largest(lst))
if __name__=="__main__":
    main()'''
# programm to check whether the list is sorted or not
'''def is_sorted(lst):
    n=len(lst)
    for i in range(1,n):
        if lst[i]>=lst[i-1]:
            pass
        else:
            return False
    return True
def main():
    lst=list(map(int,input("enter the list of elements: ").split()))
    print(is_sorted(lst))
if __name__=="__main__":
    main()'''
#i am confused here
'''def duplicates(lst):
    s=set()
    n=len(lst)
    for i in range(n):
        s.insert(lst[i])
    for i in range(s):'''
# remove duplicates and identify number of unique elements in list of elements
'''def duplicates(lst):
    i=0
    for j in range(1,len(lst)):
        if lst[j]!=lst[i]:
            lst[i+1]=lst[j]
            i=i+1
    return i+1
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(duplicates(lst))
if __name__=="__main__":
    main()'''

#left rotate the list by one place [time complexity is o(n)  
# and space complexity is o(1)becz we are not taking extra space we are using avaliabale list only]
'''def left_rotation_one(lst):
    temp=lst[0]
    n=len(lst)
    for i in range(1,n):
        lst[i-1]=lst[i]
    lst[n-1]=temp
    return lst
 
def main():
    lst=list(map(int,input("enter the list of elements: ").split()))
    print(left_rotation_one(lst))
if __name__=="__main__":
    main()'''

#left rotate the list by d places
""" def left_rotation_dplaces(lst,d):
    temp=lst[0:d]
    n=len(lst)
    d=d%n          #d>n
    for i in range(d,n):
        lst[i-d]=lst[i]
    #j=0
    for i in range(n-d,n):
        #lst[i]=temp[j]
        #j=j+1
        lst[i]=temp[i-(n-d)] #with out using variable j
        
    return lst
def main():
    lst=list(map(int,input("enter the list of elements: ").split()))
    d=int(input("enter number of elements you want to shft: "))
    print(left_rotation_dplaces(lst,d))
if __name__=="__main__":
    main() """

# another effcient approach using slicing
""" def left_rotation_dplaces(lst,d):
    n=len(lst)
    d=d%n
    return lst[d:]+lst[:d]
def main():
    lst=list(map(int,input("enter the list of elements: ").split()))
    d=int(input("enter number of elemnts to shift: "))
    print(left_rotation_dplaces(lst,d))
if __name__=="__main__":
    main() """

#right rotation

""" def right_r(lst,k):
    n=len(lst)
    k=k%n
    return lst[n-k:n ]+lst[0:n-k]
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    k=int(input("enter k: "))
    print(right_r(lst,k))
if __name__=="__main__":
    main() 
 """
 
 #move all zeros to the end of the list
""" def move_zeros_toend(lst):
    n=len(lst)
    temp=[]
    for i in range(len(lst)):
        if lst[i]!=0:
            temp.append(lst[i])
    for i in range(len(temp)):
        lst[i]=temp[i]
    for i in range(len(temp),n):
        lst[i]=0
    return lst
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(move_zeros_toend(lst))
if __name__=="__main__":
    main()
 """
#another efficient approach
""" def move_zeros_toend(lst):
    n=len(lst)
    j=-1
    for i in range(n):
        if lst[i]==0:
            j=i
            break
    for i in range(j+1,n):
        if lst[i]!=0:
            lst[i],lst[j]=lst[j],lst[i]
    return lst
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(move_zeros_toend(lst))

if __name__=="__main__":
    main()
 """
#linear search
""" def linear_search(lst,num):
    n=len(lst)
    for i in range(len(lst)):
        if lst[i]==num:
            return i
        
    return -1
def main():
    lst=list(map(int,input("enter list of elemnts: ").split()))
    num=int(input("enter number to be searched: "))
    print(linear_search(lst,num))

if __name__=="__main__":
    main()

 """
 #union of two  sorted lists using set
'''def union(a,b):
    n1=len(a)
    n2=len(b)
    i=j=0
    s=set()
    while i<n1 and j<n2:
        if a[i]<=b[j]:
            s.add(a[i])
            i=i+1
        else:
            s.add(b[j])
            j=j+1
    while i<n1:
        s.add(a[i])
        i=i+1
    while j<n2:
        s.add(b[j])
        j=j+1

    return sorted(s)
def main():
    a=list(map(int,input("enter list of elements: ").split()))
    b=list(map(int,input("enter list of elements: ").split()))
    print(union(a,b))   #   O(n1+n2)+klogk

if __name__=="__main__":
    main()'''


#union of two sorted lists using optimal merge algorithm without using set
""" def union(a,b):
    n1=len(a)
    n2=len(b)
    i=j=0
    res=[]
    while i<n1 and j<n2:
        if a[i]==b[j]:
            if not res or res[-1]!=a[i]:
                res.append(a[i])            
            i=i+1
            j=j+1
        elif a[i]<=b[j]:
            if not res or res[-1]!=a[i]:
                res.append(a[i])
            i=i+1
        else:
            if not res or res[-1]!=b[j]:
                res.append(b[j])
            j=j+1
                
    while i<n1:
        if not res or res[-1]!=a[i]:
            res.append(a[i])
        i=i+1

        
    while j<n2:
        if not res or res[-1]!=b[j]:
            res.append(b[j])
        j=j+1

        

    return res
def main():
    a=list(map(int,input("enter list of elements: ").split()))
    b=list(map(int,input("enter list of elements: ").split()))
    print(union(a,b))     #O(n1+n2)

if __name__=="__main__":
    main() 
 """
        
#program to find intersection of two sorted lists
""" def intersection(a,b):
    n1=len(a)
    n2=len(b)
    i=j=0
    res=set()
    for i in range(n1):
        for j in range(n2):
            if a[i]==b[j]:
                res.add(a[i])

    return sorted(res)
def main():
    a=list(map(int,input("enter list of elements: ").split()))
    b=list(map(int,input("enter list of elements: ").split()))
    print(intersection(a,b))     #O(n1+n2)

if __name__=="__main__":
    main() 
 """
#intersection of two sorted lists using optimal two ponter approach
""" def intersection(a,b):
    n1=len(a)
    n2=len(b)
    res=[]
    i=j=0
    while i<n1 and j<n2:
        if a[i]==b[j]:
            if not res or res[-1]!=a[i]:
                res.append(a[i])
            i=i+1
            j=j+1
        
       
        elif a[i]<b[j]:
            i=i+1
        else:
            j=j+1
    return res
def main():
    a=list(map(int,input("enter list of elements: ").split()))
    b=list(map(int,input("enter list of elements: ").split()))
    print(intersection(a,b))     #O(n1+n2)

if __name__=="__main__":
    main() 
 """
#find missing element in list of 1 to n[brute force approach]
""" def missing(lst):
    n=len(lst)+1
    
    for i in range(1,n+1):
        f=0
        for j in range(len(lst)):
            if lst[j] == i:
                f=1
                break
        if f==0:
            return i
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(missing(lst))
if __name__=="__main__":
    main()
     """
#optimal approach using set[hashing]
'''def missing(lst):
    n=len(lst)+1
    s=set(lst)
    for i in range(1,n+1):
        if i not in s:
            return i
    
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(missing(lst))
if __name__=="__main__":
    main()'''
#another approach
'''def missing(lst):
    n=len(lst)+1
    total=n*(n+1)//2
    return total-sum(lst)
    
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(missing(lst))
if __name__=="__main__":
    main()'''
#another approach using xor
""" def missing(lst):
    n=len(lst)+1
    xor1=0
    for i in range(1,n+1):
        xor1=xor1^i
    xor2=0
    for i in lst:
        xor2=xor2^i
    return xor1^xor2
    
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(missing(lst))
if __name__=="__main__":
    main()
 """

#to find maximum consecutive ones
'''def max_count_ones(lst):
    
    count=0
    maxim=0
    for i in lst:
        if i==1:
            count=count+1
            maxim=max(count,maxim)
        else:
            count=0
    return maxim
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(max_count_ones(lst))

if __name__=="__main__":
    main()'''
#find longest subarray  with k sum (brute force approach)
""" def longest_subarray(lst,k):
 
    l=0
    n=len(lst)
    for i in range(n):
        c_sum=0
        for j in range(i,n):
            #for k in range(i,j):
            c_sum=c_sum+lst[j]
            if c_sum==k:
                l=max(l,j-i+1)
    return l
def main():
    lst=list(map(int,input("enter list iof elements: ").split()))
    k=int(input("enter the target sum: "))

    print(longest_subarray(lst,k))
if __name__=="__main__":
    main() """
#optimized way to find longest sub array with k sum  
# [pref_sum + hashing]
#this is used for both positives negatives and zeros

'''def longest_subarray(lst,k):
 
    l=0
    n=len(lst)
    pref_sum=0
    seen={}
    for i in range(n):
        pref_sum=pref_sum+lst[i]
        if pref_sum==k:
            l=i+1
        if (pref_sum-k) in seen:
            l=max(l,i-seen[pref_sum-k])
        if pref_sum not in seen:
            seen[pref_sum]=i
    return l
def main():
    lst=list(map(int,input("enter list iof elements: ").split()))
    k=int(input("enter the target sum: "))

    print(longest_subarray(lst,k))
if __name__=="__main__":
    main() '''

#optimal [using sliding window of two pointer approach]
#it is only possible for zeros and positives . produce wrong results when negatives are
#involved in list of inputs
""" def longest_subarray(lst,k):
 
    l=0
    n=len(lst)
    right=0
    left=0
    c_sum=0
    while right<n:
        c_sum=c_sum+lst[right]
        while left<=right and c_sum>k :
            c_sum=c_sum-lst[left]
            left=left+1
        if c_sum==k:
            l=max(l,right-left+1)
        right=right+1
        
    return l
def main():
    lst=list(map(int,input("enter list iof elements: ").split()))
    k=int(input("enter the target sum: "))

    print(longest_subarray(lst,k))
if __name__=="__main__":
    main() 
 """
        

        
















        


 
 
