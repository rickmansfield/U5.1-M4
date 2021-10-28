"""
This version avoids nested loops and quadratic
time complexity. 
I researched built in methods and found min() & max()
- set initial values for minimum price and max profit at zero
- loop over prices
    - set min price using min() on price and min-price to use in next calculation
    - set max profit using max() on max profit vs price - min price
-return max profit 
"""
import math
import builtins
print(help(min))
print(help(max))
def buyAndSellStock(prices):
    max_profit, min_price = 0, float("inf")
    for price in prices: 
        min_price = min(price, min_price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

print(buyAndSellStock([6, 3, 1, 2, 5, 4]))
print(buyAndSellStock([8, 5, 3, 1]))
print(buyAndSellStock([3, 100, 1, 97]))