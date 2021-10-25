'''
1. The algorithm is a substitution cipher. It shifts each letter by a certain key.
2. Python Library Functions used :
    a) ord() : Converts a character to its equivalent ASCII value.
    b) chr() : Converts an ASCII value to its equivalent character.
3. What are 65 and 97?
    a) 65 is the ASCII value of 'A'.
    b) 97 is the ASCII value of 'a'.
'''


# Get number equivalent of a character
def get_num_equivalent(char):
    return (
        ord(char) - 65) if char.isupper() else (ord(char) - 97)


# Get character equivalent of a number
def get_char_equivalent(char, num):
    return chr(num + 65) if char.isupper() else chr(num + 97)


# Encryption Algorithm
def encrypt(plain_text, key):
    encrypted_text = ''

    for char in plain_text:
        num_equivalent = get_num_equivalent(char)

        # Formula : (num_equivalent + key) mod 26
        encrypted_num = (num_equivalent + key) % 26

        encrypted_text += get_char_equivalent(char, encrypted_num)

    return encrypted_text


# Decryption Algorithm
def decrypt(encrypted_text, key):
    decrypted_text = ''

    for char in encrypted_text:
        num_equivalent = get_num_equivalent(char)

        # Formula : (num_equivalent - key) mod 26
        decrypted_num = (num_equivalent - key) % 26

        decrypted_text += get_char_equivalent(char, decrypted_num)

    return decrypted_text


# Driver Code
if __name__ == '__main__':
    plain_text, key = 'TheSkinnyCoder', 3

    encrypted_text = encrypt(plain_text, key)
    decrypted_text = decrypt(encrypted_text, key)

    print(f'The Original Text is : {plain_text}')
    print(f'The Encrypted Cipher Text is : {encrypted_text}')
    print(f'The Decrypted Text is : {decrypted_text}')
