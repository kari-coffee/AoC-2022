with open('input2.txt') as f:
    data = [[[int(i) for i in coord.split(',')] for coord in line.strip().split(' -> ')] for line in f.readlines()]
    hh = 0
    lw = 0
    hw = 0
    for line in data:
        for x, y in line:
            if y > hh: hh = y
            if x < lw or lw == 0: lw = x
            if x > hw: hw = x
    grid = [['.' for i in range(lw, hw+1)] for j in range(hh+1)]
    for line in data:
        for i in range(len(line)-1):
            start = line[i]
            end = line[i+1]
            x, y = min(start[0], end[0]), min(start[1], end[1])
            if start[0]-end[0] != 0:
                #horizontal
                for length in range(max(start[0], end[0])-min(start[0], end[0])+1):
                    grid[y][x-lw+length] = '#'
            else:
                #vertical
                for length in range(max(start[1], end[1])-min(start[1], end[1])+1):
                    grid[y+length][x-lw] = '#'
    for i in grid:
        print(*i)
    
    ans = 0
    void = False
    while not void:
        rest = False
        x, y = 500-lw, 0
        while not rest:
            if y == len(grid):
                void = True
                break
            if grid[y+1][x] != '.' or x < 0 or x > len(grid[0]):
                if grid[y+1][x-1] != '.' and x-1 >= 0:
                    if x+1 < len(grid):
                        if grid[y+1][x+1] != '.':
                            rest = True
                        else:
                            if y == len(grid)-2:
                                void = True
                                break
                            x += 1
                            y += 1
                else:
                    if y == len(grid)-2:
                        void = True
                        break
                    y += 1
                    x -= 1
            else:
                if y == len(grid)-2:
                    void = True
                    break
                y += 1
        grid[y][x] = 'o'
        ans += 1
    print(ans-1)
    # for i in grid:
    #     print(*i)

with open('input2.txt') as f:
    data = [[[int(i) for i in coord.split(',')] for coord in line.strip().split(' -> ')] for line in f.readlines()]
    hh = 0
    lw = 0
    hw = 0
    for line in data:
        for x, y in line:
            if y > hh: hh = y
            if x < lw or lw == 0: lw = x
            if x > hw: hw = x
    grid = {(x, y): '.' for x in range(lw-500, hw+50) for y in range(hh+3)}
    for line in data:
        for i in range(len(line)-1):
            start = line[i]
            end = line[i+1]
            x, y = min(start[0], end[0]), min(start[1], end[1])
            if start[0]-end[0] != 0:
                #horizontal
                for length in range(max(start[0], end[0])-min(start[0], end[0])+1):
                    grid[(x+length, y)] = '#'
            else:
                #vertical
                for length in range(max(start[1], end[1])-min(start[1], end[1])+1):
                    grid[(x, y+length)] = '#'
    for x in range(lw-500, hw+500):
        grid[(x, hh+2)] = '#'
    
    ans = 0
    blocked = False
    while not blocked:
        rest = False
        x, y = 500, 0
        while not rest:
            if grid[(x, y+1)] != '.':
                if (x-1, y+1) not in grid:
                    grid[(x-1, y+1)] = '.'
                if grid[(x-1, y+1)] != '.':
                    if (x+1, y+1) not in grid:
                        grid[(x+1, y+1)] = '.'
                    if grid[(x+1, y+1)] != '.':
                        rest = True
                    else:
                        x += 1
                        y += 1
                else:
                    y += 1
                    x -= 1
            else:
                y += 1
        grid[(x, y)] = 'o'
        if (x, y) == (500, 0):
            blocked = True
            break
        ans += 1
    print(ans+1)
