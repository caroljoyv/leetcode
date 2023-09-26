nums = [2,3,1,1,4]

def find(nums):
    goal = len(nums)-1
    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] == goal:
            goal = i
    return True if goal == 0 else False

print(find(nums))