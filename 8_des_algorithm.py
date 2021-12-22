from itertools import product


FIXED_IP = [2, 6, 3, 1, 4, 8, 5, 7]
FIXED_IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]

FIXED_EP = [4, 1, 2, 3, 2, 3, 4, 1]

FIXED_P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6] #10 bit permutation
FIXED_P8 = [6, 3, 7, 4, 8, 5, 10, 9] #8 bit permutation [3,10]
FIXED_P4 = [2, 4, 3, 1] #4 bit permutation [1,4]

S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]


def permutate(original, fixed_key):
    new = ''
    for i in fixed_key:
        new += original[i - 1]
    return new


def left_half(bits):
    return bits[:len(bits) // 2]


def right_half(bits):
    return bits[len(bits) // 2:]


def shift(bits):
    rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
    rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
    return rotated_left_half + rotated_right_half


def key1(KEY):
    return permutate(shift(permutate(KEY, FIXED_P10)), FIXED_P8)


def key2(KEY):
    return permutate(shift(shift(shift(permutate(KEY, FIXED_P10)))), FIXED_P8)


def xor(bits, key):
    new = ''
    for bit, key_bit in zip(bits, key):
        new += str(((int(bit) + int(key_bit)) % 2))
    return new


def lookup_in_sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sbox[row][col])


def f_k(bits, key):
    L = left_half(bits)
    R = right_half(bits)
    bits = permutate(R, FIXED_EP)
    bits = xor(bits, key)
    bits = lookup_in_sbox(left_half(bits), S0) + lookup_in_sbox(right_half(bits), S1)
    bits = permutate(bits, FIXED_P4)
    return xor(bits, L)


def encrypt(plain_text, KEY):
    bits = permutate(plain_text, FIXED_IP)
    temp = f_k(bits, key1(KEY))
    bits = right_half(bits) + temp
    bits = f_k(bits, key2(KEY))
    return (permutate(bits + temp, FIXED_IP_INVERSE))


def decrypt(cipher_text, KEY):
    bits = permutate(cipher_text, FIXED_IP)
    temp = f_k(bits, key2(KEY))
    bits = right_half(bits) + temp
    bits = f_k(bits, key1(KEY))
    return (permutate(bits + temp, FIXED_IP_INVERSE))

def message_to_bitArray(message):
    bitArray = []
    for x in message:
        bitArray.append((format(ord(x), 'b').zfill(8)))
    return bitArray

def bitArray_to_message(bitArray):
    message = ""
    for x in bitArray:
        message += chr(int(x, 2))
    return message

def encryptText(message, KEY):
    bitArray = message_to_bitArray(message)
    bitArrayCipher = []
    for x in bitArray:
        bitArrayCipher.append(encrypt(x, KEY))
    return bitArray_to_message(bitArrayCipher)

def decryptText(message, KEY):
    bitArray = message_to_bitArray(message)
    bitArrayCipher = []
    for x in bitArray:
        bitArrayCipher.append(decrypt(x, KEY))
    return bitArray_to_message(bitArrayCipher)


def CryptAnalysis(plainText, cipherText):
    all_possible_keys = ["".join(seq) for seq in product("01", repeat=10)]
    result_keys = []
    for key in all_possible_keys:
        print (key)
        if decryptText(cipherText, key) == plainText:
            result_keys.append(key)
    return result_keys


if __name__ == "__main__":
    kkey = '1111111101'
    print(encryptText("praveen", KEY=kkey))
    print(decryptText(encryptText("praveen", KEY=kkey), KEY=kkey))
    cipher = encryptText("praveen", KEY=kkey)
    print(cipher)
    possibleKeys = CryptAnalysis("praveen", cipher)
    print (possibleKeys)
