def find(nums,target):
    ans = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                ans.append(i)
                ans.append(j)
                return ans

nums = [3,2,4]
target = 6
print(find(nums, target))