# Function to encrypt the message using Caesar Cipher
def encrypt(message, shift):
    encrypted_message = ""
    
    # Loop through each character in the message
    for char in message:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetic characters as is
        else:
            encrypted_message += char
            
    return encrypted_message

# Function to decrypt the message using Caesar Cipher
def decrypt(message, shift):
    decrypted_message = ""
    
    # Loop through each character in the message
    for char in message:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        # Leave non-alphabetic characters as is
        else:
            decrypted_message += char
            
    return decrypted_message

# Main program
def caesar_cipher():
    print("Caesar Cipher Program")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'e':
        encrypted = encrypt(message, shift)
        print("Encrypted Message:", encrypted)
    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print("Decrypted Message:", decrypted)
    else:
        print("Invalid choice, please select either 'E' for encryption or 'D' for decryption.")

# Run the Caesar Cipher program
caesar_cipher()
