with open('input.txt') as f:
    data = [[int(i) for i in line.strip()] for line in f.readlines()]
    H = len(data)-1
    W = len(data[0])-1
    ans = 0

    dp = [[[] for j in range(len(data))] for i in range(len(data))] #[left, top] #dps are 2d array of highest tree to the ___ and ___
    dp2 = [[[] for j in range(len(data))] for i in range(len(data))] #[right, bottom]
    dp[0][0] = [data[0][0], data[0][0]]
    dp2[H][W] = [data[-1][-1], data[-1][-1]]
    
    for row in range(H+1):
        for col in range(W+1):
            # if it is an edge: dp[row][col] = data[row][col]
            
            if row == 0:
                if col == 0:
                    continue
                dp[row][col] = [10, data[row][col]] # 10 is a placeholder as this value is never used
                dp2[H-row][W-col] = [10, data[H-row][W-col]]
            elif col == 0:
                dp[row][col] = [data[row][col], 10]
                dp2[H-row][W] = [data[H-row][W], 10]
            # if it is in middle:
            else:
                dp[row][col] = [max(dp[row][col-1][0], data[row][col-1]), max(dp[row-1][col][1], data[row-1][col])] 
                #dp of [row][col] = [max(dp[left] and data[left]), max(dp[up]data[up])]
                dp2[H-row][W-col] = [max(dp2[(H-row)][(W-col)+1][0], data[H-row][(W-col)+1]), max(dp2[(H-row)+1][(W-col)][1], data[(H-row)+1][W-col])]
                # dp2 is built up the opposite way (from bottom right corner)
                #dp2 of [row][col] = [max(dp2[right], data[right]), max(dp2[down], data[down])
    ans = 0
    for row in range(1, H):
        for col in range(1, W):
            valid = False
            for i in range(2): # check left and top
                if dp[row][col][i] < data[row][col]:
                    ans += 1
                    valid = True
                    break
            if not valid:
                for i in range(2): # check right and bottom
                    if dp2[row][col][i] < data[row][col]:
                        ans += 1
                        break
    H += 1
    W += 1
    print(ans+W*2+(H-2)*2)

    # lazyman's part 2 - probably could have used a function at least - might try dp ver later
    ans = 0
    for row in range(1, H):
        for col in range(1, W):
            c = 1
            j = 0
            for i in range(row-1, -1, -1):
                if data[i][col] >= data[row][col] or i == 0:
                    c *= (j+1)
                    break
                j += 1
            j = 0
            for i in range(row+1, H+1):
                if data[i][col] >= data[row][col] or i == H:
                    c *= (j+1)
                    break
                j += 1
            j = 0
            for i in range(col-1, -1, -1):
                if data[row][i] >= data[row][col] or i == 0:
                    c *= (j+1)
                    break
                j += 1
            j = 0
            for i in range(col+1, W+1):
                if data[row][i] >= data[row][col] or i == W:
                    c *= (j+1)
                    break
                j += 1
            ans = max(ans, c)
    print(ans)
