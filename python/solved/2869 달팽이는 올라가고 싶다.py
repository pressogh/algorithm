import math

def solve():
    a, b, v = map(int, input().split())
    # 마지막 날 밤에는 미끄러지지 않기 때문에 최종 도달해야 하는 위치는 v - b
    # 하루에 이동 기능한 거리는 a - b
    # 날짜는 무조건 1씩 증가해야 하기 때문에 ceil 사용으로 올림 처리
    print(math.ceil((v - b) / (a - b)))
        
if __name__ == '__main__':
    solve()