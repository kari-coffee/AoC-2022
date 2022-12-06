with open('input.txt') as f:
    data = f.read()
    
    for i in range(3, len(data)):
        valid = True
        visited = set()
        for j in range(1, 4): #modify 4 -> 14 for part 2
            if data[i] == data[i-j] or data[i-j] in visited:
                valid = False
                break
            visited.add(data[i-j])
        if valid:
            print(i+1)
            break