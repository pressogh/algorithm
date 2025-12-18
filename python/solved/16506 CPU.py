import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

opcode = ["ADD", "SUB", "MOV", "AND", "OR", "NOT", "MULT", "LSFTL", "LSFTR", "ASFTR", "RL", "RR"]

t = int(input())
while t > 0:
    t -= 1
    oc, rd, ra, rb = input().split()

    flag = False
    if oc[-1] == 'C': flag = True; oc = oc[:-1]

    res = ((((opcode.index(oc) << 2) | (2 if flag else 0)) << 3) | int(rd)) << 3
    if not oc.startswith(("MOV", "NOT")): res |= int(ra)
    res <<= 4
    res |= (int(rb) << (0 if flag else 1))
    print(format(res, 'b').zfill(16))