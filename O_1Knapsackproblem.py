def knapsack(values, weights, capacity):
    n = len(values)
    # Create a 2D DP array with (n+1) rows and (capacity+1) columns
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    
    # Build the DP array
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    print(dp)            
    
    # To find the items included, we can backtrack from dp[n][capacity]
    included_items = [0] * n
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            included_items[i-1] = 1  # Item i-1 is included
            w -= weights[i-1]

    return dp[n][capacity], included_items

# Example usage
values = [1, 2, 5, 6]
weights = [2, 3, 4, 5]
capacity = 8
max_value, included_items = knapsack(values, weights, capacity)
print("Maximum value in knapsack =", max_value)
print("Items included in the knapsack (0's and 1's):", included_items)
