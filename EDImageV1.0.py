```python
from PIL import Image

def encrypt_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    #### Loop for each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            ### pixel swapping (red and blue values)
            pixels[x, y] = (b, g, r)

    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    image.save(encrypted_image_path)
    print("Image Encrypted successfully!")
    return encrypted_image_path

def decrypt_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    ### Loop for each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            ### swapping pixels
            pixels[x, y] = (b, g, r)

    decrypted_image_path = image_path.split('_encrypted')[0] + '_decrypted.png'
    image.save(decrypted_image_path)
    print("Image decrypted successfully!")
    return decrypted_image_path

def main():
    image_path = input("Enter the path of the image: ")
    mode = 0
    mode = input("Enter 1 for 'encrypt' or 2 for 'decrypt': ")
    if mode == "1":
        encrypted_image_path = encrypt_image(image_path)
    elif mode == "2":
        decrypted_image_path = decrypt_image(image_path)
    else:
        print("Invalid mode! Please enter '1' (Encrypt)' or '2' (Decrypt)'.")
    
   
main()

```
