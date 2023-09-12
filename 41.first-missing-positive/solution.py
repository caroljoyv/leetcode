def find(nums):

    # find the missing numbers
    # a = set(range(1,max(nums)+1)) - set(nums)
    # print(a)

    # #if there are no missing numbers
    # if len(a) == 0:
    #     return max(nums) + 1
    
    # else:
    #     # finding the smallest +ve number, remove the -ve umbers first
    #     return  min(a)



    nums_set, i = set(nums), 1
    while i in nums_set:
        i += 1
    return i
ans = find([0])
print(f"Answer is {ans}")

# find([1,2,0])