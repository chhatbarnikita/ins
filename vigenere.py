key = input("Enter key:").replace(" ", "").lower()
plaintext = input("Enter text:").replace(" ", "").lower()


def encrypt(text):
    temp = ''
    i = 0
    for c in text:
        if i == len(key):
            i = 0
        value = ord(c) + (ord(key[i]) % 97)
        if value > ord('z'):
            value -= 26
        temp += chr(value)
        i += 1
    return temp


def decrypt(text):
    temp = ''
    i = 0
    for c in text:
        if i == len(key):
            i = 0
        value = ord(c) - (ord(key[i]) % 97)
        if value < ord('a'):
            value += 26
        temp += chr(value)
        i += 1
    return temp


cipher_text = encrypt(plaintext)
print("Cipher text: " + cipher_text)
decrypted_text = decrypt(cipher_text)
print("Decrypted text: " + decrypted_text)
