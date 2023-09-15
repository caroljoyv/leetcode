def find(nums):
        new_arr = list(set(nums))
        nums[:] = sorted(new_arr)[:]
        return len(new_arr)


ans = find([1,2,2,2,3,4,4,])
