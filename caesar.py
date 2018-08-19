def encrypt(text):
    temp = ''
    for c in text:
        value = ord(c) + key
        if value > ord('z'):
            value -= 26
        temp += chr(value)
    return temp


def decrypt(text):
    temp = ''
    for c in text:
        value = ord(c) - key
        if value < ord('a'):
            value += 26
        temp += chr(value)
    return temp


if __name__ == '__main__':
    key = int(input("Enter key: ")).replace(" ", "").lower()
    plaintext = input("Enter plain text: ").replace(" ", "").lower()
    cipher_text = encrypt(plaintext)
    print("Encrypted text: " + cipher_text)
    print("Decrypted text: " + decrypt(cipher_text))