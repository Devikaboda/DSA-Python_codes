#two sum
""" def two_sum(lst,target_sum):
    n=len(lst)
    for i in range(n):
        for j in range(i+1,n):
            if lst[i]+lst[j]==target_sum:
                return i,j
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    target_sum=int(input("enter target value: "))
    print(two_sum(lst,target_sum))
if __name__=="__main__":
    main() """
#another approach   [tc-o(n) hasing technique]
'''def two_sum(lst,target_sum):
    seen=set()
    for i in lst:
        if (target_sum-i) in seen:
            return i,target_sum-i
        seen.add(i)
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    target_sum=int(input("enter target value: "))
    print(two_sum(lst,target_sum))
if __name__=="__main__":
    main()'''

#two pointer approach: if sorted tc-o(n) else tc-o(nlogn)

""" def two_sum(lst,target_sum):
    n=len(lst)
    left=0
    right=n-1
    c_sum=0
    lst.sort()
    for i in range(0,n):
        c_sum=lst[left]+lst[right]
        if c_sum==target_sum:
            return lst[left],lst[right]
        elif c_sum>target_sum:
            right=right-1
        else:
            left=left+1


    
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    target_sum=int(input("enter target value: "))
    print(two_sum(lst,target_sum))
if __name__=="__main__":
    main() """

#to sort list of 0's ,1's and 2's
#brute force way is using any soring algorithm
#better way
""" def sort_012(lst):
    n=len(lst)
    c0=c1=c2=0
    for i in range(n):
        if lst[i]==0:
            c0=c0+1
        if lst[i]==1:
            c1=c1+1
        if lst[i]==2:
            c2=c2+1
    for i in range(0,c0):
        lst[i]=0
    for i in range(c0,c0+c1):
        lst[i]=1
    for i in range(c0+c1,n):
        lst[i]=2
    return lst
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(sort_012(lst))
if __name__=="__main__":
    main() """
#optimsal approach using dutch national falg algorithm
""" def sort_012(lst):
    n=len(lst)
    low=mid=0
    high=n-1
    while mid<=high:
        if lst[mid]==0:
            lst[mid],lst[low]=lst[low],lst[mid]
            low=low+1
            mid=mid+1
        elif lst[mid]==1:
            mid=mid+1
        else:
            lst[mid],lst[high]=lst[high],lst[mid]
            high=high-1
    return lst
def main():
    lst=list(map(int,input("enter list elements: ").split()))
    print(sort_012(lst))
if __name__=="__main__":
    main()
        
 """
#find an element in an array which is repeating more than n//2 times(majority element)
""" def majority_ele(lst):
    n=len(lst)
    for i in range(n):
        c=0
        for j in range(n):
            if lst[i]==lst[j]:
                c=c+1
        if c>n//2:
            return lst[i]
    return -1
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(majority_ele(lst))
if __name__=="__main__":
    main() """

#better solution
""" def majority_ele(lst):
    n=len(lst)
    d={}
    for i in range(n) :
        if lst[i] not in d:
            d[lst[i]]=1
        else:
            d[lst[i]]=d[lst[i]]+1
    for i in d:
        if d[i]>n//2:
            return i

    return -1
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(majority_ele(lst))
if __name__=="__main__":
    main()
 """

#optimal boyer moore voting algorithm
""" def boyer_moore(lst):
    c=0
    maj=None
    n=len(lst)
    for i in lst:
        if c==0:
            maj=i
        if i==maj:
            c=c+1
        else:
            c=c-1
    if lst.count(maj)>n//2:
        return maj
    else:
        return -1
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(boyer_moore(lst))
if __name__=="__main__":
    main()    
     """
#find alll sub arrays

""" def sub_array(lst):
    n=len(lst)
    l=[]
    for i in range(n):
        for j in range(i+1,n+1):
            s=[]
            for k in range(i,j):
                s.append(lst[k])
            l.append(s)
    return l
    
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(sub_array(lst))
if __name__=="__main__":
    main()  """

# to find maximum subarray sum       [brute force approach]

'''def max_subarray_sum(lst):
    n=len(lst)
    maxi=float("-inf")
    for i in range(n):
        for j in range(i+1,n+1):
            s=0
            for k in range(i,j):
                s=s+lst[k]
            maxi=max(maxi,s)
    return maxi
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(max_subarray_sum(lst))
if __name__=="__main__":
    main() '''
