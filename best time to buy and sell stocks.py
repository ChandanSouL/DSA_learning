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