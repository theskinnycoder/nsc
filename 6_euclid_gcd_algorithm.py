# Euclid's GCD Algorithm (Iterative)
def euclidean_gcd(a, b):
    # a > b, always. Else, swap them.
    if b > a:
        a, b = b, a
    while(b):
        a, b = b, a % b
    return a


# Euclid's GCD Algorithm (Recursive)
def recursive_euclidean_gcd(a, b):
    # a > b, always. Else, swap them.
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return recursive_euclidean_gcd(b, a % b)


# Driver Code
if __name__ == '__main__':
    arr = list(map(int, input("Enter any no. of elements : ").split()))
    length_of_arr = len(arr)

    gcd = euclidean_gcd(arr[0], arr[1])

    for i in range(2, length_of_arr):
        gcd = euclidean_gcd(gcd, arr[i])

    print(f"The GCD of all the numbers is : {gcd}")
