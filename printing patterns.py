#for half pyramid
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('* ',end = ' ')
    print('')
#instead of * print letters
#use num = 65 for capital Alphabets and num = 97 for small letters
#then convert num into chr datatype

#instead of * print numbers
#use nums =1 and increment nums at the end of ith loop
s = 65
n = 5
for i in range(1,n):
    for j in range(1,i+1):
        print(chr(s),end = ' ')
        s+=1
    print('')



#to inverse the same pattern
n = 5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('* ',end = ' ')
    print('')


#full pyramid


n = 7
for i in range(1,n+1):      #(n,0,-1)
    for j in range(n-i):
        print(" ",end = '')
    
    for k in range(1,2*i):  #(2*i-1)
        print("*",end = ' ')
    print(' ')



#printing alphabets

alpha = 65
n = 4
for i in range(0,n):
    print(" "*(n-i),end = ' ')
    
    for j in range(0,i+1):
        print(chr(alpha),end = ' ')
        alpha+=1 
    alpha = 65
    print('')