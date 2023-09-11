def remove(arr):
    l = len(arr)
    arr.sort()
    duplicates = set()

    for i in range(l):
        if i == l-1:
            break
        if arr[i] == arr[i+1]:
            duplicates.add(arr[i])

    return list(duplicates)

answer = remove([2,7,3,4,2,7])
print(f"The duplicates are: {answer}")