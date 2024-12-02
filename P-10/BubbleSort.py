def bubble_sort(A):
    n = len(A)
    comparisons = 0
    movements = 0

    for i in range(n - 1, 0, -1):
        bChanged = False
        for j in range(i):
            comparisons += 1
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                movements += 2
                bChanged = True

        if not bChanged:
            break

    print(">> Sorted :", ', '.join(map(str, A)))
    print(">> Number of Comparisons :", comparisons)
    print(">> Number of Data Movements :", movements)