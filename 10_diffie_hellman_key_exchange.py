P, G = 23, 9

print(f'The values of P and G are : {P} and {G}')

a, b = 4, 3
print(f"The private key 'a' for Alice is : {a}")
print(f"The private key 'b' for Bob is : {b}")

x = int(pow(G, a, P))
y = int(pow(G, b, P))

ka = int(pow(y, a, P))
kb = int(pow(x, b, P))

print(f"The secret key of Alice is : {ka}")
print(f"The secret Key of Bob is : {kb}")
