jewels = "aA"
stones = "aAAbbbb"

count = 0
for i in jewels:
    for j in stones:
        if i == j:
            count += 1
print(count)

