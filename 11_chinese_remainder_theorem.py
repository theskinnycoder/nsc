# Get the product of all elements of an array
def prod_of_arr(arr):
    prod = 1
    for elem in arr:
        prod *= elem
    return prod


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


# CRT Algorithm
def chinese_remainder(num_arr, rem_arr):
    sum = 0
    prod = prod_of_arr(num_arr)
    for num, rem in zip(num_arr, rem_arr):
        p = prod // num
        sum += rem * euclidean_mod_inverse(p, num) * p
    return sum % prod


if __name__ == '__main__':
    num_arr = [3, 4, 7]
    rem_arr = [1, 1, 0]
    print(f"The minimum number that gives {rem_arr} on modulo division with {num_arr} is : {chinese_remainder(num_arr, rem_arr)}")
