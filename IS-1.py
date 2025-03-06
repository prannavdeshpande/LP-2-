def transform_string():
    user_string = input("Enter the string to transform: ")
    
    print("Choose the bitwise operation:")
    print("1. AND (&)")
    print("2. XOR (^)")
    
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice not in [1, 2]:
            print("Invalid choice! Please select 1 or 2.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    result = ""
    operation = "AND" if choice == 1 else "XOR"
    print(f"\nPerforming {operation} operation with 127...\n")
    
    for c in user_string:
        ascii_value = ord(c)
        transformed_value = (ascii_value & 127) if choice == 1 else (ascii_value ^ 127)
        transformed_char = chr(transformed_value) if 32 <= transformed_value <= 126 else "."
        result += transformed_char
        
        print(f"'{c}' -> ASCII: {ascii_value} -> Transformed: {transformed_value} -> '{transformed_char}'")
    
    print("\nOriginal String:", user_string)
    print("Transformed String:", result)

def main():
    while True:
        print("\n========== Bitwise String Transformer ==========")
        print("1. Transform a string")
        print("2. Exit")
        
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                transform_string()
            elif option == 2:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1 or 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
