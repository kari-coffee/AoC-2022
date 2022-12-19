with open('input2.txt') as f:
    data = list(f.read())

chamber = [[1 for i in range(7)]]+[[0 for i in range(7)] for j in range(3)] #floor
rocks = [[(2,-1),(3,-1),(4,-1),(5,-1)], [(3,-1),(2,-2),(3,-2),(4,-2),(3,-3)], [(2,-3),(3,-3),(4,-3),(4,-1),(4,-2)], [(2,-1),(2,-2),(2,-3),(2,-4)], [(2,-1),(3,-1),(2,-2),(3,-2)]]
heights = [1, 3, 3, 4, 2]


c = 0
for k in range(2022):
    rest = False
    rock = rocks[k%5]
    empty = chamber.count([0 for m in range(7)])
    while empty > heights[k%5]+3:
        chamber.pop()
        empty -= 1
    for l in range(heights[k%5]+3-empty):
        chamber.append([0 for _ in range(7)])
    i = 0
    while not rest:
        display = [[1 for b in range(7)]] + [[0 for n in range(7)] for v in range(len(chamber)-1)]
        if i % 2 == 0: #pushed
            if data[c%len(data)] == '>':
                x = 1
            else:
                x = -1
            new = [(rock[j][0]+x, rock[j][1]) for j in range(len(rock))]
            valid = True
            for j in range(len(new)):
                if new[j][0] >= 7 or new[j][0] < 0 or chamber[new[j][1]][new[j][0]]:
                    valid = False
                    break
            if valid:
                rock = new
            else:
                pass
            c += 1
        else: #falls
            new = [(rock[j][0], rock[j][1]-1) for j in range(len(rock))]
            valid = True
            for j in range(len(new)):
                if chamber[new[j][1]][new[j][0]] == 1:
                    valid = False
                    break
            if valid:
                rock = new
            else:
                rest = True
                break
        for x,y in rock:
            display[y][x] = 1
        # for m in display:
        #     print(m)
        # print('\n')
        i += 1
    for x,y in rock:
        chamber[y][x] = 1
print(len(chamber)-4)
 
