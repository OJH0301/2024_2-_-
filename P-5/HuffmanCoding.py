class Node:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

def heappush(heap, node):
    heap.append(node)
    i = len(heap) - 1
    while i != 1:
        pi = i // 2
        if node.freq >= heap[pi].freq:
            break
        heap[i] = heap[pi]
        i = pi
    heap[i] = node

def heappop(heap):
    size = len(heap) - 1
    if size == 0:
        return None

    root = heap[1]
    last = heap[size]
    pi = 1
    i = 2

    while i <= size:
        if i < size and heap[i].freq > heap[i + 1].freq:
            i += 1
        if last.freq <= heap[i].freq:
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2

    heap[pi] = last
    heap.pop()
    return root

def make_tree(freq, labels):
    heap = [0]
    for f, label in zip(freq, labels):
        heappush(heap, Node(f, label))

    while len(heap) > 2:
        e1 = heappop(heap)
        e2 = heappop(heap)

        merged = Node(e1.freq + e2.freq)
        merged.left = e1
        merged.right = e2
        heappush(heap, merged)

    root = heappop(heap)
    return root

def generate_codes(node, current_code="", codes={}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

def compress_rate(original_text, huffman_codes):
    original_size = len(original_text) * 8
    compressed_size = sum(len(huffman_codes[char]) for char in original_text)
    compression_ratio = (original_size - compressed_size) / original_size * 100
    return compression_ratio

labels = ['k', 'o', 'r', 'e', 'a', 't', 'c', 'h']
freq = [10, 5, 2, 15, 18, 4, 7, 11]

root = make_tree(freq, labels)
codes = {}
generate_codes(root, "", codes)

while True:
    text = input("Please a word: ").strip()
    if not all(char in labels for char in text):
        print("illegal character.")
        continue

    encoded_text = ''.join(codes[char] for char in text)
    print(f"결과 비트 열: {encoded_text}")

    compression_ratio = compress_rate(text, codes)
    print(f"압축률: {compression_ratio:.2f}%")
    break