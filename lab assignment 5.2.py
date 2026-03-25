prices = tuple(map(int, input("Enter prices separated by space: ").split()))

print("Total items sold:", len(prices))
print("Cheapest price:", min(prices))
print("Costliest price:", max(prices))
print("Prices in ascending order:", tuple(sorted(prices)))

costliest = max(prices)
count = prices.count(costliest)
print("Number of costliest items sold:", count)