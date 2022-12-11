from operator import mul
from operator import add
from functools import reduce

# with open('input.txt') as f:

#     inspect = [0, 0, 0, 0, 0, 0, 0, 0]
    
#     monkeys = [[[54,82,90,88,86,54], [mul, 7], 11, 2, 6],
#                 [[91,65], [mul, 13], 5, 7, 4],
#                 [[62, 54, 57, 92, 83, 63, 63], [add, 1], 7, 1, 7],
#                 [[67, 72, 68], [mul, None], 2, 0, 6],
#                 [[68, 89, 90, 86, 84, 57, 72, 84], [add, 7], 17, 3, 5],
#                 [[79, 83, 64, 58], [add, 6], 13, 3, 0],
#                 [[96, 72, 89, 70, 88], [add, 4], 3, 1, 2],
#                 [[79], [add, 8], 19, 4, 5]]
#     # inspect = [0, 0, 0, 0]
#     # monkeys = [[[79, 98], [mul, 19], 23, 2, 3],
#     #            [[54, 65, 75, 74], [add, 6], 19, 2, 0],
#     #            [[79, 60, 97], [mul, None], 13, 1, 3],
#     #            [[74], [add, 3], 17, 0 , 1]
#     #            ]
#     for round in range(20):
#         for i, monkey in enumerate(monkeys):
#             while monkey[0]:
#                 item = monkey[0].pop(0)
#                 if monkey[1][1] == None:
#                     new = reduce(monkey[1][0], [item, item])
#                 else:
#                     new = reduce(monkey[1][0], [item, monkey[1][1]])
#                 new //= 3
#                 if new % monkey[2] == 0:
#                     monkeys[monkey[3]][0].append(new)
#                 else:
#                     monkeys[monkey[4]][0].append(new)
#                 inspect[i] += 1
#     first = max(inspect)
#     inspect.remove(first)
#     second = max(inspect)
#     inspect.remove(second)
#     print(first*second)

from collections import deque
with open('input.txt') as f:

    inspect = [0, 0, 0, 0, 0, 0, 0, 0]
    
    monkeys = [[deque([54,82,90,88,86,54]), [mul, 7], 11, 2, 6],
                [deque([91,65]), [mul, 13], 5, 7, 4],
                [deque([62, 54, 57, 92, 83, 63, 63]), [add, 1], 7, 1, 7],
                [deque([67, 72, 68]), [mul, None], 2, 0, 6],
                [deque([68, 89, 90, 86, 84, 57, 72, 84]), [add, 7], 17, 3, 5],
                [deque([79, 83, 64, 58]), [add, 6], 13, 3, 0],
                [deque([96, 72, 89, 70, 88]), [add, 4], 3, 1, 2],
                [deque([79]), [add, 8], 19, 4, 5]]
    # inspect = [0, 0, 0, 0]
    # monkeys = [[[79, 98], [mul, 19], 23, 2, 3],
    #            [[54, 65, 75, 74], [add, 6], 19, 2, 0],
    #            [[79, 60, 97], [mul, None], 13, 1, 3],
    #            [[74], [add, 3], 17, 0 , 1]
    #            ]
    lcm = reduce(mul, [i[2] for i in monkeys])
    for round in range(10000):
        for i, monkey in enumerate(monkeys):
            while monkey[0]:
                item = monkey[0].popleft()
                if monkey[1][1] == None:
                    new = reduce(monkey[1][0], [item, item])
                else:
                    new = reduce(monkey[1][0], [item, monkey[1][1]])
                new %= lcm
                if new % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(new)
                else:
                    monkeys[monkey[4]][0].append(new)
                inspect[i] += 1
    first = max(inspect)
    inspect.remove(first)
    second = max(inspect)
    inspect.remove(second)
    print(first*second)
