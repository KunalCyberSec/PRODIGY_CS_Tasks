This is a Python program that implements the Caesar Cipher algorithm. 
The program allows users to input a message and a shift value, then either encrypts or decrypts the text based on their choice.

How the program works:

Encrypt Function:

1. Takes a message and a shift value.
2. For each character in the message, it checks if it's uppercase, lowercase, or a non-alphabetic character.
3. Shifts alphabetic characters by the specified shift value while leaving non-alphabetic characters unchanged.

Decrypt Function:

1. Similar to the encryption function, but it reverses the shift to restore the original message.

Main Program Logic:

1. The user selects whether to encrypt or decrypt.
2. Inputs the message and shift value.
3. Based on the user’s choice, the appropriate function is called.
