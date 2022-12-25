from operator import add, sub, mul, truediv
from functools import reduce

with open('input3.txt') as f:
    data = [line.strip() for line in f.readlines()]

m = {}
for line in data:
    self, calc = line.split(': ')
    if calc.isdigit():
        m[self] = int(calc)
    else:
        a, op, b = calc.split()
        if op == '+':
            op = add
        elif op == '-':
            op = sub
        elif op == '*':
            op = mul
        elif op == '/':
            op = truediv
        m[self] = [a, op, b]

def shout(name):
    if isinstance(m[name], int):
        return m[name]
    else:
        return reduce(m[name][1], [shout(m[name][0]), shout(m[name][2])])
#print(shout('root'))

# part 2
# initially tried brute force, then tried to reverse the equation manually (printed out the path that humn is on) - realised I got surprisingly close, just 1 mistake somewhere

flip = lambda op: lambda a, b: op(b, a)
ops = {add: (sub, sub), sub: (add, flip(sub)), mul: (truediv, truediv), truediv: (mul, flip(truediv))}
def shout(name):
    if isinstance(m[name], int) or m[name] == None:
        return m[name]
    else:
        a, b = shout(m[name][0]), shout(m[name][2])
        if None in (a, b):
            return None
        return m[name][1](a, b)

m['root'][1] = sub
m['humn'] = None
def solve(name, x):
    if m[name] == None:
        return x
    else:
        a = shout(m[name][0])
        b = shout(m[name][2])
        if b == None:
            return solve(m[name][2], ops[m[name][1]][1](x, a)) # humn down right path - avoid that path
        elif a == None:
            return solve(m[name][0], ops[m[name][1]][0](x, b)) # humn down left path

print(solve('root', 0))
