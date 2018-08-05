import numpy as np

key = input("Enter key:").replace(" ", "").lower()
plaintext = input("Enter text:").replace(" ", "").lower()

key_matrix = np.array(key)
print(key_matrix)

# matrix = np.matrix([[1, 4, 2], [6, 3, 7], [7, 7, 3]])
#
# print(matrix)
# print(int(np.linalg.det(matrix)))
# print(matrix.getI() * int(np.linalg.det(matrix)))