with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

    sizes = {}
    path = []

    for line in data:
        if line[0] == '$':
            if line == '$ ls':
                continue
            elif line == '$ cd ..':
                path.pop()
            else:
                path.append(line[5:])
                sizes['/'.join(path)] = 0
        elif line.split()[0].isdigit():
            size, name = line.split()
            temp = [i for i in path]
            while temp:
                sizes['/'.join(temp)] += int(size)
                temp.pop()
    print(sizes)
    ans = sum([size for size in sizes.values() if size <= 100000])
    print(ans)

    #part 2
    free = 70000000 - sizes['/']
    needed = 30000000-free
    sizes = sorted(list(sizes.values()))
    for i in sizes:
        if i > needed:
            print(i)
            break
