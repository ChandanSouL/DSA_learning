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
def subsquence(word,word2):
    i = 0
    j = 0
    while i < len(word) and j < len(word2):
        if word[i] == word2[j]:
            i+=1
        j+=1
    return i==len(word)

#longest common prefix
def longestCommonPrefix(strs):
        ans = ''
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        if len(first) !=0:
            i = 0
            while i < len(first) and first[i] == last[i]:
                ans+=first[i]
                i+=1
        return ans

#merge strings alternatively
def mergeAlternately(self, word1: str, word2: str) -> str:
    ans = ''
    i=0
    j=0
    while i<len(word1) and j < len(word2):
        ans+=word1[i]
        ans+=word2[j]
        i+=1
        j+=1
    if i==(len(word1)) and j!=len(word2):
        for k in range(j,len(word2)):
            ans+=word2[k]
    if j==(len(word2)) and i!=len(word1):
        for k in range(i,len(word1)):
            ans+=word1[k]
    return ans

#reverse a prefix of the word
def reverseprefix(word,ch):
    if ch in word:
        index = word.find(ch)
        return word[0:index+1][::-1] + word[index+1:]
    return word

#Find if the words can be order in ascending
usernames = 'a'
n = len(usernames)
res = []
no = 'NO'
yes = 'YES'
can_rearrange = no

for i in range(n-1):
    if usernames[i] > usernames[i + 1]:
        can_rearrange = yes
        break

print(can_rearrange)
