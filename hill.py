import numpy as np

# key = input("Enter key:").replace(" ", "").lower()
# plaintext = input("Enter text:").replace(" ", "").lower()
key = "gybnqkurp"
plaintext = "actact" #encryption: pohpoh
key_list = [(ord(c) % 97) for c in key]

key_matrix = np.array(key_list).reshape(3, 3)


def encrypt():
    encrypted_text = []
    for i in range(0, len(plaintext)-2, 3):
        col = np.array([ord(plaintext[i]) - 97, ord(plaintext[i+1]) - 97, ord(plaintext[i+2]) - 97])
        mul_col = list(np.remainder(np.matmul(key_matrix, col), 26) + 97)
        encrypted_text += [chr(c) for c in mul_col]
    print(encrypted_text)
    return encrypted_text

def decrypt(cipher):
    print("decryption")


if __name__ == '__main__':
    cipher_text = encrypt()
    decrypt(cipher_text)


# matrix = np.matrix([[1, 4, 2], [6, 3, 7], [7, 7, 3]])
#
# print(matrix)
# print(int(np.linalg.det(matrix)))
# print(matrix.getI() * int(np.linalg.det(matrix)))