#!/usr/bin/python3

import random

# UPPER_LIMIT = int(4294967295)
# LOWER_LIMIT = int(2147483648)

UPPER_LIMIT = int(2147483647)
LOWER_LIMIT = int(1073741824)

# Power function at the bit level from geeksforgeeks.org
def power(x, y, n):
    res = 1
    x = x % n

    while y > 0:
        if y & 1:
            res = (res * x) % n

        y = y >> 1
        x = (x*x) % n
    return res


# pseudocode from miller-rabin wikipedia
def miller_rabin(n):
    # Number of iterations
    k = 40
    # d * 2^r = n-1
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for i in range(0, k):
        a = 2 + random.randint(1, n - 4)

        x = power(a, d, n)

        if x == 1 or x == n-1:
            return True

        for j in range(0, r-1):
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
    while True:
        q = random_big_num()
        while q % 12 != 5:
            q = random_big_num()
        if test_prime(q):
            p = 2 * q + 1
            if test_prime(p):
                return p


def read_in_encryption():
    ptextfile = open("ptext.txt", 'r')
    message = ptextfile.read()
    ptextfile.close()
    pubkeyfile = open("pubkey.txt")
    key = pubkeyfile.read()
    pubkeyfile.close()
    data = key.split()
    return message, int(data[0]), int(data[1]), int(data[2])


def read_in_decryption():
    ciphertextfile = open("ctext.txt", 'r')
    ciphertext = ciphertextfile.read()
    ciphertextfile.close()
    cipher = ciphertext.split()
    privatekeyfile = open("prikey.txt", 'r')
    d = privatekeyfile.read()
    privatekeyfile.close()
    d_data = d.split()
    pubkeyfile = open("pubkey.txt")
    key = pubkeyfile.read()
    pubkeyfile.close()
    data = key.split()
    return cipher, int(d_data[2]), int(data[0])


def get_c1_encrypt(g, p, k):
    return pow(g, k, p)


def get_c2_encrpyt(e, m, p, k):
    return (pow(e, k, p) * pow(m, 1, p)) % p

def hex_to_string(words):
    return bytes.fromhex(words).decode('utf-8', "ignore")


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
        d = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        g = 2
        e = power(g, d, p)
        pubkeyfile = open("pubkey.txt", 'w')
        pubkeyfile.write(str(p) + " " +  str(g) + " " + str(e))
        pubkeyfile.close()
        privatekeyfile = open("prikey.txt", 'w')
        privatekeyfile.write(str(p) + " " + str(g) + " " + str(d))
        privatekeyfile.close()
    elif selection == 2:
        message, p, g, e = read_in_encryption()
        hex_message = message.encode('utf-8').hex()
        print(hex_message)
        words = []
        for i in range(0, len(hex_message), 8):
            words.append(int(hex_message[i:i+8], 16))
        cipher = ''
        for i in range(0, len(words)):
            k = random.randint(0, p-1)
            c1 = get_c1_encrypt(g, p, k)
            c2 = get_c2_encrpyt(e, words[i], p, k)
            cipher += str(c1) + " " + str(c2) + '\n'
        ciphertextfile = open("ctext.txt", 'w')
        ciphertextfile.write(cipher)
        ciphertextfile.close()
        print(cipher)
    elif selection == 3:
        cipher, d, p = read_in_decryption()
        message = ''
        for i in range(0, len(cipher), 2):
            message += hex((power(int(cipher[i]), (p-1) - d, p) * (int(cipher[i+1]) % p)) % p)[2:]
        print(hex_to_string(message))
        dtextfile = open("dtext.txt", 'w')
        dtextfile.write(hex_to_string(message))
        dtextfile.close()

    else:
        print("Invalid selection. Please enter only 1-3.")


main()
