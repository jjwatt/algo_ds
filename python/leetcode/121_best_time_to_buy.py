def max_profit(prices):
    if not prices:
        return 0
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)  # Update min price if a lower price is found
        max_profit = max(max_profit, price - min_price)  # Update max_profit
    return max_profit
