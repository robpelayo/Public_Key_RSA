#!/usr/bin/python3

import random


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
    if n % 2 == 0:
        return False
    return miller_rabin(n)


