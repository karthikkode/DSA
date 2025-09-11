def maxProfit(prices):
    min_price = prices[0]
    profit = 0
    for i in range(0, len(prices)):
        if prices[i] < min_price:
            min_price=prices[i]
        curr_profit = prices[i] - min_price
        if curr_profit > profit:
            profit = curr_profit
    
    return profit
