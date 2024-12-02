def quick_sort(A, left, right, stats):
    if left < right:
        q = partition(A, left, right, stats)
        quick_sort(A, left, q - 1, stats)
        quick_sort(A, q + 1, right, stats)


def partition(A, left, right, stats):
    low = left + 1
    high = right
    pivot = A[left]
    while low <= high:
        while low <= right and A[low] < pivot:
            stats['comparisons'] += 1
            low += 1
        while high >= left and A[high] > pivot:
            stats['comparisons'] += 1
            high -= 1
        if low < high:
            A[low], A[high] = A[high], A[low]
            stats['movements'] += 2
    A[left], A[high] = A[high], A[left]
    stats['movements'] += 2
    return high


def quick_sort_with_stats(data):
    stats = {'comparisons': 0, 'movements': 0}
    quick_sort(data, 0, len(data) - 1, stats)
    print(">> Sorted:", ", ".join(map(str, data)))
    print(">> Number of Comparisons:", stats['comparisons'])
    print(">> Number of Data Movements:", stats['movements'])