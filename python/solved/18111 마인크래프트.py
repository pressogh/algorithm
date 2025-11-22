import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter
n, m, b = map(int, input().split())
ground = Counter()
for _ in range(n):
    ground.update(map(int, input().split()))

min_floor, max_floor = min(ground.keys()), max(ground.keys())

time_res, floor_res = 2 ** 31, -1
for floor in range(min_floor, max_floor + 1):
    time, block = 0, b
    less_cnt = 0

    for value, count in ground.items():
        if value > floor:
            block += (value - floor) * count
            time += 2 * ((value - floor) * count)
        if value < floor:
            less_cnt += (floor - value) * count
            time += (floor - value) * count
    
    if block >= less_cnt and time <= time_res:
        time_res = time
        floor_res = floor

print(time_res, floor_res)