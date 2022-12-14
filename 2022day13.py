def check(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b: return 1
        elif a > b: return -1
        else: return 0
    else:
        if isinstance(a, int):
            a = [a]
        if isinstance(b, int):
            b = [b]
        if len(a) == 0 and len(b) == 0: return 0
        elif len(a) == 0: return 1
        elif len(b) == 0: return -1
        
        if (valid := check(a[0], b[0])) == 0:
            return check(a[1:], b[1:])
        else:
            return valid

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]
    ans = 0
    pair_num = 1
    for i in range(0, len(data), 3):
        a = eval(data[i])
        b = eval(data[i+1])

        if check(a, b) > 0:
            ans += pair_num
        pair_num += 1
    print(ans)

    #part 2
with open('input.txt') as f:
    data = [eval(line.strip()) for line in f.readlines() if line != '\n']  + [[[2]], [[6]]]

    def partition(A, p, r):
        pivot = A[r]
        i = p-1
        for j in range(p, r):
            if check(pivot, A[j]) < 0:
                i += 1
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
        A[r] = A[i+1]
        A[i+1] = pivot
        return i+1

    def quicksort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            quicksort(A, p, q-1)
            quicksort(A, q+1, r)
    quicksort(data, 0, len(data)-1)
    for i in data:
        print(i)
    print((data.index([[2]])+1)*(data.index([[6]])+1))