#better appraoch
#max sub array sum is not always whiole array sum

""" def max_subarray_sum(lst):
    n=len(lst)
    maxi=float("-inf")
    for i in range(n):
        s=0
        for j in range(i,n):
            s=s+lst[j]
            maxi=max(maxi,s)
    return maxi
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(max_subarray_sum(lst))
if __name__=="__main__":
    main() """
#optimal kadane's algoritham
""" def max_subarray_sum(lst):
    n=len(lst)
    s=lst[0]
    maxi=lst[0]
    for i in range(1,n):
        s=max(lst[i],s+lst[i])
        maxi=max(maxi,s)
    return maxi
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(max_subarray_sum(lst))
if __name__=="__main__":
    main()  """

#optimal kadane algorithm sum  and finding sub array also
#temp_start    => "possible starting point of a new subarray"
#start         = >"confirmed starting point of the max subarray found so far"
""" def max_subarray_sum(lst):
    n=len(lst)
    s=lst[0]
    maxi=lst[0]
    start=end=0
    temp_start=0
    for i in range(1,n):
        if lst[i]>s+lst[i]:
            s=lst[i]
            temp_start=i
        else:
            s=s+lst[i]
        if s>maxi:
            maxi=s
            start=temp_start
            end=i
    return maxi,lst[start:end+1]


def main():    
    lst=list(map(int,input("enter list of elements: ").split()))
    print(max_subarray_sum(lst))
if __name__=="__main__":
    main()
 """
# best time to buy and sell to maximize the profit[when we take input ]
""" def buy_sell(lst,b):
    n=len(lst)
    max_profit=0
    for i in range(n):
        if lst[b]<lst[i]:
            p=lst[i]-lst[b]
            max_profit=max(max_profit,p)
    return max_profit


def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    b=int(input("enter index of value you to buy "))
    print(buy_sell(lst,b))
if __name__=="__main__":
    main() """

#optimal approach to buy and sell a product by maximize its profit
""" def buy_sell(lst):
    n=len(lst)
    mini=lst[0]
    profit=0
    for i in range(1,n):
        cost=lst[i]-mini  #(buy before, sell after)
        profit=max(profit,cost)
        mini=min(mini,lst[i])
    
    return profit
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(buy_sell(lst))
if __name__=="__main__":
    main()  """
 
#rearrange elements by sign alternatively

""" def arrange_alternate(lst):
    n=len(lst)
    pos=[]
    neg=[]
    for i in range(n):
        if lst[i]>0:
            pos.append(lst[i])
        if lst[i]<0:
            neg.append(lst[i])
    for i in range(n//2):
        lst[i*2]=pos[i]
        lst[2*i+1]=neg[i]
    return lst
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(arrange_alternate(lst))
if __name__=="__main__":
    main()
 """
# another approach
""" def arrange_alternate(lst):
    n=len(lst)
    pos=0
    neg=1
    a=[0]*n
    for i in range(n):
        if lst[i]>0:
            a[pos]=lst[i]
            pos=pos+2
        else:
            a[neg]=lst[i]
            neg=neg+2
    return a

        
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    print(arrange_alternate(lst))
if __name__=="__main__":
    main()
  """
# above two approaches are work only when there are equal number of positives and negatives in
#a particular list if they are unequal then approacch is different lets see
""" def arrange_alternate(lst):
    pos=[i for i in lst if i>0]
    neg=[i for i in lst if i<0]
    a=[]
    i=j=0
    turn =0  # turn 0 menas postive, turn  1 represents negative
    while i<len(pos) and j< len(neg):
        if turn==0:
            a.append(pos[i])
            i=i+1
            turn =1
        else:
            a.append(neg[j])
            j=j+1
            turn =0
    return a
def main():

    lst=list(map(int,input("enter list of elements: ").split()))
    print(arrange_alternate(lst))
if __name__=="__main__":
    main()
  
 """
# to find leader of the list means consider an element as a leader if it is greater than 
#all the elements at right to it
""" def leader_list(lst):
    n=len(lst)
    l=[]
    
    for i in range(n):
        lead=True
        for j in range(i+1,n):
            if lst[j]>lst[i]:
                lead=False
                break
        if lead==True:
            l.append(lst[i])
                
    return l
def main():

    lst=list(map(int,input("enter list of elements: ").split()))
    print(leader_list(lst))
if __name__=="__main__":
    main() """

