arr = [1,2,3,4,5,6]
n = len(arr)
def binarysearch(arr,low,high,key):
    if (high < low):
        return -1
    
    mid = high+low //2
    if (key == arr[mid]):
        return mid
        
    if (key > arr[mid]):
        return binarysearch(arr,mid+1,high,key)
    
    return binarysearch(arr,low,mid-1,key)
    
def deleteElement(arr, n, key):
    pos = binarysearch(arr,0,n-1,key)

    if pos == -1:
        print('no element')
        return n 
    
    for i in range(pos,n-1):
        arr[i] = arr[i+1]
        return n-1