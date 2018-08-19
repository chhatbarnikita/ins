import numpy as np


def encrypt():
    encrypted_text = []
    ls = [c for c in key] + [l for l in plaintext]
    rem = np.remainder(len(plaintext), len(key))
    if rem != 0:
        ls.extend('q' * rem)
    for i in range(1, len(key)+1):
        index = ls.index(str(i)) + len(key)
        encrypted_text += [ls[c] for c in range(index, len(ls), len(key))]
    return "".join(encrypted_text)


def decrypt(text):
    return


if __name__ == '__main__':
    plaintext = "nikitachhatbar"
    key = "4213"
    cipher_text = encrypt()
    print(cipher_text)
