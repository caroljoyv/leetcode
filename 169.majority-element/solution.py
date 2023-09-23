nums = [3,3,4]

max_count = 0


for i in list(set(nums)):

    if max_count < nums.count(i):
        maj_element = i
        max_count = nums.count(i)



print(maj_element)
