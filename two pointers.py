#given array find the two numbers whose sum add up to K
#example nums = [1,2,3,4,5,6] k = 11 return 5,6
def twoPointers(nums,k):
    i = 0
    n = len(nums)
    j = n-1
    while i < j:
        if nums[i] + nums[j] ==k:
            return nums[i],[j]
        elif nums[i] + nums[j] < k:
            i+=1
        else:
            j-=1
        return -1