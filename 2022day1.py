#part 1
with open('temp.txt') as f:
    data = f.readlines()
    res = 0
    c = 0
    for line in data:
        if line == '\n':
            res = max(res, c)
            c = 0
        else:
            c += int(line)
    print(res)

#part 2
with open('temp.txt') as f:
    data = f.readlines()
    snacks = [0 for i in range(10000)]
    i = 0
    for line in data:
        if line == '\n':
            i += 1
        else:
            snacks[i] += int(line)
        
    res = 0
    for i in range(3):
        res += max(snacks)
        snacks.remove(max(snacks))
    print(res)