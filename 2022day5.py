# with open('temp.txt') as f:
#     data = [line.strip() for line in f.readlines()]
# #                 [M]     [V]     [L]
# # [G]             [V] [C] [G]     [D]
# # [J]             [Q] [W] [Z] [C] [J]
# # [W]         [W] [G] [V] [D] [G] [C]
# # [R]     [G] [N] [B] [D] [C] [M] [W]
# # [F] [M] [H] [C] [S] [T] [N] [N] [N]
# # [T] [W] [N] [R] [F] [R] [B] [J] [P]
# # [Z] [G] [J] [J] [W] [S] [H] [S] [G]
# #  1   2   3   4   5   6   7   8   9 
#     crates = [['Z','T','F','R','W','J','G'],['G','W','M'],['J','N','H','G'],['J','R','C','N','W'],['W','F','S','B','G','Q','V','M'],
#     ['S','R','T','D','V','W','C'],['H','B','N','C','D','Z','G','V'], ['S','J','N','M','G','C'],['G','P','N','W','C','J','D','L']]
#     for line in data:
#         arr = line.split()
#         n, start, end = [int(arr[i]) for i in range(1, 6, 2)]
#         for i in range(n):
#             try:
#                 x = crates[start-1].pop()
#                 crates[end-1].append(x)
#             except:
#                 pass
#     ans = ''
#     for i in crates:
#         if len(i) != 0:
#             ans += i[-1]
#     print(ans)

with open('temp.txt') as f:
    data = [line.strip() for line in f.readlines()]
    crates = [['Z','T','F','R','W','J','G'],['G','W','M'],['J','N','H','G'],['J','R','C','N','W'],['W','F','S','B','G','Q','V','M'],
    ['S','R','T','D','V','W','C'],['H','B','N','C','D','Z','G','V'], ['S','J','N','M','G','C'],['G','P','N','W','C','J','D','L']]
    for line in data:
        arr = line.split()
        n, start, end = [int(arr[i]) for i in range(1, 6, 2)]
        end -= 1
        start -= 1
        if n > crates[start]:
            crates[start] = crates[start][:-n]
            crates[end] += crates[start][-n::-1]
        
    ans = ''
    for i in crates:
        if len(i) != 0:
            ans += i[-1]
    print(ans)