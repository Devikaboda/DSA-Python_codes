r=4
c=7
'''for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
'''

'''for i in range(r):
    for j in range(i+1):
        print("#",end="")
    print()'''

'''for i in range(r):
    for j in range(c-i):
        print("#",end="")
    print()
'''
'''for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("#",end="")
        else:
            print(" ",end="")
    print()'''

'''for i in range(r):
    for j in range(r-1-i):
        print(" ",end="")
    for k in range(c):
        print("#",end="")
    print()
    '''
'''for i in range(r):
    for j in range(i):
        print(" ",end="")
    for k in range(c):
        print("#",end="")
    print()
'''
'''for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
'''
'''for i in range(r):
    for j in range(i):
        print(" ",end="")
    for k in range(2*r-1-(2*i)):
        print("#",end="")
    print()'''

'''for i in range(r):
    for j in range(r-1-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
for i in range(r):
    for j in range(i+1):
        print(" ",end="")
    for k in range(c-(2*i+2)):
        print("*",end="")
    print()'''



