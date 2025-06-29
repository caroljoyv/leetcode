## Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

def findMaxAverage(nums, k): # this approach fails for edge cases 
    n = len(nums)
    l = 0
    r = l+k
    # maxAvg = 0 this initialization fails for the case when nums = [-1] and k = 1
    maxAvg = float('-inf')  # Initialize to negative infinity to handle all cases

    while r <= n:
        avgValue = sum(nums[l:r])/k
        maxAvg = max(maxAvg, avgValue)
        l += 1
        r += 1
    return maxAvg

print(findMaxAverage([1], 1))  # Output: 12.75


def findMaxAverageOptimum(nums: [int], k: int)-> float: ## correct solution
    s = sum(nums[:k])
    maxSum = s

    for i in range(k, len(nums)):
        s += nums[i] - nums[i-k]
        maxSum = max(s, maxSum)
    return maxSum/k

print(findMaxAverageOptimum([1,12,-5,-6,50,3],4))