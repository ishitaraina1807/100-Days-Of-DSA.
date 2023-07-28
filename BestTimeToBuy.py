prices = [2,4,1,3,5]

if len(prices) < 2:
    profit = 0
else:
    buy = prices[0]
    sell = 0

    for i in prices[1:]:
        if i < buy:
            buy = i
        else:
            current_profit = i - buy
            max_profit = max(sell, current_profit)

    profit = max_profit

print(profit)  
