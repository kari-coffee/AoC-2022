from functools import lru_cache

with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]

    dirs_in = {'/':[]}
    dirs_up = {}
    sizes = {}
    current = ''
    for line in data:
        if '$ cd' in line:
            if line[5] == '.':
                if current != '/':
                    current = dirs_up[current]
            elif line[5] == '/':
                current = '/'
            else:
                current = line[5:]
        elif line[:3] == 'dir':
            dirs_up[line[4:]] = current
            if current in dirs_in:
                dirs_in[current].append(line[4:])
            else:
                dirs_in[current] = [line[4:]]
        elif line == '$ ls':
            continue
        else:
            size = line.split()[0]
            if current in dirs_in:
                dirs_in[current].append(size)
            else:
                dirs_in[current] = [size]
    ans = 0
    @lru_cache
    def find_size(dir):
        size = 0
        for i in dirs_in[dir]:
            if i.isdigit():
                size += int(i)
            elif i in sizes:
                size += sizes[i]
            else:
                size += find_size(i)
        sizes[dir] = size
        return size

    sizes['/'] = find_size('/')
    for i in sizes:
        size = int(sizes[i])
        if size <= 100000:
            ans += size
    total = sum(sizes.values())
    if total <= 100000:
        ans += total
    print(ans)
