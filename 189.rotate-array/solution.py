def find(nums):
    k = 3
    slice = nums[:-k%len(nums)]
    print(slice)

    # for i in range(len(nums)-k,-1,-1):
    #     nums[i+(k-1)] = nums[i-1]
    # print(nums)
    # for i in range(0,k):
    #     nums[i] = slice[i]
    # print(nums)


    # for ind, val in enumerate(nums[:k+1]):
    #     ind = ind+k
    #     nums[ind] = val
    # print(nums)
    # for i in range(0,k):
    #     nums[i] = slice[i]
    # print(nums)
find([1,2,3,4,5,6,7])