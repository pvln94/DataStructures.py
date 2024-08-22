def fractional_knapsack(values, weights, capacity):
    n = len(values)
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(n)]
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    print(items)
    total_value = 0.0
    fractions = [0] * n

    for i in range(n):
        if capacity == 0:
            break
        value, weight, ratio = items[i]
        if weight <= capacity:
            fractions[i] = 1
            capacity -= weight
            total_value += value
        else:
            fractions[i] = capacity / weight
            total_value += value * fractions[i]
            capacity = 0

    return total_value, fractions

# Example usage
values = [25,24,15]
weights = [18,15,10]
capacity = 20
total_value, fractions = fractional_knapsack(values, weights, capacity)

print("Maximum value in knapsack =", total_value)
print("Fractions of items included:")
for i in range(len(values)):
    print(f"x{i} = {fractions[i]}")

