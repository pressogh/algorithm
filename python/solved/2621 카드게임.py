import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

cards = []
for _ in range(5):
    t, n = input().split()
    cards.append((int(n), t))

cards.sort()

def rule_1():
    for i in range(5):
        if cards[i][1] != cards[0][1]: return 0
        if i < 4:
            if cards[i + 1][0] - cards[i][0] != 1: return 0
    return 900 + cards[-1][0]


def rule_2():
    c = [0] * 10
    for card in cards:
        c[card[0]] += 1
    for i in range(10):
        if c[i] != 4: continue
        return 800 + i
    return 0


def rule_3():
    c = [0] * 10
    for card in cards:
        c[card[0]] += 1
    
    three, two = -1, -1
    for i in range(10):
        if c[i] == 3: three = i
        if c[i] == 2: two = i
    
    if three == -1 or two == -1: return 0
    return 700 + three * 10 + two


def rule_4():
    for i in range(5):
        if cards[i][1] != cards[0][1]: return 0
    return 600 + cards[-1][0]


def rule_5():
    for i in range(5):
        if i < 4:
            if cards[i + 1][0] - cards[i][0] != 1: return 0
    return 500 + cards[-1][0]


def rule_6():
    c = [0] * 10
    for card in cards:
        c[card[0]] += 1
    for i in range(10):
        if c[i] != 3: continue
        return 400 + i
    return 0


def rule_7():
    c = [0] * 10
    for card in cards:
        c[card[0]] += 1
    
    c = [i for i in range(10) if c[i] == 2]
    if len(c) < 2: return 0
    return 300 + c[-1] * 10 + c[0]


def rule_8():
    c = [0] * 10
    for card in cards:
        c[card[0]] += 1
    
    c = [i for i in range(10) if c[i] == 2]
    if not c: return 0
    return 200 + c[-1]


def rule_9():
    return 100 + cards[-1][0]


res = 0
res = max(res, rule_1())
res = max(res, rule_2())
res = max(res, rule_3())
res = max(res, rule_4())
res = max(res, rule_5())
res = max(res, rule_6())
res = max(res, rule_7())
res = max(res, rule_8())
res = max(res, rule_9())
print(res)