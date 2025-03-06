def encrypt(plaintext, key):
    col = len(key)
    row = len(plaintext) // col
    if len(plaintext) % col != 0:
        row += 1
    matrix = [['' for _ in range(col)] for _ in range(row)]
    for i in range(len(plaintext)):
        matrix[i // col][i % col] = plaintext[i]
    
    key_order = sorted([(key[i], i) for i in range(len(key))])
    
    cipher = ''
    for _, index in key_order:
        for r in range(row):
            cipher += matrix[r][index] if matrix[r][index] else 'Z'
    
    return cipher

def decrypt(cipher, key):
    col = len(key)
    row = len(cipher) // col
    
    key_order = sorted([(key[i], i) for i in range(len(key))])
    index_order = [i[1] for i in key_order]
    
    matrix = [['' for _ in range(col)] for _ in range(row)]
    idx = 0
    for i in index_order:
        for j in range(row):
            matrix[j][i] = cipher[idx]
            idx += 1
    
    plaintext = ''.join(''.join(row) for row in matrix).rstrip('Z')
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ").replace(" ", "").upper()
    key = input("Enter key: ").upper()
    cipher_text = encrypt(plaintext, key)
    print(f"Encrypted: {cipher_text}")
    decrypted_text = decrypt(cipher_text, key)
    print(f"Decrypted: {decrypted_text}")
