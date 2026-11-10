def best_choc(prices,window_size):
    current_total = sum(prices[0:window_size])
    best_total = current_total
    window_totals = [0] * (len(prices) - window_size + 1)

    for i in range(window_size, len(prices)):
        left_choc = prices[i - window_size]
        right_choc = prices[i]

        current_total = current_total - left_choc + right_choc

        window_totals[i - window_size + 1] = current_total

    return best_total

prices = [2, 1, 5, 1, 3, 2]
window_size = 3

result = best_choc(prices, window_size)

print(result)
