#minimum flip bits to conver a number
"""def count_flip_bits(start,goal):
    res=start^goal
    count=0
    while res:    #means while res!=0
        res=res&(res-1)
        count+=1
    return count
def main():
    start=int(input("Enter the start number: "))
    goal=int(input("Enter the goal number: "))
    print("Minimum flip bits required: ",count_flip_bits(start,goal))
if __name__=="__main__":
    main()"""

#------------------------------------------------------------
#Given an integer array nums of unique elements, return all possible subsets (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.
"""def subsets(nums):
    ans=[]
    n=len(nums)
    subsets=1<<n
    for i in range(subsets):
        res=[]
        for j in range(n):
            if (i&(1<<j))!=0:    #if the jth bit of i is set, then include nums[j] in the current subset
                res.append(nums[j])
        ans.append(res)
    return ans
def main():
    nums=list(map(int,input("Enter the numbers: ").split()))
    print("All possible subsets are: ",subsets(nums))
if __name__=="__main__":
    main()"""


            
        