nums = [3,2,2,3]
val = 3

for i in range(nums.count(val)):
    nums.remove(val)
print(len(nums))
print(nums)