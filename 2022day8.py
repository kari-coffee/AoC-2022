with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]
    H = len(data)
    W = len(data[0])
    ans = 0
    dp = [] #[left, top] #dps are 2d array of highest tree to the ___ and ___
    dp2 = [] #[right, bottom]
    for row in range(1, H-1):
        for col in range(1, W-1):
            if row == 0:
                dp[row, col] = 
            dp[row, col] = [max(data[row-1], dp[row-1]), max(data[col-1], dp[col-1])]
            dp2[H-row, W-col] = [max(data[(H-row)+1], dp[(H-row)+1]), max(data[(W-col)+1], dp[(W-col)+1])]
