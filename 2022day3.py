with open('temp.txt') as f:
    data = f.readlines()
    c = 0
    for line in data:
        n = len(line)
        first = set(line[:n//2])
        second = set(line[n//2:])
        for i in first.intersection(second):
            same = i
        if same == same.upper():
            c += ord(same) - 64 + 26
        else:
            c += ord(same) - 96
print(c)

with open('temp.txt') as f:
    data = f.readlines()
    c = 0
    for i in range(0, len(data), 3):
        group = [set(data[i+j]) for j in range(3)]
        x = set.intersection(*group)
        for k in x:
            if k == '\n':
                continue
            same = k
        if same == same.upper():
            c += ord(same) - 64 + 26
        else:
            c += ord(same) - 96
print(c)