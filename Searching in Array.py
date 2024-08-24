#Searching in Array has 3 methods
#Brute force method using for loop
#Using recurssion and Binary search 
#fibonnaci 


#1 method
def findElement(arr, n, key):
    for i in range(n):
        if (arr[i] == key):
            return i

    # If the key is not found
    return -1

#2 method
def binary_search(arr, start, end, key):
    
    # if case is evaluated when element is found else -1 is returned
    if (start < end):
        mid = (start + end) //2

        if (key == arr[mid]):
            return mid
        
        if (key < arr[mid]):
            return binary_search(arr, start, mid - 1, key)
        
        if (key > arr[mid]):
            return binary_search(arr, mid + 1, end, key)
    
    else:
        return -1
#using recurssion calling the function again with mid as end point allows you to reduce time complexity
    
#fiboncci series

def fibinocci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    while n >=2:
        return fibinocci(n-1)+fibinocci(n-2)