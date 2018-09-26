import numpy as np


def to_binary(key, n, msg):
    binary = bin(key).replace('0b', '')
    temp = msg
    for i in binary:
        if i == '1':
            temp *= np.remainder(temp**2, n)
        else:
            temp *= np.remainder(temp**2, n)
    return np.remainder(temp, n)


def get_encrypted_key(key, n, msg):
    num = np.remainder(msg, n)
    for i in range(0, key - 1):
        num *= msg
        num = np.remainder(num, n)
    converted_text = num
    return converted_text


if __name__ == '__main__':
    p = 29
    alpha = 2
    a = 5
    b = 12
    A = get_encrypted_key(a, p, alpha)
    B = get_encrypted_key(b, p, alpha)
    kab = get_encrypted_key(a, p, B)
    kba = get_encrypted_key(b, p, A)
    print("a: " + str(a))
    print("b: " + str(b))
    print("kab: " + str(kab))
    print("kba: " + str(kba))
