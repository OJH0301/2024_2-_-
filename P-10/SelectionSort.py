def selection_sort(A):
    n = len(A)
    comparisons = 0
    movements = 0

    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            comparisons += 1
            if A[j] < A[least]:
                least = j
        if least != i:
            A[i], A[least] = A[least], A[i]
            movements += 2

    print(">> Sorted :", ', '.join(map(str, A)))
    print(">> Number of Comparisons :", comparisons)
    print(">> Number of Data Movements :", movements)