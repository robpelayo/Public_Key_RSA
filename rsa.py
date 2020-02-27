#!/usr/bin/python3

import random


def miller_rabin(n):
    # Number of iterations
    k = 5
    # d * 2^r = n-1
    d = n - 1
    r = 0
    print(d)
    while d % 2 == 0:
        d //= 2
        r += 1
        # print("2^", r, "*", d, "=", pow(2,r) * d, "=", n-1)

    for i in range(0, k):
        a = random.randint(2, n-2)
        # print("Random number:", a)

        # x = a^d mod n
        x = pow(a,d) % n
        print(a, "^", d, "%", n, "=", x)

        if x == 1 or x == n-1:
            continue

        for j in range(0, r-1):
            x = pow(x, 2) % n
            if x == n - 1:
                continue

        return False
    return True


def test_prime(n):
    # False = composite, True = prime
    if n % 2 == 0:
        return False
    return miller_rabin(n)


print(test_prime(7829))
