import time

count = 0

def hanoi_tower(n, fr='A', tmp='B', to='C') :
    global count
    count += 1
    if (n == 1) :
        print("원판 1: %s --> %s" % (fr, to))
    else :
        hanoi_tower(n - 1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to)

num = int(input('하노이 타워 높이를 입력해 주세요 : '))
start = time.time()
hanoi_tower(num)
end = time.time()
print("함수 호출 횟수:", count)
print("실행시간 = ", end - start)