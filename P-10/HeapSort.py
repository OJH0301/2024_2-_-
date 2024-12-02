def heappush(heap, n, stats):
    heap.append(n)
    i = len(heap) - 1
    while i != 1:
        pi = i // 2
        stats['comparisons'] += 1
        if n <= heap[pi]:
            break
        heap[i] = heap[pi]
        stats['movements'] += 1
        i = pi
    heap[i] = n
    stats['movements'] += 1


def heappop(heap, stats):
    size = len(heap) - 1
    if size == 0:
        return None

    root = heap[1]
    last = heap[size]
    pi = 1
    i = 2

    while i <= size:
        if i < size:
            stats['comparisons'] += 1
            if heap[i] < heap[i + 1]:
                i += 1
        stats['comparisons'] += 1
        if last >= heap[i]:
            break
        heap[pi] = heap[i]
        stats['movements'] += 1
        pi = i
        i *= 2

    heap[pi] = last
    stats['movements'] += 1
    heap.pop()
    return root


def heapSort(data):
    heap = [0]
    stats = {'comparisons': 0, 'movements': 0}

    for e in data:
        heappush(heap, e, stats)

    for i in range(1, len(data) + 1):
        data[-i] = heappop(heap, stats)

    print(">> Sorted:", ", ".join(map(str, data)))
    print(">> Number of Comparisons:", stats['comparisons'])
    print(">> Number of Data Movements:", stats['movements'])