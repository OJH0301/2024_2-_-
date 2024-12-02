from queue import Queue
from collections import deque

def radix_sort(A):
    comparisons = 0
    movements = 0
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            digit = (A[i] // factor) % BUCKETS
            comparisons += 1
            queues[digit].put(A[i])

        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                movements += 2
                i += 1

        factor *= 10

    print(">> Sorted:", ", ".join(map(str, A)))
    print(">> Number of Comparisons:", comparisons)
    print(">> Number of Data Movements:", movements)

import random
BUCKETS = 10
DIGITS  = 4