This is a Python program that implements the Caesar Cipher algorithm. 
The program allows users to input a message and a shift value, then either encrypts or decrypts the text based on their choice.

How the program works:
Encrypt Function:
Takes a message and a shift value.
For each character in the message, it checks if it's uppercase, lowercase, or a non-alphabetic character.
Shifts alphabetic characters by the specified shift value while leaving non-alphabetic characters unchanged.
Decrypt Function:
Similar to the encryption function, but it reverses the shift to restore the original message.
Main Program Logic:
The user selects whether to encrypt or decrypt.
Inputs the message and shift value.
Based on the user’s choice, the appropriate function is called.
