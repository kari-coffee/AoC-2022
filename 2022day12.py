with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]
    H = len(data)
    W = len(data[0])
    grid = [['' for i in range(W)] for j in range(H)]
    
    #with part 2 bits
    poss = []
    for row in range(H):
        for col in range(W):
            if data[row][col] == 'S':
                start = [col, row]
            elif data[row][col] == 'a':
                poss.append([col, row, 0])
            grid[row][col] = data[row][col]
    
    queue = [[start[0], start[1], 0]] + poss
    visited = set()
    stop = False
    while queue and not stop:
        x, y, steps = queue.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if 0 <= x+dx < W and 0 <= y+dy < H and (x+dx, y+dy) not in visited:
                next = grid[y+dy][x+dx]
                cur = grid[y][x]
                if cur != 'E':
                    visited.add((x, y))
                if next == 'E' and cur == 'z':
                    print(steps+1)
                    stop = True
                    break
                
                elif (ord(next)-ord(cur) <= 1 or cur == 'S') and ([x+dx, y+dy, steps+1] not in queue):
                    queue.append([x+dx, y+dy, steps+1])
                    
