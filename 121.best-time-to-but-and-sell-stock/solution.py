prices = [1,2]

min_ind = prices.index(min(prices))
print(min_ind)

profit = 0
max_ind = 0

for i in range(min_ind+1, len(prices)):
    if prices[i] - prices[min_ind] > profit:
        profit = prices[i] - prices[min_ind]
        max_ind = i

if max_ind > 0:
    print(max_ind+1)
else:
    print(max_ind)