""" #optimal solution

def leader_list(lst):
    n=len(lst)
    l=[]
    maxi=float("-inf")
    for i in range(n-1,-1,-1):
        if lst[i]>maxi:
            l.append(lst[i])
            maxi=lst[i]
    return l
    #return l[::-1]  # reverse to maintain original order
def main():

    lst=list(map(int,input("enter list of elements: ").split()))
    print(leader_list(lst))
if __name__=="__main__":
    main() 
 """

#find the length of longest consecutive sequence
""" def longest_consecutive(lst):
    n=len(lst)
    longest=0
    for i in range(n):
        current=lst[i]
        length=1
        while current+1 in lst:
            current=current+1
            length=length+1
        longest=max(length,longest)
    return longest
   
def main():

    lst=list(map(int,input("enter list of elements: ").split()))
    print(longest_consecutive(lst))
if __name__=="__main__":
    main() 
 
 """
 # (using sorting )better solution O(n logn) 
""" def longest_consecutive(lst):
    n=len(lst)
    if not lst:
        return 0
    length=1
    count=1
    lst.sort()
    for i in range(1,n):
        if lst[i]==lst[i-1]+1:
            count=count+1
            length=max(length,count)
        elif lst[i]!=lst[i-1]:
            count=1
    return length
def main():

    lst=list(map(int,input("enter list of elements: ").split()))
    print(longest_consecutive(lst))
if __name__=="__main__":
    main()   """
#optimal solution
 
""" def longest_consecutive(lst):
    n=len(lst)
    if not lst:
        return 0
    longest=0
    nums=set(lst)
    for i in nums:
        if i-1 not in nums:
            current=i
            length=1
            while current+1 in nums:
                current=current+1
                length=length+1
            longest=max(longest,length)
    return longest
def main():

    lst=list(map(int,input("enter list of elements: ").split()))
    print(longest_consecutive(lst))
if __name__=="__main__":
    main() 

 """
 #set matrix zeros
""" def set_matrix_zeros(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    
    zero_rows=set()
    zero_cols=set()
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j]=0
    return matrix
def main():
    rows=int(input("enter number of rows: "))
    cols=int(input("enter number of cols: "))

    print("Enter matrix row by row (space separated):")
    matrix=[]
    for i in range(rows):
        row=list(map(int,input().split()))
        matrix.append(row)
    print("before")
    for row in matrix:
        print(row)
    set_matrix_zeros(matrix)
    for row in matrix:
        print(row)
if __name__=="__main__":
    main() """

# set matrix zeros another approach
""" def matrix_row(matrix,i,cols):
    for j in range(cols):
        if matrix[i][j]!=0:
            matrix[i][j]=None
def matrix_col(matrix,j,rows):
    for i in range(rows):
        if matrix[i][j]!=0:
            matrix[i][j]=None
        
def set_zeros_matrix(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                matrix_row(matrix,i,cols)
                matrix_col(matrix,j,rows)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==None:
                matrix[i][j]=0
    return matrix
def main():
    rows=int(input("enter number of rows: "))
    cols=int(input("enter number of cols: "))

    print("Enter matrix row by row (space separated):")
    matrix=[]
    for i in range(rows):
        row=list(map(int,input().split()))
        matrix.append(row)
    print("before")
    for row in matrix:
        print(row)
    print(set_zeros_matrix(matrix))
    for row in matrix:
        print(row)
if __name__=="__main__":
    main() 
      """
# better approach
""" def set_matrix_zeros(matrix):
    m=len(matrix)
    n=len(matrix[0])
    row=[0]*m
    col=[0]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
    for i in range(m):
        for j in range(n):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=0
    return matrix
def main():
    rows=int(input("enter number of rows: "))
    cols=int(input("enter number of cols: "))
    print("enter the matrix row by row(space separated): ")
    matrix=[]
    
    for i in range(rows):
        row=list(map(int,input().split()))
        matrix.append(row)
    print("before")
    for row in matrix:
        print(row) 
    set_matrix_zeros(matrix)
    
    print("after")
    for row in matrix:
        print(row) 
if __name__=="__main__":
    main()
 """
