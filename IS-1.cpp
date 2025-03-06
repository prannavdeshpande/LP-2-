#include <iostream>
#include <string>
using namespace std;

void transformString() {
    string userString;
    cout << "Enter the string to transform: ";
    cin.ignore();
    getline(cin, userString);

    cout << "Choose the bitwise operation:\n";
    cout << "1. AND (&)\n";
    cout << "2. XOR (^)\n";
    int choice;
    cout << "Enter your choice (1 or 2): ";
    cin >> choice;

    if (choice != 1 && choice != 2) {
        cout << "Invalid choice! Please select 1 or 2.\n";
        return;
    }

    string result = "";
    cout << "\nPerforming " << (choice == 1 ? "AND" : "XOR") << " operation with 127...\n";

    for (char c : userString) {
        int asciiValue = static_cast<int>(c);
        int transformedValue = (choice == 1) ? (asciiValue & 127) : (asciiValue ^ 127);
        char transformedChar = static_cast<char>(transformedValue);

       
        if (transformedValue < 32 || transformedValue > 126) {
            result += ".";
        } else {
            result += transformedChar;
        }

        cout << "'" << c << "' -> ASCII: " << asciiValue
             << " -> Transformed: " << transformedValue
             << " -> '" << (transformedValue < 32 || transformedValue > 126 ? '.' : transformedChar) << "'\n";
    }

    cout << "\nOriginal String: " << userString << endl;
    cout << "Transformed String: " << result << endl;
}

int main() {
    while (true) {
        cout << "\n========== Bitwise String Transformer ==========\n";
        cout << "1. Transform a string\n";
        cout << "2. Exit\n";
        cout << "Enter your choice: ";
        int option;
        cin >> option;

        if (option == 1) {
            transformString();
        } else if (option == 2) {
            cout << "Exiting the program. Goodbye!\n";
            break;
        } else {
            cout << "Invalid choice! Please enter 1 or 2.\n";
        }
    }

    return 0;
}
