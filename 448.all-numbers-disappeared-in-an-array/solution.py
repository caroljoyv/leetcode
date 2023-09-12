def find(nums):
    # n = len(nums)
    # array = list(range(1,n+1))
    # new_nums = list(set(nums))
    # ans = []
    # for i in array:
    #     if i not in new_nums:
    #         ans.append(i)

    n = len(nums)
    nums_set = set(nums)
    array_set = set(range(1,n+1))
    ans = list(array_set - nums_set)


    return ans



    

ans = find([4,3,2,7,8,2,3,1])
print(f"Answer = {ans}")