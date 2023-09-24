prices = [7,1,3,5,6,4]

profit = 0
buy = prices[0]
for i in prices[1:]:
    if i > buy:
        profit =  max(profit,i - buy)
    else:
        buy = i

print(profit)


