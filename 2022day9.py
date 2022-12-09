with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

    visited = set()
    head = [0, 0]
    tail = [0, 0]

    def chase():
        x = head[0]-tail[0]
        y = head[1]-tail[1]
        if set([abs(x), abs(y)]) == set([1,2]):
            if abs(x) > 1:
                x //= 2
            else:
                y //= 2
            tail[0] += x
            tail[1] += y
        elif abs(x) == 2:
            tail[0] += (x//2)
        elif abs(y) == 2:
            tail[1] += (y//2)
        if tuple(tail) not in visited:
            visited.add(tuple(tail))

    for line in data:
        d, v = line.split()
        v = int(v)
        if d == 'R':
            for i in range(v):
                head[0] += 1
                chase()
        elif d == 'L':
            for i in range(v):
                head[0] -= 1
                chase()
        elif d == 'U':
            for i in range(v):
                head[1] += 1
                chase()
        else:
            for i in range(v):
                head[1] -= 1
                chase()
print(len(visited))


#part 2
with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

    visited = set()
    rope = [[0,0] for _ in range(10)]

    def chase(head, tail, is_tail):
        x = head[0]-tail[0]
        y = head[1]-tail[1]
        if (2 in [x, y] or -2 in [x, y]) and 0 not in [x, y]:
            if abs(x) > 1:
                x //= 2
            if abs(y) > 1:
                y //= 2
            tail[0] += x
            tail[1] += y
        elif abs(x) == 2:
            tail[0] += (x//2)
        elif abs(y) == 2:
            tail[1] += (y//2)
        if tuple(tail) not in visited and is_tail:
            visited.add(tuple(tail))
            print(tail)
        return(tail)

    ix = 0
    while ix < len(data):
        d, v = data[ix].split()
        v = int(v)
        
        for _ in range(v):
            if d == 'R':
                    rope[0][0] += 1
            elif d == 'L':
                    rope[0][0] -= 1
            elif d == 'U':
                    rope[0][1] += 1
            else:
                    rope[0][1] -= 1
            for knot in range(1, 10):
                is_tail = False
                if knot == 9:
                    is_tail = True

                rope[knot] = chase(rope[knot-1], rope[knot], is_tail)
        ix += 1
print(len(visited))
