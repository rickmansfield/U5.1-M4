    """
    WARNING... 
    this code will work in real life perfectly. BUT...
    it will NOT PASS CodeSignal grading due to a nasty 
    4 second time constraint. The constraint is there
    to force the student to find a way other than nested
    loops (resulting in quadratic time complexity) to solve
    the problem. 
    """
def buyAndSellStock(prices):
    profitLossList = []
    for eachLHNumber in range(len(prices)):
        for eachRHNumber in range(eachLHNumber + 1, len(prices)):
            profit = (prices[eachRHNumber] - prices[eachLHNumber])
            profitLossList.append(profit)
    profitsSorted =  sorted(profitLossList)
    print(profitsSorted)
    if profitsSorted == []:
        return 0
    maxProfits = profitsSorted.pop()
    if maxProfits  < 0 or maxProfits  == []:
        return 0 
    else:
        return maxProfits 

print(buyAndSellStock([6, 3, 1, 2, 5, 4]))
print(buyAndSellStock([8, 5, 3, 1]))
print(buyAndSellStock([3, 100, 1, 97]))
