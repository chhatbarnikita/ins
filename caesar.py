key = int(input("Enter key: ")).replace(" ", "").lower()
plainText = input("Enter plain text: ").replace(" ", "").lower()


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
    cipherText = encrypt(plainText)
    print("Encrypted text: " + cipherText)
    print("Decrypted text: " + decrypt(cipherText))