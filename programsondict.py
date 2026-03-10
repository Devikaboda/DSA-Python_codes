'''d={1:'a','two':'b',3:'c'}
print(d)
print(d['two'])
print(26 in d)
d.update({4:'g',5:'7'})
print(d)
d.pop(5)
print(d)
d.popitem()
print(d)
del d[3]
print(d)
print(d.clear())'''


# special case
'''d={1: 'a', 'two': 'b', 3: 'c', 4: 'g', 5: '7'}
print(d.pop(6,"not found"))
d.clear()
print(d)'''

#accessing the dictionary

'''d={1: 'a', 'two': 'b', 3: 'c', 4: 'g', 5: '7'}
for i in d.keys():
    print(i)
print("\n")
for i in d.values():
    print(i)
print("\n")
for i in d.items():
    print(i)'''

#programm to count the number of occurenences of each character in given string
'''s=input("enter  a string: ")
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)'''

#programm to count the total number of pairs 
'''s=(map(int,input(" ").split()))
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
res=0
for i in d.values():
    res=res+i//2
print(res)'''

#programm to print mobile number associated with the name if the name is not among the display not found.
'''n=int(input("enter the number of contacts: "))
d={}
for i in range(n):
    l=input().split()
    d[l[0].lower()]=l[1]
s=int(input("enter the number of chances: "))
for i in range(s):
    name=input().lower()
    if name in d.keys():
        print("mob:",d[name])
    else:
        print("contact not found")'''


#programm to print the kth non repeating charcater in the given string.
'''s=input("enter a string: ").lower()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
k=int(input("enter the k th non repeating charcter you want: "))
count=0
for i in d:
    if d[i]==1:
        count+=1
        if count==k:
            print(i)
            break'''



# to count the occurence of each word in given sentence print the occurence ofword,
#   whose count is greater than 3
'''import re
sen=input("enter the sentence: ").lower()
sen=re.sub(r'[,.?:]'," ",sen)
lst=sen.split()
d={}
for i in lst:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if d[i]>=3:
        print(i,d[i])'''

#remove the duplicate keys and only return the keys with high value they score.


'''lst=input().split(",")
d={}
for i in lst:
    t=i.split()
    if t[0] not in d:
        d[t[0]]=t[1]
    else:
        if t[1]>d[t[0]]:
            d[t[0]]=t[1]
print(d)'''

#program to inverse dictionary such that keys become values and vice versa.
    
'''d={1:'a',2:'b',3:'c',4:'a',5:'b',6:'a'}
res={}
for i in d:
    if d[i] not in res:
        res[d[i]]=[]
        res[d[i]].append(i)
    else:
        res[d[i]].append(i)
print(res)'''

#programm to kept the words in sentence in order.


'''sen=input("enter a sentence: ").lower().split()
d={}
for i in sen:
    if len(i) not in d:
        d[len(i)]=[]
        d[len(i)].append(i)

    else:
        d[len(i)].append(i)
s_d=sorted(d.keys(),reverse=True)
for i in s_d:
    for j in sorted(d[i]):
         print(j)'''

#dictionary comprehension:
lst=input().split()
d={i:len(i) for i in lst }   
print(d)

       
    
    
    
    

    




