from math import ceil

def encrypt(plaintext):
    text = [plaintext[i] for i in range(0, len(plaintext), 2)] + [plaintext[i] for i in range(1, len(plaintext), 2)]
    if len(plaintext) % 2 != 0:
        text.append("?")
    return "".join(text)


def decrypt(text):
    i, j = 0, ceil(len(text)/2)
    decrypted_text = ''
    for k in range(0, ceil(len(text)/2)):
        decrypted_text += text[i] + text[j]
        i += 1
        j += 1
    return decrypted_text.strip("?")


if __name__ == '__main__':
    text = input("Enter text: ")
    cipher_text = encrypt(text)
    print("Encrypted text: " + cipher_text)
    print("Decrypted text: " + decrypt(cipher_text))