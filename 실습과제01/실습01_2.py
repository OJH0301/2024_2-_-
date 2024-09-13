import time

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib_iter(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for k in range(2, n+1):
        a, b = b, a+b
    return b

k = 5

print("Fibonacci반복(", k, ") = ",fib_iter(k))
print("Fibonacci순환(", k,") = ",fib(k))

def measure_time(func1, func2, n):
  start_time1 = time.time()
  result1 = func1(n)
  end_time1 = time.time()
  elapsed_time1 = end_time1 - start_time1
  start_time2 = time.time()
  result2 = func2(n)
  end_time2 = time.time()
  elapsed_time2 = end_time2 - start_time2
  print("n= ", n, "반복: ", elapsed_time1, "순환: ", elapsed_time2)

for n in range(1, 40):
  measure_time(fib_iter, fib, n)

