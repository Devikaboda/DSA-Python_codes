
'''list=[50,45,67,93,12]


for i,j in enumerate(list):
    print(i,j)



list=sorted(list)
print(list)
list=sorted(list,reverse=True)
print(list)
sort method is efficient than sorted function
list.sort()
print(list)
list.sort(reverse=True)
print(list)


list1=[89,78,90,45,67]
l=list(reversed(list1))
print(l)
list1.reverse()
print(list1)'''

#programm to find sum of sublist

'''l=input("enter a list of numbers between []\n")
print(l)
l=eval(l)
start=int(input("enter start index"))
stop=int(input("enter the stop index"))
print("sum=",sum(l[start:stop+1:]))'''




#programm to insert an element at right position of sorted list
'''lst=(input("enter a sorted list[ ]\n"))
l=list(map(int, lst.split(',')))
n=int(input("enter the number to be inserted:"))
for i in range(len(l)):
    if n<l[i]:
        l.insert(i,n)
        break
print(l)  '''

#min-max sum
'''lst=[4,3,8,5,1]
total=sum(lst)
print(total)
mi=total-max(lst)
mx=total-min(lst)
print("min=",mi)
print("max=",mx)'''


#programm to check whether the expression contains balanaced parenthesis or not
'''s=list(input("enter an expression within brackets[ ]\n"))
li=[]
for i in s:
    if i=='[' or i=='{' or i=='(':
        li.append(i)
    elif i in [']',')','}']:
        if not li:
            li.append(i)
            break
        elif i==']' and li[-1]=='[':
            li.pop()
        elif i=='}' and li[-1]=='{':
            li.pop()
        elif i==')' and li[-1]=='(':
            li.pop()
        else:
            break
if len(li)==0:
    print("balanaced parenthesis")
else:
    print("unbalanced parenthesis") '''


#string comparison
'''lst1=[1,2,3]
lst2=[4,5,6,7]
l=[4,5,6,7,8]
print(lst1>lst2)
print(lst2>lst1)
print(lst2>l)'''


# STRING COMPREHENSION topic
#TRADITIONAL APPROACH
'''lst=[1,2,3,4]
sq_lst=[]
for i in lst:
    sq_lst.append(i**2)
print(sq_lst)
'''
#use of comprehension for above code
'''lst=[1,2,3,4]
sq=[i**2 for i in lst ]
print(sq)'''


#zip() function
'''l1=[1,2,3,4,]
l2=[5,6,7,8]
for i,j in zip(l1,l2):
    print(i,j)'''

#ANOTHER EXAMPLE
'''l1=['app','i','goo']
l2=['le ','s ','d ']
res=[]
for i,j in zip(l1,l2):
    res.append(i+j)
print(' '.join(res))'''

      # USING LIST COMPREHENSION
'''l1=['app','i','goo']
l2=['le ','s ','d ']
res=[i+j for i,j in zip(l1,l2)]
print(''.join(res))'''


#PROGRAM: TAKE INPUT STRING FROM THE USER AND IF THE LENGTH OF THE WORD BASED ON SOME CONDITION
'''s=input("enter s string : ").split()
res=[]
for i in s:
    if len(i)>5:
        res.append(i.lower())
    else:
        res.append(i.upper())
print(" ".join(res))'''

#using list comprehension

'''s=input("enter a string: ").split()
print(" ".join(i.lower() if len(i)>5  else i.upper() for i in s))'''


# all() and any() FUNCTIONS
'''lst=[12,79,85,67,34]
print(all([i>35 for i in lst]))
print(any([i>35 for i in lst]))'''

#tuple
'''tup=(10)
print(tup)
print(type(tup))



tup=(10,)
print(tup)
print(type(tup))'''

tup=(10,[20,30,40],True,19.5)
print(tup)
print(tup[2])












    


        




        





 
 
