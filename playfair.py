import numpy as np


def key_matrix():
    keylist = [c for c in key]
    for c in range(97, 123):
        if len(keylist) == 25:
            break
        if chr(c) not in keylist:
            if chr(c) == 'q':
                if chr(c) not in plain_text:
                    continue
            keylist.append(chr(c))
    k_matrix = np.array(keylist).reshape((5, 5))
    print(k_matrix)
    return k_matrix


def get_row_col(alpha1, alpha2):
    global row1, row2, column1, column2
    first, second = False, False
    for i in range(5):
        if alpha1 in matrix[i] or alpha2 in matrix[i]:
            for j in range(5):
                if matrix[i][j] == alpha1:
                    row1, column1 = i, j
                    first = True
                elif matrix[i][j] == alpha2:
                    row2, column2 = i, j
                    second = True
            if first and second:
                break


def encryption(text):
    encrypted_text = ''
    global row1, row2, column1, column2

    for k in range(0, len(text), 2):
        get_row_col(text[k], text[k+1])

        if row1 == row2:
            encrypted_text += matrix[row1][(column1 + 1) % 5] + matrix[row2][(column2 + 1) % 5]
        elif column1 == column2:
            encrypted_text += matrix[(row1 + 1) % 5][column1] + matrix[(row2 + 1) % 5][column2]
        else:
            encrypted_text += matrix[row1][column2] + matrix[row2][column1]
        
        row1, column1, row2, column2 = 0, 0, 0, 0
    return encrypted_text


def decryption(text):
    decrypted_text = ''
    global row1, row2, column1, column2

    for k in range(0, len(text), 2):
        get_row_col(text[k], text[k+1])

        if row1 == row2:
            decrypted_text += matrix[row1][(column1 - 1) % 5] + matrix[row2][(column2 - 1) % 5]
        elif column1 == column2:
            decrypted_text += matrix[(row1 - 1) % 5][column1] + matrix[(row2 - 1) % 5][column2]
        else:
            decrypted_text += matrix[row1][column2] + matrix[row2][column1]

        row1, column1, row2, column2 = 0, 0, 0, 0
    return decrypted_text


if __name__ == '__main__':
    key = input("Enter key: ").replace(" ", "").lower()
    plain_text = input("Enter plain text: ").replace(" ", "").lower()
    row1, column1, row2, column2 = 0, 0, 0, 0
    matrix = key_matrix()
    cipher_text = encryption(plain_text)
    print("Cipher text: " + cipher_text)
    print("Decrypted text: " + decryption(cipher_text))

