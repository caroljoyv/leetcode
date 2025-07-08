# Approach 1
# 1. sort array
# 2. find the difference of consecutive elements
#     a. if difference == 1, increase right FloatingPointError
#     b. else increase left pointer

# time complexity: n log n
# space complexity: n(1)


def findLHS(nums:[int]) -> int:
        l = 0
        r = 1
        result = 0
        nums.sort()      

        while r < len(nums):
                difference = nums[r] - nums[l]

                if difference == 1:
                        result = max(result, r-l+1)  # lenght of the harmonious subsequence
                if difference <= 1:
                        r += 1 # increase window size
                else:
                        l += 1 # decrease window size
                    
       
        return result


print(findLHS([1,3,2,2,5,2,3,7]))
print(findLHS([1,2,3,4]))


# Approach 2: better one

# a. create a hashmap with value and frequency
# b. for each unique value, check if n+1 exists in the map
# c. if yes, max lenght = max of max_lenght and current lenght, where current length = freq of n + freq of n+1


# Time complexity: O(n)
# Space complexity: O(n)


from collections import Counter

def solutionUsingHashMaps(nums:[int]) -> int:
        max_length = 0
        frequencyMap = Counter(nums)

        for num in frequencyMap:
                if num+1 in frequencyMap:
                        current_length = frequencyMap[num] + frequencyMap[num+1]
                        max_length = max(max_length, current_length)
        return max_length


print(solutionUsingHashMaps([1,3,2,2,5,2,3,7]))
        