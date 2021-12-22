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


# Driver Code
if __name__ == '__main__':
    num = 10
    mod = 17
    print(
        f"The Modular Multiplicative Inverse of {num} is : {euclidean_mod_inverse(num, mod)}")
