#Following algorithm is only for 3*3 matrix
import numpy as np


def check_determinant():
    if np.linalg.det(key_matrix) != 0:
        return int(np.linalg.det(key_matrix))
    else:
        print("Determinant of the key matrix is not zero!")
        exit()


def check_gcd(num1, num2):
    while num1:
        if num2 == 0:
            break
        num1, num2 = num2, num1 % num2
    if num1 == 1:
        return
    else:
        exit()


def mod_inverse(a, m):
    a = np.remainder(a, m)
    for x in range(1, m):
        if np.remainder((a * x), m) == 1:
            return x
    return 1


def get_minor(i, j):
    temp = []
    for m in range(3):
        if m == i:
            continue
        for n in range(3):
            if n == j:
                continue
            temp.append(key_matrix[m][n])
    return np.array(temp).reshape(2, 2)


def find_inverse(det_inv):
    adj_matrix = []
    for i in range(3):
        for j in range(3):
            minor = get_minor(i, j)
            cofactor = (minor[0][0] * minor[1][1]) - (minor[0][1] * minor[1][0]) #taking determinant of minor
            adj_matrix.append(cofactor * det_inv)
    for i in range(1, len(adj_matrix), 2):
        adj_matrix[i] *= (-1)
    inv_matrix = np.transpose(np.array(adj_matrix).reshape(3, 3))
    return inv_matrix


def convert(text, matrix):
    converted_text = []
    for i in range(0, len(text)-2, 3):
        col = np.array([ord(text[i]) - 97, ord(text[i+1]) - 97, ord(text[i+2]) - 97])
        new_col = list(np.remainder(np.matmul(matrix, col), 26) + 97) #multiplication of key with column of plaintext
        converted_text += [chr(c) for c in new_col]
    return "".join(converted_text)


def encrypt():
    encrypted_text = convert(plaintext, key_matrix)
    return encrypted_text


def decrypt(cipher):
    determinant = check_determinant()
    check_gcd(determinant, 26)
    temp = mod_inverse(determinant, 26)
    inverse = find_inverse(temp)
    decrypt_text = convert(cipher, inverse)
    return decrypt_text


if __name__ == '__main__':
    # Enter key whose length is such that 3*3 matrix can be formed
    # Similarly length of the plain text must be multiple of 3

    key = input("Enter key:").replace(" ", "").lower()
    plaintext = input("Enter text:").replace(" ", "").lower()
    # plaintext = "actact" and key = "gybnqkurp"
    # encryption = "pohpoh"

    key_list = [(ord(c) % 97) for c in key]
    key_matrix = np.array(key_list).reshape(3, 3)

    cipher_text = encrypt()
    print("Encrypted text: " + str(cipher_text))
    decrypted_text = decrypt(cipher_text)
    print("Decrypted text: " + str(decrypted_text))


