#Recursive method
def binarysearch(arr,low,high,x):
    if low < high:
        mid = low+ (high-low) //2
        if arr[mid] == x:
            return mid
        
        if (x > arr[mid]):
            return binarysearch(arr,mid+1,high,x)
        
        else:
            return binarysearch(arr,low,mid-1,x)
    else:
        return -1
    
#iterative method
def binaryiterativesearch(arr,high,low,x):
    while high >= low:
        mid = low + (high-low) //2
        if arr(mid) == x:
            return mid
        elif x > arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1
        