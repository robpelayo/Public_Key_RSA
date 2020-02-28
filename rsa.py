#!/usr/bin/python3

import random

UPPER_LIMIT = int(4294967295)
LOWER_LIMIT = int(2147483648)


# Power function at the bit level from geeksforgeeks.org
def power(x, y, n):
    res = 1
    x = x % n

    while y> 0:
        if y & 1:
            res = (res * x) % n

        y = y >> 1
        x = (x*x) % n
    return res


# pseudocode from miller-rabin wikipedia
def miller_rabin(n):
    # Number of iterations
    k = 30
    # d * 2^r = n-1
    d = n - 1
    r = 0
    # print(d)
    while d % 2 == 0:
        d //= 2
        r += 1
        # print("2^", r, "*", d, "=", pow(2,r) * d, "=", n-1)

    for i in range(0, k):
        a = 2 + random.randint(1, n - 4)
        # print("Random number:", a)

        # x = a^d mod n
        # x = pow(a,d) % n
        x = power(a, d, n)
        # print(a, "^", d, "%", n, "=", x)

        if x == 1 or x == n-1:
            return True

        for j in range(0, r-1):
            # x = pow(x, 2) % n
            x = power(x, 2, n)
            if x == n - 1:
                return True

        return False
    return True


def test_prime(n):
    # False = composite, True = prime
    if n % 2 == 0 or n <= 1:
        return False
    return miller_rabin(n)


def random_big_num():
    return random.randint(LOWER_LIMIT, UPPER_LIMIT)


def generate_safe_prime():
    q = 0
    while True:
        q = random_big_num()
        while q % 12 != 5:
            q = random_big_num()
            # print(q)
        # print("Testing if prime")
        if test_prime(q):
            # print("We found our prime")
            p = 2 * q + 1
            if test_prime(p):
                return p


def prompt():
    try:
        print("What would you like to do?")
        print("1. Key Generation")
        print("2. Encryption")
        print("3. Decryption")
        return int(input("Enter 1-3: "))
    except:
        print("Only enter a number 1-3")
        return prompt()


def main():
    selection = prompt()
    if selection == 1:
        seed_num = int(input("Input a number to seed the random number generator: "))
        random.seed(seed_num)
        p = generate_safe_prime()
        g = 2
        e = 12
        pubkeyfile = open("pubkey.txt", 'w')
        pubkeyfile.write(str(p) + " " +  str(g) + " " + str(e))
        pubkeyfile.close()
        print(p)
    elif selection == 2:
        print("encryption")
    elif selection == 2:
        print("encryption")
    else:
        print("Invalid selection. Please enter only 1-3.")


main()
