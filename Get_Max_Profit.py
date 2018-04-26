'''

Given an array of stock prices at different times during a day like such:
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
Find the greatest profit or least loss if there is no profit possible

'''

def get_max_profit(stock_prices):


    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')
        
    low = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for value in range(1, len(stock_prices)):
        
        max_profit = max(max_profit,(stock_prices[value]-low))
        
        low = min(low, stock_prices[value])

        
    return max_profit

