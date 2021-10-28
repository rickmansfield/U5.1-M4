"""
This version of my code helps the reader understand
how I arrived at this particular solution. 
But got to file /Task5clean.py to see the
final version that works perfectly. 

- initiate an empty list set it to a variable profit/loss to capture numbers
- iterate/loop over the "prices" list
    - for each price subtract it from all other prices and store each result in the profit/loss list. 
    -sort the final list 
    return the last profit number on the list as it is the "greatest" profit number on the list. 
"""
prices1 =  [6, 3, 1, 2, 5, 4] # 4
prices2 = [8, 5, 3, 1] # 0
prices3 = [3, 100, 1, 97] # 97

def buyAndSellStock(prices):
    profitLossList = []
    # priceToProfDict = {}
    for eachLHNumber in range(len(prices)):
        # print("---------LHN---------")
        # print(prices[eachLHNumber])
        for eachRHNumber in range(eachLHNumber + 1, len(prices)):
            # print("------RHN-------")
            # print(prices[eachRHNumber])
            profit = (prices[eachRHNumber] - prices[eachLHNumber])
            # print("--------profit------")
            # print(profit)
            profitLossList.append(profit)
            # priceToProfDict[prices[eachRHNumber]] = profit
    # print(profitLossList)
        # print(priceToProfDict)
    profitsSorted =  sorted(profitLossList)
    # print(profitsSorted)
    maxProfit = profitsSorted[-1]
    if maxProfit < 0:
        return 0 
    else:
        return maxProfit

print(buyAndSellStock(prices1))
print(buyAndSellStock(prices2))
print(buyAndSellStock(prices3))
