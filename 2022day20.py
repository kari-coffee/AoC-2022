# with open('input2.txt') as f:
#     nums = [int(line.strip()) for line in f.readlines()]
# length = len(nums)
# mixed = [(i, n) for i, n in enumerate(nums)]

# for i in range(length): #go through each number
#     for ix in range(length): #go through until you find the right indexed one (not duplicate or wrong number)
#         if mixed[ix][0] == i:
#             x = mixed.pop(ix)
#             if x[1]-ix == 0:
#                 mixed.append(x)
#             else:
#                 mixed.insert((x[1]+ix) % (length-1), x)
#             break

# ans = 0
# for i in range(len(mixed)):
#     if mixed[i][1] == 0:
#         start = i
#         break
# for i in [1000, 2000, 3000]:
#     ans += mixed[(start+i)%length][1]
# print(ans)

# part 2

with open('input2.txt') as f:
    nums = [int(line.strip()) for line in f.readlines()]

length = len(nums)

mixed = [(i, n*811589153) for i, n in enumerate(nums)]
for _ in range(10):
    for i in range(length): #go through each number
        for ix in range(length): #go through until you find the right indexed one (not duplicate or wrong number)
            if mixed[ix][0] == i:
                x = mixed.pop(ix)
                if x[1]-ix == 0:
                    mixed.append(x)
                else:
                    mixed.insert((x[1]+ix) % (length-1), x)
                break

ans = 0
for i in range(len(mixed)):
    if mixed[i][1] == 0:
        start = i
        break
for i in [1000, 2000, 3000]:
    ans += mixed[(start+i)%length][1]
print(ans)
