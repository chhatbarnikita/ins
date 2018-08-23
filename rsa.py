import numpy as np


def totient(l, m):
    return (l-1)*(m-1)


def find_publickey(a, m):
    a = np.remainder(a, m)
    for x in range(1, m):
        if np.remainder((a * x), m) == 1:
            return x
    return 1


def convert(key, product, msg):
    converted_text = np.remainder(msg**key, product)
    return converted_text


if __name__ == '__main__':
    # text = int(input("Enter text: "))
    print(11**23)
    text = 88
    p = 17
    q = 11
    n = p * q
    e = 7
    tot = totient(p, q)
    print("n= " + str(n))
    print("totient= " + str(tot))
    d = find_publickey(e, tot)
    print("d: " + str(d))
    cipher_text = convert(e, n, text)
    print("Encrypted text: " + str(cipher_text))
    print("Decrypted text: " + str(convert(d, n, cipher_text)))
    print()