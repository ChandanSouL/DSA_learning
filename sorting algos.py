#selection sort
a = [64,25,12,22,11]
n = len(a)
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if a[min_index] > a[j]:
            min_index = j
    
    a[i],a[min_index] = a[min_index],a[i]
print ("Sorted array")
for i in range(len(a)):
    print(a[i],end=" ") 

#-----------------------------------------------------------------------------------------
#Bubble sort
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubblesort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

#----------------------------------------------------------------------------------------------
#insertion sort 
def insertionsort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j > 0 and arr[j] > key:
            arr[j+1] = arr[i]
            j -=1
        arr[j+1] = key 
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver method
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertionsort(arr)
    printArray(arr)
#--------------------------------------------------------------------------------------
# Merge sort
def merge_sort(arr):
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    #recurssive merge sort
    merge_sort(left_arr)
    merge_sort(right_arr)

    i= 0 #this is the index of left
    j = 0 #this is the index of right
    k = 0 #this is the index of the main arr

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i+=1
        else:
            arr[k] = right_arr[j]
            j+=1
        k+=1

    while i<len(left_arr):
        arr[k] = left_arr[i]
        i+=1
        k+=1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j+=1
        k+=1
    return arr

arr_test = [1,54,5642,21,5534,64,334,12,2,4,5]
print(merge_sort(arr_test))
 