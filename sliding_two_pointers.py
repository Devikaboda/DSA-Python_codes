"""#longest substring without repeating characters
def longest_substring(s):
    char_dict={}
    left=0
    max_length=0
    for right in range(len(s)):
        if s[right] in char_dict and char_dict[s[right]]>=left:
            left=char_dict[s[right]]+1
        char_dict[s[right]]=right
        max_length=max(max_length,right-left+1)
    
    return max_length
def main():
    s=input("Enter the string: ")
    print("Length of longest substring without repeating characters: ",longest_substring(s))
if __name__=="__main__":
    main()"""

#Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
#brute force approach
"""def longest_subarray_with_flips(nums, k):
    max_length=0
    n=len(nums)
    for i in range(n):
        zeros=0
        for j in range(i,n):
            if nums[j]==0:
                zeros+=1
            if zeros<=k:
                length=j-i+1
                max_length=max(max_length,length)
            else:
                break
    return max_length
def main():
    nums=list(map(int,input("enter arr of nums: ").split()))
    k=int(input("enter the value of k: "))
    print(longest_subarray_with_flips(nums,k))
if __name__=="__main__":
    main()"""

#optimal approach
"""def longest_subarray_with_flips(nums, k):
    left=0
    right=0
    max_length=0
    zeros=0
    while right<len(nums):
        if nums[right]==0:
            zeros+=1
        if zeros>k:
            if nums[left]==0:
                zeros-=1
            left+=1
        if zeros<=k:
            length=right-left+1
            max_length=max(max_length,length)
        right+=1
    return max_length
def main():
    nums=list(map(int,input("enter arr of nums: ").split()))
    k=int(input("enter the value of k: "))
    print(longest_subarray_with_flips(nums,k))
if __name__=="__main__":
    main()"""

#longest  repeating chracter replacement(424 leet)
#You are given a string s and an integer k.
#  You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.
#Return the length of the longest substring containing the same letter you can get after performing the above operations.
#brute force appraoch
"""def longest_repeating_char_replacement(s,k):
    max_length=0
    max_freq=0
    d={}
    n=len(s)
    for i in range(n):
        for j in range(i,n):
            if s[j] not in d:
                d[s[j]]=1
            if s[j] in d:
                d[s[j]]+=1
                max_freq=max(max_freq,d[s[j]])
            changes=(j-i+1)-max_freq
            if changes <=k:
                max_length=max_(max_length,j-i+1)
            else:
                break
    return max_length"""

#maximum points you can obtain from k cards
def max_points_from_k_cards(nums,k):
    right_sum=0
    left_sum=0
    max_sum=0
    n=len(nums)
    for i in range(k):
        left_sum+=nums[i]
    max_sum=left_sum

    right_index=n-1
    for i in range(k-1,-1,-1):
        left_sum=left_sum-nums[i]
        right_sum+=nums[right_index]
        right_index-=1
        max_sum=max(max_sum,left_sum+right_sum)
    return max_sum
def main():
    nums=list(map(int,input("enter nums: ").split()))
    k=int(input("enter k: "))
    print(max_points_from_k_cards(nums,k))
if __name__=="__main__":
    main()



            

    



   

