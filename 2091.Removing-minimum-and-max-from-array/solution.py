def find(nums):
    
    min_ind = nums.index(min(nums))
    max_ind = nums.index(max(nums))
    mid_ind = len(nums) // 2

    if min_ind < mid_ind and max_ind < mid_ind:  #case 1
        return max(min_ind,max_ind)+1

    elif min_ind >= mid_ind and max_ind >= mid_ind: # case 2
        
        reversed_arr = nums[::-1]  #reversing the array
        reversed_min = reversed_arr.index(min(reversed_arr))
        reversed_max = reversed_arr.index(max(reversed_arr))
        return max(reversed_max,reversed_min)+1
        
    elif min_ind >= mid_ind and max_ind < mid_ind: # case 4
        #index from back
        if min_ind == mid_ind:
            return min_ind +1
        reversed_arr = nums[::-1]  #reversing the array
        reversed_min = reversed_arr.index(min(reversed_arr))

        return max_ind+1+reversed_min+1
        
    else: #case 3
        if max_ind == mid_ind:
            return max_ind +1
        reversed_arr = nums[::-1]  #reversing the array
        reversed_max = reversed_arr.index(max(reversed_arr))

        return min_ind+1+reversed_max+1
    

arr =[-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28]
ans = find(arr)

print(f"Minimum number of deletions = {ans} ")



    



