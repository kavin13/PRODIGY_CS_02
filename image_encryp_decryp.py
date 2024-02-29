from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

    encrypted_image_path = image_path.replace('.png', '_encrypted.png')
    image.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()

  for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    decrypted_image_path = image_path.replace('_encrypted.png', '_decrypted.png')  # Save decrypted image
    image.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")

if __name__ == "__main__":
    image_path = r"C:\Users\kavin\Downloads\PRODIGY_CS_02\jpeg420exif.jpg"
    choice = input("Enter 'E' to encrypt or 'D' to decrypt the image: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))

    if choice.upper() == 'E':
        encrypt_image(image_path, key)
    elif choice.upper() == 'D':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
