def hex2bin(s):
    mp = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
          '4': "0100", '5': "0101", '6': "0110", '7': "0111",
          '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
          'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin

def ascii_to_hex(data):
    return ''.join(['{:02x}'.format(ord(c)) for c in data]).upper()

def hex_to_ascii(data):
    return ''.join([chr(int(data[i:i+2], 16)) for i in range(0, len(data), 2)])

def bin2hex(s):
    mp = {"0000": '0', "0001": '1', "0010": '2', "0011": '3',
          "0100": '4', "0101": '5', "0110": '6', "0111": '7',
          "1000": '8', "1001": '9', "1010": 'A', "1011": 'B',
          "1100": 'C', "1101": 'D', "1110": 'E', "1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]
    return hex

def bin2dec(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def dec2bin(num):
    res = bin(num).replace("0b", "")
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res

def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation

def shift_left(k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k

def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans

# Tables required for the algorithm
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
         6, 7, 8, 9, 8, 9, 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1]

per = [16, 7, 20, 21, 29, 12, 28, 17,
       1, 15, 23, 26, 5, 18, 31, 10,
       2, 8, 24, 14, 32, 27, 3, 9,
       19, 13, 30, 6, 22, 11, 4, 25]

sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

keyp = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Number of bit shifts
shift_table = [1, 1, 2, 2, 2, 2, 2, 2,
               1, 2, 2, 2, 2, 2, 2, 1]

# Key-Compression Table: Compression of key from 56 bits to 48 bits
key_comp = [14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32]

def encrypt(pt, rkb, rk, mode="ENCRYPT"):
    pt = hex2bin(pt)
    
    # Ensure pt is 64 bits (pad if needed)
    if len(pt) < 64:
        pt = pt.zfill(64)
    elif len(pt) > 64:
        pt = pt[:64]

    # Initial Permutation
    pt = permute(pt, initial_perm, 64)
    print(f"\n{'-'*80}")
    print(f"AFTER INITIAL PERMUTATION: {bin2hex(pt)}")
    
    # Splitting into left and right halves
    left = pt[0:32]
    right = pt[32:64]
    
    print(f"\nINITIAL STATE:")
    print(f"Left Half (L0): {bin2hex(left)} (Binary: {left})")
    print(f"Right Half (R0): {bin2hex(right)} (Binary: {right})")
    
    # Header for round details
    print(f"\n{'-'*80}")
    print(f"{'Round':^10}|{'Left Half':^18}|{'Right Half':^18}|{'Round Key':^14}|{'Operation':^20}")
    print(f"{'-'*10}|{'-'*18}|{'-'*18}|{'-'*14}|{'-'*20}")
    
    for i in range(0, 16):
        # Expansion: Expand right half from 32 to 48 bits
        right_expanded = permute(right, exp_d, 48)
        
        # XOR with round key
        xor_x = xor(right_expanded, rkb[i])
        
        # S-box substitution
        sbox_str = ""
        s_box_details = []  # To store detailed S-box transformations
        
        for j in range(0, 8):
            # Get row and column indices for S-box
            row = bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
            col = bin2dec(int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
            val = sbox[j][row][col]
            bin_val = dec2bin(val)
            sbox_str = sbox_str + bin_val
            
            # Store details for this S-box
            s_box_details.append(f"S{j+1}[{row},{col}]={val}({bin_val})")
        
        # Straight Permutation
        sbox_str = permute(sbox_str, per, 32)
        
        # XOR left and sbox_str
        result = xor(left, sbox_str)
        left = result
        
        # Swapper (except for last round)
        operation = "Regular"
        if i != 15:
            left, right = right, left
            operation = "Swap halves"
        
        # Print round details
        print(f"{i+1:^10}|{bin2hex(left):^18}|{bin2hex(right):^18}|{rk[i]:^14}|{operation:^20}")
        
        # Print detailed transformations for this round
        if mode == "ENCRYPT":
            action = "Encryption"
        else:
            action = "Decryption"
            
        print(f"\nDetailed {action} Round {i+1}:")
        print(f"  Input Right Half: {bin2hex(right)} (Binary: {right})")
        print(f"  Expanded to 48 bits: {bin2hex(right_expanded)} (Binary: {right_expanded})")
        print(f"  Round Key {i+1}: {rk[i]} (Binary: {rkb[i]})")
        print(f"  After XOR with key: {bin2hex(xor_x)} (Binary: {xor_x})")
        print(f"  S-Box Substitution: {', '.join(s_box_details)}")
        print(f"  After Permutation: {bin2hex(sbox_str)} (Binary: {sbox_str})")
        print(f"  Input Left Half: {bin2hex(result if i == 15 else (right if i < 15 else left))} (Binary: {result if i == 15 else (right if i < 15 else left)})")
        print(f"  New Left Half: {bin2hex(left)} (Binary: {left})")
        print(f"  New Right Half: {bin2hex(right)} (Binary: {right})")
        
        if i != 15:
            print(f"  Swapped for next round: L{i+1} = R{i}, R{i+1} = L{i} ⊕ f(R{i}, K{i+1})")
        else:
            print(f"  Final round (no swap): L16 remains L16, R16 remains R16")
    
    # Combination
    combine = left + right
    
    # Final permutation
    cipher_text = permute(combine, final_perm, 64)
    print(f"\n{'-'*80}")
    print(f"AFTER FINAL PERMUTATION: {bin2hex(cipher_text)}")
    
    return cipher_text

def main():
    print("\n" + "="*50)
    print("DES (Data Encryption Standard) Implementation")
    print("="*50)
    
    # Get plaintext and convert to hex
    plaintext = input("Enter the plaintext: ").upper()
    hex_plaintext = ascii_to_hex(plaintext)
    
    # Display input conversions
    print(f"\nPlaintext: {plaintext}")
    print(f"ASCII to Hex: {hex_plaintext}")
    print(f"Hex to Binary: {hex2bin(hex_plaintext)}")
    
    # Ensure plaintext is a multiple of 16 chars (64 bits in hex)
    if len(hex_plaintext) % 16 != 0:
        original_length = len(hex_plaintext)
        hex_plaintext = hex_plaintext.ljust((len(hex_plaintext) // 16 + 1) * 16, '0')
        print(f"Padded plaintext hex from {original_length} to {len(hex_plaintext)} chars: {hex_plaintext}")
    
    # Get key and convert to hex
    key_text = input("Enter the key: ").upper()
    hex_key = ascii_to_hex(key_text)
    
    # Display key conversions
    print(f"\nKey: {key_text}")
    print(f"ASCII to Hex: {hex_key}")
    
    # Ensure key is exactly 16 chars (64 bits in hex)
    if len(hex_key) > 16:
        hex_key = hex_key[:16]
        print(f"Key truncated to 64 bits (16 hex chars): {hex_key}")
    elif len(hex_key) < 16:
        original_length = len(hex_key)
        hex_key = hex_key.ljust(16, '0')
        print(f"Key padded from {original_length} to 16 hex chars: {hex_key}")
    
    # Process key
    key = hex2bin(hex_key)
    print(f"Key in binary: {key}")
    
    # Key permutation (PC-1)
    key = permute(key, keyp, 56)
    print(f"After key permutation (PC-1, 56 bits): {key}")
    
    # Split key
    left = key[0:28] 
    right = key[28:56]
    print(f"Split key: Left half: {left}, Right half: {right}")
    
    # Generate round keys
    rkb = []  # Round keys in binary
    rk = []   # Round keys in hex
    
    print("\nROUND KEY GENERATION:")
    print(f"{'Round':^8}|{'Left Key Half':^32}|{'Right Key Half':^32}|{'Combined':^60}|{'Compressed Key':^52}")
    print(f"{'-'*8}|{'-'*32}|{'-'*32}|{'-'*60}|{'-'*52}")
    
    for i in range(0, 16):
        # Shifting
        left = shift_left(left, shift_table[i])
        right = shift_left(right, shift_table[i])
        
        # Combining and permutation
        combine_str = left + right
        round_key = permute(combine_str, key_comp, 48)
        
        rkb.append(round_key)
        rk.append(bin2hex(round_key))
        
        print(f"{i+1:^8}|{left:^32}|{right:^32}|{combine_str:^60}|{round_key:^52}")
    
    # ENCRYPTION
    print("\n" + "="*50)
    print("ENCRYPTION PROCESS")
    print("="*50)
    
    cipher_text = ""
    # Process plaintext in 64-bit blocks (16 hex chars)
    block_count = len(hex_plaintext) // 16
    print(f"Processing {block_count} block(s) of plaintext")
    
    for i in range(0, len(hex_plaintext), 16):
        block = hex_plaintext[i:i+16]
        print(f"\nEncrypting Block {i//16 + 1}/{block_count}: {block}")
        cipher_block = bin2hex(encrypt(block, rkb, rk, "ENCRYPT"))
        cipher_text += cipher_block
        print(f"Block {i//16 + 1} Cipher Result: {cipher_block}")
    
    print("\n" + "="*50)
    print(f"FINAL CIPHER TEXT: {cipher_text}")
    print(f"(Hex to ASCII: {hex_to_ascii(cipher_text)})")
    print("="*50)
    
    # DECRYPTION
    print("\n" + "="*50)
    print("DECRYPTION PROCESS")
    print("="*50)
    
    rkb_rev = rkb[::-1]  # Reverse the order of round keys
    rk_rev = rk[::-1]
    
    plain_text = ""
    # Process ciphertext in 64-bit blocks (16 hex chars)
    block_count = len(cipher_text) // 16
    print(f"Processing {block_count} block(s) of ciphertext")
    
    for i in range(0, len(cipher_text), 16):
        block = cipher_text[i:i+16]
        print(f"\nDecrypting Block {i//16 + 1}/{block_count}: {block}")
        plain_block = bin2hex(encrypt(block, rkb_rev, rk_rev, "DECRYPT"))
        plain_text += plain_block
        print(f"Block {i//16 + 1} Plaintext Result: {plain_block}")
    
    # Convert hex back to ASCII
    decrypted_text = hex_to_ascii(plain_text)
    
    print("\n" + "="*50)
    print(f"FINAL DECRYPTED TEXT (HEX): {plain_text}")
    print(f"FINAL DECRYPTED TEXT (ASCII): {decrypted_text}")
    print("="*50)
    
    # SUMMARY
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"Original Text: {plaintext}")
    print(f"Key: {key_text}")
    print(f"Cipher Text (Hex): {cipher_text}")
    print(f"Decrypted Text: {decrypted_text}")
    print("="*50)

if __name__ == "__main__":
    main()
