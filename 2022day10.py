with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]
    ans = 0
    c = 0
    X = 1
    for line in data:
        
        if line == 'noop':
            c += 1
            next_cycle = False
        else:
            V = int(line.split()[1])
            c += 1
            next_cycle = True
        if (c-20) % 40 == 0:
            ans += c*X
        if next_cycle:
            c += 1
            if (c-20) % 40 == 0:
                ans += c*X
            X += V
        if c > 220:
            break
    print(ans)

#part 2
with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

    def draw(X, c, row):
        if (c-1) in (X-1, X, X+1):
            CRT[row][c-1] = '#'
    c = 1
    X = 1
    ix = 0
    CRT = [['.' for i in range(40)] for i in range(6)]
    row = 0
    second = False
    while ix < len(data):
        if data[ix] == 'noop':
            draw(X, c, row)
            c += 1
            ix += 1
        else:
            draw(X, c, row)
            c += 1
            
            if second:
                second = False
                V = int(data[ix].split()[1])
                X += V
                ix += 1
            else:
                second = True
        if c > 40:
            c = 1
            row += 1
            if row > 5:
                break
    for i in CRT:
        print(''.join(i))
