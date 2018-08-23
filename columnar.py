import numpy as np


def encrypt(text):
    encrypted_text = []
    ls = [c for c in key] + [l for l in text]
    rem = np.remainder(len(text), len(key))
    if rem != 0:
        ls.extend('q' * (len(key) - rem)) #appending list for proper length
    for i in range(1, len(key)+1):
        index = ls.index(str(i)) + len(key)
        encrypted_text += [ls[c] for c in range(index, len(ls), len(key))] #adding column values
    return "".join(encrypted_text)


def decrypt(text):
    temp = dict()
    x = 0
    decrypted_text = ''
    column_size = int(len(text) / len(key))
    for i in range(1, len(key)+1):
        temp.__setitem__(i, text[x: x+column_size]) #converting to a dictionary
        x += column_size
    for i in range(column_size):
        for c in key:
            decrypted_text += temp.get(int(c))[i]
    return decrypted_text.strip('q')


if __name__ == '__main__':
    key = input("Enter key (in digits): ")
    plaintext = input("Enter text: ")
    # key = "253164"
    # plaintext = "cryptography"
    cipher_text = encrypt(plaintext)
    print("Encrypted text: " + cipher_text)
    print("Decrypted text: " + decrypt(cipher_text))
