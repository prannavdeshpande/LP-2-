#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Function to encrypt using columnar transposition
string encrypt(const string& plaintext, const string& key) {
    int keyLength = key.length();
    int plaintextLength = plaintext.length();

    // Determine the number of rows needed
    int numRows = (plaintextLength + keyLength - 1) / keyLength;

    // Create a matrix to hold the plaintext characters
    vector<vector<char>> matrix(numRows, vector<char>(keyLength, ' ')); // Initialize with spaces

    // Fill the matrix with the plaintext
    int k = 0;
    for (int i = 0; i < numRows; ++i) {
        for (int j = 0; j < keyLength; ++j) {
            if (k < plaintextLength) {
                matrix[i][j] = plaintext[k++];
            }
        }
    }

    // Sort the key to determine the column order
    string sortedKey = key;
    sort(sortedKey.begin(), sortedKey.end());

    // Read the matrix column by column based on the sorted key
    string ciphertext = "";
    for (char c : sortedKey) {
        int colIndex = key.find(c);
        for (int i = 0; i < numRows; ++i) {
            ciphertext += matrix[i][colIndex];
        }
        key[colIndex] = '*'; // Mark the column as used to handle duplicate key characters
    }

    return ciphertext;
}

// Function to decrypt using columnar transposition
string decrypt(const string& ciphertext, const string& key) {
    int keyLength = key.length();
    int ciphertextLength = ciphertext.length();
    int numRows = (ciphertextLength + keyLength - 1) / keyLength;

    // Create a matrix to hold the ciphertext characters
    vector<vector<char>> matrix(numRows, vector<char>(keyLength, ' '));

    // Sort the key to determine the column order
    string sortedKey = key;
    sort(sortedKey.begin(), sortedKey.end());

    // Fill the matrix column by column based on the sorted key
    int k = 0;
    string originalKey = key;  // Store the original key for index lookup
    for (char c : sortedKey) {
        int colIndex = originalKey.find(c);

        for (int i = 0; i < numRows; ++i) {
            if (k < ciphertextLength) {
                matrix[i][colIndex] = ciphertext[k++];
            }
        }
        originalKey[colIndex] = '*';  // Mark the column as used to handle duplicate key characters
    }

    // Read the matrix row by row to get the plaintext
    string plaintext = "";
    for (int i = 0; i < numRows; ++i) {
        for (int j = 0; j < keyLength; ++j) {
            if (matrix[i][j] != ' ') {
                plaintext += matrix[i][j];
            }
        }
    }

    return plaintext;
}

int main() {
    string plaintext, key;

    cout << "Enter the plaintext: ";
    getline(cin, plaintext);

    cout << "Enter the key (e.g., 4312): ";
    getline(cin, key);

    string ciphertext = encrypt(plaintext, key);
    cout << "Ciphertext: " << ciphertext << endl;

    string decryptedText = decrypt(ciphertext, key);
    cout << "Decrypted text: " << decryptedText << endl;

    return 0;
}