import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def bin_to_int(s):
    res = 0
    mul = 1
    for i in range(len(s) - 1, -1, -1):
        res += int(s[i]) * mul
        mul *= 2
    return res

t = int(input())
for i in range(1, t + 1):
    b = int(input())
    s = [0 if x == 'O' else 1 for x in input()]
    asi = []
    for j in range(b):
        asi.append(chr(bin_to_int(s[j * 8:j * 8 + 8])))
    
    print(f"Case #{i}: {''.join(asi)}")