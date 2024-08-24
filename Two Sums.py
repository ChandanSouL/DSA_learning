#two sums
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Brute Force Approach
#using two for loops to find the i'th and j'th number.
#adding them to get the target and return the list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

#Using HAshmaps to reduce the for loops
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in nmap:
                return [nmap[complement],i]
            nmap[n] = i
#take a way from this is when using 2nd loop always use Hashmap, Hashmap is a like a Dictionary assigning I with every loop
#if the list is [2,7,13,11] then Hashmap will be like this
#{2: 0, 7: 1, 13: 2, 11: 3}

#palindrome number
def palindrome(n):
    y = str(n)
    if y == y[::-1]:
        return True
    else:
        return False
