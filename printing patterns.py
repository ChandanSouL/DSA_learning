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



#to inverse the same pattern
n = 5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('* ',end = ' ')
    print('')