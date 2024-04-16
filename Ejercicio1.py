import heapq

class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.symbol < other.symbol
        return self.freq < other.freq

def build_huffman_tree(symbols):
    heap = [HuffmanNode(sym, freq) for sym, freq in symbols.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(left.symbol + right.symbol, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node.left is None and node.right is None:
        codebook[node.symbol] = prefix
    if node.left:
        generate_codes(node.left, prefix + "0", codebook)
    if node.right:
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

# Diccionario inverso basado en el código de Huffman
reverse_codebook = {
    '00': 'Ankh',
    '010': 'Lotus',
    '011': 'Scarab',
    '100': 'Obelisk',
    '101': 'Djed',
    '1100': 'Sphinx',
    '1101': 'Pyramid',
    '111': 'Eye of Horus'
}

# Diccionario de traducción de jeroglíficos a significados en español
jeroglifico_a_espanol = {
    'Ankh': 'vida',
    'Lotus': 'pureza',
    'Scarab': 'transformación',
    'Obelisk': 'estabilidad',
    'Djed': 'durabilidad',
    'Sphinx': 'guardián',
    'Pyramid': 'eternidad',
    'Eye of Horus': 'protección'
}

def decode_and_translate_huffman(encoded_message, reverse_codebook, translation_dict):
    decoded_message = []
    translated_message = []
    current_code = ""
    for bit in encoded_message:
        current_code += bit
        if current_code in reverse_codebook:
            jeroglifico = reverse_codebook[current_code]
            decoded_message.append(jeroglifico)
            translated_message.append(translation_dict[jeroglifico])
            current_code = ""  # Reset the current code
    return ' '.join(decoded_message), ' '.join(translated_message)

def verify_translation(translated_message):
    keywords = ['vida', 'pureza', 'transformación', 'estabilidad', 'durabilidad', 'guardián', 'eternidad', 'protección']
    for keyword in keywords:
        if keyword in translated_message:
            return True
    return False

# Mensajes codificados para decodificar
mensaje_1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"

# Decoding and translating the encoded message
decoded_message, translated_message = decode_and_translate_huffman(mensaje_1, reverse_codebook, jeroglifico_a_espanol)

if verify_translation(translated_message):
    print("Decoded Message:", decoded_message)
    print("Translated Message:", translated_message)
else:
    print("La traducción no tiene sentido.")
