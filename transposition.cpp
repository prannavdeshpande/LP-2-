#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string encrypt(string plaintext, string key) {
    int col = key.length();
    int row = plaintext.length() / col;
    if (plaintext.length() % col != 0) {
        row++;
    }

    vector<vector<char>> matrix(row, vector<char>(col, ' ')); 

    for (int i = 0; i < plaintext.length(); ++i) {
        matrix[i / col][i % col] = plaintext[i];
    }

    vector<pair<char, int>> key_order;
    for (int i = 0; i < key.length(); ++i) {
        key_order.push_back(make_pair(key[i], i));
    }
    sort(key_order.begin(), key_order.end());

    string cipher = "";
    for (auto const& [char_val, index] : key_order) {
        for (int r = 0; r < row; ++r) {
            if (matrix[r][index] != ' ') {
                cipher += matrix[r][index];
            } else {
                cipher += 'Z';
            }
        }
    }

    return cipher;
}

string decrypt(string cipher, string key) {
    int col = key.length();
    int row = cipher.length() / col;

    vector<pair<char, int>> key_order;
    for (int i = 0; i < key.length(); ++i) {
        key_order.push_back(make_pair(key[i], i));
    }
    sort(key_order.begin(), key_order.end());

    vector<int> index_order;
    for (auto const& [char_val, index] : key_order) {
        index_order.push_back(index);
    }

    vector<vector<char>> matrix(row, vector<char>(col, ' '));

    int idx = 0;
    for (int i : index_order) {
        for (int j = 0; j < row; ++j) {
            matrix[j][i] = cipher[idx];
            idx++;
        }
    }

    string plaintext = "";
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            plaintext += matrix[i][j];
        }
    }

    // Remove trailing 'Z' characters
    while (!plaintext.empty() && plaintext.back() == 'Z') {
        plaintext.pop_back();
    }

    return plaintext;
}

int main() {
    string plaintext, key;

    cout << "Enter plaintext: ";
    getline(cin, plaintext);
    
    //Remove spaces and convert to uppercase
    string plaintext_no_spaces = "";
    for (char c : plaintext){
        if (c != ' ')
            plaintext_no_spaces += toupper(c);
    }
    plaintext = plaintext_no_spaces;
   
    cout << "Enter key: ";
    getline(cin, key);
    
    //Convert key to uppercase
    for (char & c : key) c = toupper(c);

    string cipher_text = encrypt(plaintext, key);
    cout << "Encrypted: " << cipher_text << endl;

    string decrypted_text = decrypt(cipher_text, key);
    cout << "Decrypted: " << decrypted_text << endl;

    return 0;
}
