import math


# Extended Euclid's Algorithm for Modular Multiplicative Inverse
def euclidean_mod_inverse(a, b):
    temp = b

    # Initialize variables
    t1, t2 = 0, 1

    if b == 1:
        return 0
 
    # Perform extended Euclid's algorithm until a > 1
    while a > 1:
        quotient, remainder = divmod(a, b)
        a, b = b, remainder
         
        t1, t2 = t2 - t1 * quotient, t1
     
    if (t2 < 0) :
        t2 += temp
 
    return t2


# Select Public Key
def get_public_key(phi):
    for i in range(2, phi):
        if math.gcd(i, phi) == 1:
            return i

# RSA Encryption Algorithm
def encrypt(plain_msg, e, n):
    return pow(plain_msg, e) % n


# RSA Decryption Algorithm
def decrypt(encrypted_msg, d, n):
    return pow(encrypted_msg, d) % n


# Driver Code
if __name__ == '__main__':
    plain_msg = 89
    p, q = 3, 7

    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_public_key(phi)
    # d = euclidean_mod_inverse(phi, e)
    d = (2 * phi + 1) // e

    encrypted_msg = encrypt(plain_msg, e, n)
    decrypted_text = decrypt(encrypted_msg, d, n)

    print(f'The Original Text is : {plain_msg}')
    print(f'The Encrypted Cipher Text is : {encrypted_msg}')
    print(f'The Decrypted Text is : {decrypted_text}')