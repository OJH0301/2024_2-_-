def insertion_sort(A):
    n = len(A)
    comparisons = 0
    movements = 0
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            comparisons += 1
            A[j + 1] = A[j]
            movements += 1
            j -= 1
        if j >= 0:
            comparisons += 1
        A[j + 1] = key
        movements += 1

    print(">> Sorted:", ", ".join(map(str, A)))
    print(">> Number of Comparisons:", comparisons)
    print(">> Number of Data Movements:", movements)