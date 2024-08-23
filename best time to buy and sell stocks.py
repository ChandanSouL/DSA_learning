prices = [10,1,5,6,7,1]
#output = 6
def buyandSellStocks(prices):
    res = 0
    lowest = prices[0] #assigning the first index as lowest
    for i in prices: #iteratin g through the list
        if i < lowest:  #comparing and assigning the lowest
            lowest = i
        res = max(res,i-lowest)  #getting the maximum of the result and getting the ouput
    return res


#two Chocolates
def twochocolates(prices,money):
    prices.sort()
    for i in range(len(prices)-1):
        if prices[i]+prices[i+1] <= money:
            return money - prices[i] - prices[i+1]
    return money

#Closest number to zero
def closestNumber(arr):
    closest = arr[0]
    for i in arr:
        if abs(i) < abs(closest):
            closest = i
        if closest < 0 and abs(closest) in arr:    #if -1 and 1 are then we need to return 1 because it will be maximum between -1 and 1
            return abs(closest)
        else:
            return closest
        
#longest common prefix
def longestcommonprefix(strs):
    ans = ""
    first, last = strs[0], strs[-1]
    if len(first) != 0:
        i=0
        while i < len(first) and first[i] == last[i]:
            ans+=first[i]
            i+=1
    return ans

#issubsquence
def subsquence(word1,word2):
    i = 0
    j = 0
    while i < len(word1) and j < len(word2):
        if word1[i] == word2[j]:
            i+=1
        j+=1
    return i==len(word1)

