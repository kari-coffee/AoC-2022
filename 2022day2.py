with open('temp.txt') as f:
    data = f.readlines()
    score = 0
    d = {'A':1, 'B':2, 'C':3, 'X':1,'Y':2,'Z':3}
    for line in data:
        a, b = line.split()
        x = d[a]
        y = d[b]
        if x == y:
            score += y + 3
        elif (x,y) in [(1,3), (3,2), (2,1)]:
            score += y
        else:
            score += y + 6
    print(score)

with open('temp.txt') as f:
    data = f.readlines()
    score = 0
    d = {'A':1, 'B':2, 'C':3}
    lose = {1:3,2:1,3:2}
    win = {3:1,1:2,2:3}
    for line in data:
        a, b = line.split()
        x = d[a]
        if b == 'X': #lose
            score += lose[x]
        elif b == 'Y': #draw
            score += x + 3
        else: #win
            score += win[x]+ 6
    print(score)
    