#optimal approach using constatant space
# usin first row and sirst column as markers
""" def set_matrix_zeros(matrix):
    r=len(matrix)
    c=len(matrix[0])
    col=1
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                matrix[i][0]=0
                if j!=0:
                    matrix[0][j]=0
                else:
                    col=0
    for i in range(1,r):
        for j in range(1,c):
            if matrix[i][j]!=0:
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
    if matrix[0][0]==0:
        for j in range(c):
            matrix[0][j]=0
    if col==0:
        for i in range(r):
            matrix[i][0]=0
    return matrix
def main():
    rows=int(input("enter number of rows: "))
    cols=int(input("enter number of cols: "))
    print("enter the matrix row by row(space separated): ")
    matrix=[]
    
    for i in range(rows):
        row=list(map(int,input().split()))
        matrix.append(row)
    print("before")
    for row in matrix:
        print(row) 
    set_matrix_zeros(matrix)
    
    print("after")
    for row in matrix:
        print(row) 
if __name__=="__main__":
    main() """
 
#rotate matrix by 90 degree clock wise
#brute force apporach
""" def rotate_by_90(matrix):
    
    n=len(matrix)
    arr=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr[j][n-1-i]=matrix[i][j]
    return  arr
def main():
    rows=int(input("enter number of rows: "))
    print("enter matrix row by row (space separated)")
    matrix=[]
    for i in range(rows):
        row=list(map(int,input().split()))
        matrix.append(row)
    print("before")
    for row in matrix:
        print(row)
    rotated=rotate_by_90(matrix)
    for row in rotated:
        print(row)
if __name__=="__main__":
    main()
 """
""" #optimal apporach
def rotate_by_90(matrix):
    n=len(matrix)
    #transpose
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
def main():
    rows=int(input("enter number of rows: "))
    print("enter matrix row by row (space separated)")
    matrix=[]
    for i in range(rows):
        row=list(map(int,input().split()))
        matrix.append(row)
    print("before")
    for row in matrix:
        print(row)
    rotated=rotate_by_90(matrix)
    for row in rotated:
        print(row)
if __name__=="__main__":
    main()
 """

 #spiral matrix
""" def spiral_matrix(matrix):
    res=[]
    n=len(matrix)
    m=len(matrix[0])
    bot,right=n-1,m-1
    top=left=0
    
    while top<=bot and left<=right:
        for i in range(left,right+1):
            res.append(matrix[top][i])
        top=top+1
        for i in range(top,bot+1):
            res.append(matrix[i][right])
        right=right-1
        if top<=bot:
            for i in range(right,left-1,-1):
                res.append(matrix[bot][i])
            bot=bot-1
        if left<=right:
            for i in range(bot,top-1,-1):
                res.append(matrix[i][left])
            left=left+1
    return res
def main():
    rows=int(input("enter number of rows: "))
    cols=int(input("enter number of cols: "))
    print("enter matrix row by row (space separated)")
    matrix=[]
    for i in range(rows):
        row=list(map(int,input().split()))
        matrix.append(row)
    print("before")
    for row in matrix:
        print(row)
    result=spiral_matrix(matrix)
    print(result)
if __name__=="__main__":
    main() """
#count the number of subarrays having sum equal to k
#brute force apporach
""" def count_subarray_sumk(lst,k):
    n=len(lst)
    c=0
    for i in range(n):
        for j in range(n):
            s=0
            for p in range(i,j+1):
                s=s+lst[p]
            if s==k:
                c=c+1
    return c
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    k=int(input("enter the value of k: "))
    print(count_subarray_sumk(lst,k))
if __name__=="__main__":
    main() """
#better approach
""" def count_subarray_sumk(lst,k):
    n=len(lst)
    c=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s=s+lst[j]
            if s==k:
                c=c+1
    return c
def main():
    lst=list(map(int,input("enter list of elements: ").split()))
    k=int(input("enter the value of k: "))
    print(count_subarray_sumk(lst,k))
if __name__=="__main__":
    main()

 """
#optimal approach
def longest_subarray(lst,k):
 
    l=0
    n=len(lst)
    pref_sum=0
    seen={}
    c=0
    for i in range(n):
        pref_sum=pref_sum+lst[i]
        if pref_sum==k:
            c=c+1

        if (pref_sum-k) in seen:
            c=c+seen[pref_sum-k]
            
        if pref_sum in seen:
            seen[pref_sum]=seen[pref_sum]+1
        else:
            seen[pref_sum]=1
    return c
def main():
    lst=list(map(int,input("enter list iof elements: ").split()))
    k=int(input("enter the target sum: "))

    print(longest_subarray(lst,k))
if __name__=="__main__":
    main() 


    


 

        


