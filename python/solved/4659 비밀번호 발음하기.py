import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import string

vowels = set(['a', 'e', 'i', 'o', 'u'])
consonants = set(string.ascii_lowercase) - vowels

while True:
    s = input()
    if s == "end": break

    acceptable = True

    if len(set(s) & vowels) == 0: acceptable = False
    else:
        for i in range(len(s) - 2):
            t = set(s[i:i+3])
            if len(t & vowels) == 0 or len(t & consonants) == 0:
                acceptable = False
                break
        for i in range(len(s) - 1):
            if s[i] == s[i + 1] and s[i] not in set(['e', 'o']):
                acceptable = False
                break
    
    print(f"<{s}> is ", "not " if not acceptable else "", "acceptable.", sep='')