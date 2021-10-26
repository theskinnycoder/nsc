from numpy import array


# Convert key text to 5*5 matrix
def create_key_matrix(key):
    # Do not repeat any letters in the key (hence convert to set 1st)
    mtx = list(set(key))

    # NOTE: Skip J in the alphabets for 25 letters (5*5)
    alphabets_array = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")
    for letter in alphabets_array:
        if letter not in mtx:
            mtx.append(letter)

    key_matrix = array(mtx).reshape(5, 5)
    return key_matrix


# Convert input plain text to digraphs array
def message_to_digraphs(plain_text):
    # If the plain text is odd in length, append Z, to get perfect digraphs
    if len(plain_text) & 1:
        plain_text += "Z"

    arr_of_pairs = [plain_text[i : i + 2] for i in range(0, len(plain_text), 2)]

    digraphs_array = []
    for pair in arr_of_pairs:
        if pair[0] == pair[1]:
            digraphs_array.append(pair[0] + 'Z')
        else:
            digraphs_array.append(pair)
    
    return digraphs_array



def find_position(key_matrix, letter):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                x, y = i, j
    return x, y


def encrypt(message, key_matrix):
    cipher = []
    
    for e in message:
        p1, q1 = find_position(key_matrix, e[0])
        p2, q2 = find_position(key_matrix, e[1])
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            cipher.append(key_matrix[p1][q1 + 1])
            cipher.append(key_matrix[p1][q2 + 1])
        elif q1 == q2:
            if p1 == 4:
                p1 = -1
            if p2 == 4:
                p2 = -1
            cipher.append(key_matrix[p1 + 1][q1])
            cipher.append(key_matrix[p2 + 1][q2])
        else:
            cipher.append(key_matrix[p1][q2])
            cipher.append(key_matrix[p2][q1])
        return cipher


if __name__ == '__main__':
    # Get the keyword & get the 5*5 key matrix
    key = input("Enter the keyword : ")
    key_matrix = create_key_matrix(key)
    print(f"The Key Matrix :\n{key_matrix}")

    # Get the plain text & the digraphs array
    message = input("Enter the plain text : ")
    digraphs_array = message_to_digraphs(message)
    print(f"The Array of Digraphs :\n{digraphs_array}")

    print(f"The Ciphered Text : {encrypt(digraphs_array, key_matrix)}")
