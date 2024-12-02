sorted = [0] * 100

def merge_sort(A, left, right, stats):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid, stats)
        merge_sort(A, mid + 1, right, stats)
        merge(A, left, mid, right, stats)


def merge(A, left, mid, right, stats):
    global sorted
    k = left
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        stats['comparisons'] += 1
        if A[i] <= A[j]:
            sorted[k] = A[i]
            stats['movements'] += 1
            i, k = i + 1, k + 1
        else:
            sorted[k] = A[j]
            stats['movements'] += 1
            j, k = j + 1, k + 1

    if i > mid:
        sorted[k:k + right - j + 1] = A[j:right + 1]
        stats['movements'] += (right - j + 1)
    else:
        sorted[k:k + mid - i + 1] = A[i:mid + 1]
        stats['movements'] += (mid - i + 1)

    A[left:right + 1] = sorted[left:right + 1]
    stats['movements'] += (right - left + 1)

def merge_sort_with_stats(data):
    stats = {'comparisons': 0, 'movements': 0}
    merge_sort(data, 0, len(data) - 1, stats)
    print(">> Sorted:", ", ".join(map(str, data)))
    print(">> Number of Comparisons:", stats['comparisons'])
    print(">> Number of Data Movements:", stats['movements'])
