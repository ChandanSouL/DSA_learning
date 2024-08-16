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
    
#3 method
def fibonacci_search(arr, x, n):
    # Initialize Fibonacci numbers
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci

    # fibM is going to store the smallest
    # Fibonacci Number greater than or equal to n
    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    # Marks the eliminated range from the front
    offset = -1

    # while there are elements to be inspected.
    # Note that we compare arr[fibMm2] with x.
    # When fibM becomes 1, fibMm2 becomes 0
    while fibM > 1:
        # Check if fibMm2 is a valid location
        i = min(offset + fibMMm2, n - 1)

        # If x is greater than the value at
        # index fibMm2, cut the subarray array
        # from offset to i
        if arr[i] < x:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        # If x is less than the value at
        # index fibMm2, cut the subarray
        # after i+1
        elif arr[i] > x:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        # element found. return index
        else:
            return i

    # comparing the last element with x
    if fibMMm1 and arr[n - 1] == x:
        return n - 1

    # element not found. return -1
    return -1