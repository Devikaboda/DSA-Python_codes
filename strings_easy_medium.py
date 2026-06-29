#reverse the words in the string
#Brute force approach
"""def  reverse_words_in_string(s):
    word=""
    words=[]
    for ch in s:
        if ch!=" ":
            word+=ch
        else:
            if word:   #Only store the word if it is not empty means if word!=" "
                words.append(word)
                word=""
    if word:
        words.append(word)
    words.reverse()
    return " ".join(words)
def main():
    s=input('enter a string: ')
    print(reverse_words_in_string(s))
if __name__=="__main__":
    main()"""

#------------------------------------------------------------------
#largest odd substring
'''def largest_odd_sub(s):
    
    n=len(s)-1
    for i in range(n,-1,-1):
        if int(s[i])%2!=0:
            ans=s[:i+1]
            return ans.lstrip("0")
    return ""
 

def main():
    s=input("enter a string of numbers: ")
    print(largest_odd_sub(s))
if __name__=="__main__":
    main()'''


#------------------------------------------------------------

#remove outer most parentheses
'''def remove_outermost_par(s):
    depth=0
    ans=[]
    for ch in s:
        if ch=="(":
            if depth>0:
                ans.append(ch)
            depth+=1
        else:
            depth-=1
            if depth>0:
                ans.append(ch)
    return " ".join(ans)
def main():
    s=input("enter a string ")
    print(remove_outermost_par(s))
if __name__=="__main__":
    main()'''

#------------------------------------------------------------

#isomorphic string
'''def isomorphic(s,t):
    mapping={}
    used=set()
    for c1,c2 in zip(s,t):
        if c1 in mapping:
            if mapping[c1]!=c2:
                return False
        else:
            if c2 in used:
                return False
        mapping[c1]=c2
        used.add(c2)
    return True
    
def main():
    s=input("enter a string: ")
    t=input("enter another string: ")
    print(isomorphic(s,t))
if __name__=="__main__":
    main()'''

#------------------------------------------

#rotate string so that it equals to given goal
"""def rotate_string(s,goal):
    if len(s)!=len(goal):
        return False
    n=len(s)
    for i in range(n):
        x=(s[i: ]+s[:i])
        if x==goal:
            return True 
    return False
def main():
    s=input("enter a string: ")
    goal=input("enter the targetted goal: ")
    print(rotate_string(s,goal))
if __name__=="__main__":
    main()"""




#optimal approach
'''def rotate_string(s,goal):
    if len(s)!=len(goal):
        return False
    return goal in (s+s)
def main():
    s=input("enter a string: ")
    goal=input("enter the targetted goal: ")
    print(rotate_string(s,goal))
if __name__=="__main__":
    main()'''

#-----------------------------------------------------------------------

#sort characters by frequency
"""def sort_char_by_freq(s):
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1
    sorted_chars=sorted(d.items(),key=lambda x:(-x[1],x[0]))
    ans=""
    for ch ,freq in sorted_chars:
        ans=ans+ch*freq
    return ans
def main():
    s=input("enter a stringg: ")
    print(sort_char_by_freq(s))
if __name__=="__main__":
    main()"""
#-------------------------------------------------------------------------

#maximum nesting depth of parentheses
"""def max_depth(s):
    c_depth=0
    ma_depth=0
    for ch in s:
        if ch=="(":
            c_depth+=1
            if c_depth>ma_depth:
                ma_depth=c_depth
        elif ch==")":
            c_depth-=1
    return ma_depth
def main():
    s=input("enter a string: ")
    print(max_depth(s))
if __name__=="__main__":
    main()"""

#-------------------------------------------------
#string to integer conversion atoi using recursion
"""def atoi(s):
    sign=1
    n=len(s)
    num=0
    i=0
    while i<n and s[i]==" ":
        i+=1
    if i<n and s[i]=="-":
        sign=-1
        i+=1
    elif i<n and s[i]=="+":
        i+=1
             
    def solve(i, num):

        # base case
        if i >= n or not s[i].isdigit():
            return num

        # build number
        num = num * 10 + int(s[i])

        # recursive call
        return solve(i + 1, num)

    ans = solve(i, 0)

    ans = sign * ans

    # range checking
    INT_MIN = -2147483648
    INT_MAX = 2147483647

    if ans < INT_MIN:
        return INT_MIN

    if ans > INT_MAX:
        return INT_MAX

    return ans
    
    
def main():
    s=input("enter a string: ")
    print(atoi(s))
if __name__=="__main__":    
    main()
"""
#to generate  longest palindromic substring(brute force approach)complexity O(n^3)
'''def longest_palindrome(s):
    n=len(s)
    longest=""
    for i in range(n):
        for j in range(i,n):
            sub=s[i:j+1]
            if sub==sub[::-1] and len(sub)>len(longest):
                longest=sub
    return longest
def main():
    s=input("enter a string: ")
    print(longest_palindrome(s))    
if __name__=="__main__":    
    main()'''

#optimal approach using expand around center technique complexity O(n^2)
"""def longest_palindrome(s):
    n=len(s)
    res=""
    def expand(left,right):
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    for i in range(n):
        odd=expand(i,i)
        even=expand(i,i+1)  
        if len(odd)>len(res):
            res=odd
        if len(even)>len(res):
            res=even
    return res
def main():
    s=input("enter a string: ")
    print(longest_palindrome(s))
if __name__=="__main__":
    main()"""
#------------------------------------------------------------------------

#sum of beauty of all substrings
def beauty_sum(s):
    n=len(s)
    beauty=0
    for i in range(n):
        freq={}
        
        for j in range(i,n):
            freq[s[j]]=freq.get(s[j],0)+1
            #maxi=max(freq.values())
            #mini=min(freq.values())
            maxi=0
            for val in freq.values():
                if val>maxi:
                    maxi=val
            mini=float("inf")
            for val in freq.values():
                if val<mini:
                    mini=val
            beauty+=(maxi-mini)
    return beauty
def main():
    s=input("enter a string: ")
    print(beauty_sum(s))
if __name__=="__main__":
    main()






    


        
