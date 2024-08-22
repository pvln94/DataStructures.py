import heapq

class Node:
    def __init__(self, probability, symbol=None):
        self.probability = probability
        self.symbol = symbol
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.probability < other.probability

def build_huffman_tree(probabilities):
    heap = [Node(prob, symbol) for symbol, prob in probabilities.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(node1.probability + node2.probability)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_codes(node, current_code, huffman_codes):
    if node is None:
        return
    if node.symbol is not None:
        huffman_codes[node.symbol] = current_code
        return
    generate_codes(node.left, current_code + "0", huffman_codes)
    generate_codes(node.right, current_code + "1", huffman_codes)

def huffman_coding(symbols, probabilities):
    prob_dict = dict(zip(symbols, probabilities))
    root = build_huffman_tree(prob_dict)
    
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)
    
    return huffman_codes

# Example usage
symbols = ['A', 'B', 'C', 'D', 'E','F','G']
probabilities = [0.4, 0.3, 0.14, 0.07, 0.05, 0.03, 0.01]
huffman_codes = huffman_coding(symbols, probabilities)

print("Symbol\tCodeword")
for symbol, codeword in huffman_codes.items():
    print(f"{symbol}\t{codeword}")
