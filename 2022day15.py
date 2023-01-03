from re import findall

with open('input.txt') as f:
    data = f.readlines()

# ROW = 2000000
# seen = set()
# covered = [0, 0]
# for line in data:
#     sx, sy, bx, by = [int(i) for i in findall('[0-9-]+', line)]

#     dist = abs(sx-bx) + abs(sy-by)
#     y_dist = abs(ROW-sy)
#     remaining = dist-y_dist
#     if remaining > 0:
#         covered[0] = min(covered[0], sx-remaining)
#         covered[1] = max(covered[1], sx+remaining)
# print(covered[1]-covered[0])

#part 2
for row in range(20):
    seen_s = set()
    seen_b = set()
    covered = [0, 0]
    sensors = 0
    beacons = 0
    for line in data:
        sx, sy, bx, by = [int(i) for i in findall('[0-9-]+', line)]
        if sy == row and sx not in seen_s:
            seen_s.add(sx)
            sensors += 1
        if by == row and bx not in seen_b:
            seen_b.add(bx)
            beacons += 1
        dist = abs(sx-bx) + abs(sy-by)
        y_dist = abs(row-sy)
        remaining = dist-y_dist
        if remaining > 0:
            left = sx-remaining
            right = sx+remaining
            if left <= covered[1] and right >= covered[0] or covered == [0, 0]:
                covered[0] = min(covered[0], sx-remaining)
                covered[1] = max(covered[1], sx+remaining) - sensors-beacons
            else:
                print(row)
    covered[0] = max(0, covered[0])
    covered[1] = min(20, covered[1])

    #print(covered[1]-covered[0])
