import re
from collections import deque
from collections import defaultdict

blueprints = []
with open('input2.txt') as f:
    data = f.readlines()
for line in data:
    ores = [i.split()[0] for i in re.findall('\d+ ore', line)]
    clay = int(re.findall('\d+ clay', line)[0].split()[0])
    obs = int(re.findall('\d+ obs', line)[0].split()[0])
    costs = {i:{0:int(ores[i]), 1:0, 2:0} for i in range(4)}
    costs[2][1] = clay
    costs[3][2] = obs
    blueprints.append(costs)

def solve(blueprints_num, mins):
    ans = 1
    for ix in range(blueprints_num):
        costs = blueprints[ix]
        robots = {i: 0 for i in range(4)}
        robots[0] = 1
        mats = {i: 0 for i in range(4)}
        queue = deque([(mats, robots, 0, set())])

        best = 0
        needed = {0:0 for i in range(4)}
        needed[3] = 1000
        needed[2] = costs[3][2]
        needed[1] = costs[2][1]
        needed[0] = max([costs[i][0] for i in costs])
        bests = defaultdict(int)
        while queue:
            mats, robots, time, skipped = queue.popleft()
            bests[time] = max(bests[time], mats[3])
            if time <= mins and bests[time] == mats[3]:

                poss = set()
                poss.add(-1)
                for i in range(3, -1, -1):
                    if (costs[i][0] <= mats[0]) and (costs[i][1] <= mats[1]) and (costs[i][2] <= mats[2]) and (robots[i]+1 <= needed[i]) and (i not in skipped):
                        poss.add(i)
                        if i == 3:
                            break #prioritise geode robot
                for build in poss:
                    if build == -1:
                        new_mats = mats.copy()
                        for i in range(4):
                            new_mats[i] += robots[i]
                        queue.append((new_mats, robots, time+1, poss))
                    else:
                        new_robots = robots.copy()
                        new_mats = mats.copy()
                        new_robots[build] += 1
                        for i in range(4):
                            new_mats[i] += robots[i]
                            if i < 3:
                                new_mats[i] -= costs[build][i]
                        queue.appendleft((new_mats, new_robots, time+1, set()))
        best = bests[mins]
        ans *= best
    print(ans)
solve(3, 32)
