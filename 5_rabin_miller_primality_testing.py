from random import randint


# Fast Modular Exponentiation Algorithm
def mod_exp(base, power, mod):
    if power == 0:
        return 1
    elif power % 2 == 0:
        temp = mod_exp(base, power // 2, mod)
        return temp ** 2 % mod
    else:
        return ((base % mod) * (mod_exp(base, power - 1, mod))) % mod


def miller_test(d, n):
    a = 2 + randint(1, n - 4)
    x = mod_exp(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False



def is_prime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for i in range(k):
        if not miller_test(d, n):
            return False
    return True


# Driver Code
if __name__ == '__main__':
    k = 4
    n = int(input("enter number : "))
    if is_prime(n, k):
        print("Probably Prime")
    else:
        print("Inconclusive")
