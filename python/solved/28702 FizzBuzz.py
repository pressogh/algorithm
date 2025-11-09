def f(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    elif n % 3 != 0 and n % 5 == 0:
        return "Buzz"
    return str(n)

def solve():
    k = [input(), input(), input()]
    if k[0].isdecimal():
        print(f(int(k[0]) + 3))
    elif k[1].isdecimal():
        print(f(int(k[1]) + 2))
    elif k[2].isdecimal():
        print(f(int(k[2]) + 1))

if __name__ == '__main__':
    solve()