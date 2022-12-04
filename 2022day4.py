with open('temp.txt') as f:
    data = [line.strip() for line in f.readlines()]
    c = 0
    for line in data:
        a, b = line.split(',')
        a1, a2 = [int(i) for i in a.split('-')]
        b1, b2 = [int(i) for i in b.split('-')]
        if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
            c += 1
    print(c)

with open('temp.txt') as f:
    data = [line.strip() for line in f.readlines()]
    c = 0
    for line in data:
        a, b = line.split(',')
        a1, a2 = [int(i) for i in a.split('-')]
        b1, b2 = [int(i) for i in b.split('-')]
        if a1 in range(b1,b2+1) or a2 in range(b1,b2+1) or b1 in range(a1,a2+1) or b2 in range(a1,a2+1):
            c += 1
    print(c)