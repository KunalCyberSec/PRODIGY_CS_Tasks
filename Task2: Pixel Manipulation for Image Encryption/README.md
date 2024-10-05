This is a Python program that encrypts and decrypts an image by manipulating the pixel values using basic mathematical operations. 
We'll use the Pillow library to handle image processing, so ensure you have it installed by running:
  "pip install pillow"

How it works:

Encrypting the image:

1. The program reads the image using Pillow's Image.open() and converts the image into a NumPy array, where each pixel is represented as a number (RGB values for colored images).
2. Each pixel value is modified by adding a key (a user-provided number) and taking the result modulo 256 to ensure the pixel values stay within the valid range (0–255).
3. The modified array is converted back to an image and saved as "encrypted_image.png".
   
Decrypting the image:

1. The decryption process reverses the encryption by subtracting the key from each pixel value and applying modulo 256 to handle wraparound.
2. The result is saved as "decrypted_image.png".

User Interaction:

1. The user chooses between encrypting or decrypting an image.
2. Inputs the path of the image and a numeric key.
3. The program either encrypts or decrypts the image based on the user's choice.
