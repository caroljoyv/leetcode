nums = [1,1,1,1,1,1,1]
if nums == len(nums) * [1]:
    print("Huurryy!!")


grid = [[2,1,1],[0,1,1],[1,0,1]]
print(grid[0].index(2))

for i in grid:
    for j in i:
        print(j, end = "")
    print()


# for i in grid:
#     top = grid.index(i) - 1
#     bottom = grid.index(i) + 1
#     for j in i:
#         left = i.index(j) - 1
#         right = i.index(j) + 1
        
#         print(top, bottom, left, right, end = "     ")
#     print()

count = 0
for i in grid:
    count += 1
print(count)


def makeRotten(val,count):
    
    min = 0
    for i in range(count):
        for j in range(len(grid[i])):
        
            if grid[i][j] == 2 and j+1 < len(grid[i]) and grid[i][j+1] != 0:
                grid[i][j + 1] = 2  # make right rotten
                min += 1
                makeRotten(grid[i][j + 1],count)
            elif grid[i][j] == 2 and j-1 >= 0 and grid[i][j-1] != 0:
                grid[i][j-1] = 2    # make left rotten
                min += 1
                makeRotten(grid[i][j - 1],count)
            elif grid[i][j] == 2 and i+1 < count and grid[i+1][j] != 0:
                grid[i+1][j] = 2    # make bottom rotten
                min += 1
                makeRotten(grid[i+1][j],count)
            elif grid[i][j] == 2 and i-1 >= 0 and grid[i-1][j] != 0:
                grid[i-1][j] = 2    # make top rotten
                min += 1
                makeRotten(grid[i-1][j],count)


for i in grid:
    for j in i:
        if j == 1:
            print(-1) 
            break
        
