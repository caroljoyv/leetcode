word1 = "abc"
word2 = "pqr"

res = ''
count =0
for i,j in zip(word1,word2):
    res += i
    res += j
    count += 1


if len(word1) == count:
    res += word2[count:]
else:
    res+= word1[count:]

print(res)