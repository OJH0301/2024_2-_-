def sortGapInsertion(A, first, last, gap):
    global comparisons, movements
    for i in range(first + gap, last + 1, gap):
        key = A[i]
        j = i - gap
        while j >= first and key < A[j]:
            comparisons += 1
            A[j + gap] = A[j]
            movements += 1
            j -= gap
        A[j + gap] = key
        movements += 1

def shell_sort(A):
    global comparisons, movements
    n = len(A)
    gap = n // 2
    step = 1

    while gap > 0:
        if (gap % 2) == 0:
            gap += 1
        for i in range(gap):
            sortGapInsertion(A, i, n - 1, gap)
        gap = gap // 2
        step += 1

    print(">> Sorted:", ", ".join(map(str, A)))
    print(">> Number of Comparisons:", comparisons)
    print(">> Number of Data Movements:", movements)

comparisons = 0
movements = 0