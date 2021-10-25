# Fast Modular Exponentiation Algorithm
def mod_exp(base, power, mod):
    if power == 0:
        return 1
    elif power & 1 == 0:
        temp = mod_exp(base, power // 2, mod)
        return temp ** 2 % mod
    else:
        return ((base % mod) * (mod_exp(base, power - 1, mod))) % mod


# Driver Code
if __name__ == '__main__':
    base = int(input("Enter any base : "))
    power = int(input("Enter any power : "))
    mod = int(input("Enter the value of the mod : "))
    print(
        f"The Modular Exponentiation Result is : {mod_exp(base, power, mod)}")
