# Get the plain text matrix (1 * 3 from a 3 letter word)
def get_plain_text_matrix(plain_text):
    return [(ord(plain_text[i]) - 65) for i in range(3)]


# Get the key matrix (3 * 3 mtx from a 9 letter word)
def get_key_matrix(key):
    mtx = [[0] * 3 for _ in range(3)]
    counter = 0
    for i in range(3):
        for j in range(3):
            mtx[i][j] = ord(key[counter]) - 65
            counter += 1
    return mtx


# Get the cipher text matrix (1 * 3 mtx, since 1*3 x 3*3 = 1*3)
def get_cipher_text_matrix(p_mtx, k_mtx):
    mtx = [0 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            mtx[i] += ((p_mtx[j] * k_mtx[i][j]))
        mtx[i] %= 26
    return mtx


# Encryption Algorithm
def encrypt(plain_text, key):
    plain_text_mtx = get_plain_text_matrix(plain_text)
    key_mtx = get_key_matrix(key)
    cipher_text_mtx = get_cipher_text_matrix(plain_text_mtx, key_mtx)

    return ''.join(chr(cipher_text_mtx[i] + 65) for i in range(3))


# Driver Code
if __name__ == "__main__":
    # plain_text : 3 characters
    # key : 9 characters
    plain_text, key = "TSC", "developer"

    encrypted_text = encrypt(plain_text, key)

    print(f'The Encrypted Text is : {encrypted_text}')
