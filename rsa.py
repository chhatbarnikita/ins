import numpy as np


def totient(l, m):
    return (l-1)*(m-1)


def find_publickey(r1, r2):
    r, t, t1, t2, q1 = 0, 0, 1, 0, 0
    while r != 1:
        r = np.remainder(r2, r1)
        q1 = int(r2 / r1)
        t = t2 - (q1 * t1)
        t2, t1 = t1, t
        r2, r1 = r1, r
    return t


def convert(key, product, msg):
    num = np.remainder(msg, product)
    for i in range(0, key - 1):
        num *= msg
        num = np.remainder(num, product)
    converted_text = num
    return converted_text


if __name__ == '__main__':
    # text = input("Enter text: ")
    text = 88
    p = 17
    q = 83
    n = p * q
    e = 7
    tot = totient(p, q)
    d = find_publickey(e, tot)
    cipher_text = convert(e, n, text)
    print("Message: 88")
    print("Encrypted text: " + str(cipher_text))
    print("Decrypted text: " + str(convert(d, n, cipher_text)))
