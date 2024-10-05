from PIL import Image
import numpy as np

# Function to encrypt the image using pixel manipulation
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)  # Convert the image to a numpy array (pixels)
    
    # Apply encryption: modify pixel values using the key
    encrypted_array = (img_array + key) % 256  # Ensure values remain within valid pixel range (0-255)
    
    # Convert the encrypted numpy array back to an image
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    
    # Save encrypted image
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'")
    
# Function to decrypt the image using pixel manipulation
def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img_array = np.array(img)  # Convert the image to a numpy array (pixels)
    
    # Apply decryption: reverse the modification of pixel values using the key
    decrypted_array = (img_array - key) % 256  # Reverse operation, ensuring values remain valid (0-255)
    
    # Convert the decrypted numpy array back to an image
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    
    # Save decrypted image
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'")

# Main function to handle user input for encryption or decryption
def image_encryption_tool():
    print("Image Encryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").lower()
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter an encryption/decryption key (numeric value): "))  # Simple numeric key

    if choice == 'e':
        encrypt_image(image_path, key)
    elif choice == 'd':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice, please select either 'E' for encryption or 'D' for decryption.")

# Run the Image Encryption Tool
image_encryption_tool()
