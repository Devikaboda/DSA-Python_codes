#selection sort
'''def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
def main():
    arr=list(map(int,input("enter the elements: ").split()))
    print(selection_sort(arr))
if __name__=="__main__":
    main()'''

#bubble sort
'''def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def main():
    arr=list(map(int,input("enter the elements: ").split()))
    print(bubble_sort(arr))
if __name__=="__main__":
    main()'''
#insertion sort
'''def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j=j-1
    return arr
def main():
    arr=list(map(int,input("enter the elements: ").split()))
    print(insertion_sort(arr))
if __name__=="__main__":
    main()'''

#merge sort
'''
def merge_sort(arr,low,high):
    if low == high:
        return [arr[low]]
    mid=(low+high)//2
    if low < high:
        left=merge_sort(arr,low,mid)
        right=merge_sort(arr,mid+1,high)
    return merge(left,right)
def merge(left,right):
    
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i=i+1
        else:
            res.append(right[j])
            j=j+1
    while i<len(left):
        res.append(left[i])
        i=i+1
    while j<len(right):
        res.append(right[j])
        j=j+1
    return res
def main():
    arr=list(map(int,input("enter list of elements: ").split()))
    low=0
    high=len(arr)-1
    print(merge_sort(arr,low,high))
if __name__=="__main__":
    main()'''

#quick sort
def quick_sort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        quick_sort(arr,low,p-1) 
        quick_sort(arr,p+1,high)
def partion
    

            




        
