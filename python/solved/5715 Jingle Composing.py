import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

while True:
    song = input()
    if song == '*': break

    song, res = song.split('/')[1:-1], 0
    for s in song:
        cnt = 0
        for c in s:
            match c:
                case 'W': cnt += 64
                case 'H': cnt += 32
                case 'Q': cnt += 16
                case 'E': cnt += 8
                case 'S': cnt += 4
                case 'T': cnt += 2
                case 'X': cnt += 1
        if cnt == 64: res += 1

    print(res)