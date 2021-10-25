# Extended Euclid's Algorithm for Modular Multiplicative Inverse
def euclidean_mod_inverse(a, b):
    # a > b, always. Else, swap them.
    if b > a:
        a, b = b, a

    # Initialize variables
    t1, t2 = 0, 1

    # Perform extended Euclid's algorithm until b = 0
    while b:
        quotient, remainder = divmod(a, b)

        # Shifting the values to the left
        a, b = b, remainder
        t1, t2 = t2, t1 - t2 * quotient
    return t1


# Driver Code
if __name__ == '__main__':
    num = 3
    mod = 11
    print(
        f"The Modular Multiplicative Inverse of {num} is : {euclidean_mod_inverse(num, mod)}")
