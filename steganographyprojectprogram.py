import cv2
import string
import os

# Create dictionaries for character to ASCII and ASCII to character mapping
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Load the image
image_path = r"C:\Users\ANJI JAYA\Desktop\New folder\successfully.jpeg"
x = cv2.imread(image_path)

# Get image dimensions
i, j, _ = x.shape
print(f"Image dimensions: {i}x{j}")

# Get user input for key and text to hide
key = input("Enter key to edit (Security key): ")
text = input("Enter text to hide: ")

# Initialize variables
k1 = 0
z = 0
n = 0
m = 0
l = len(text)

# Hide the text in the image
for i in range(l):
    if n < x.shape[0] and m < x.shape[1]:
        x[n, m, z] = d[text[i]] ^ d[key[k1]]
        m += 1
        if m == x.shape[1]:
            m = 0
            n += 1
        k1 = (k1 + 1) % len(key)

# Save the encrypted image
cv2.imwrite("encrypted_img.jpg", x)
os.startfile("encrypted_img.jpg")
print("Data hiding in image completed successfully.")

# Initialize variables for extraction
k1 = 0
z = 0
n = 0
m = 0

# User choice to extract data
ch = int(input("\nEnter 1 to extract data from Image: "))

if ch == 1:
    key1 = input("\n\nRe-enter key to extract text: ")
    decrypt = ""

    if key == key1:
        for i in range(l):
            if n < x.shape[0] and m < x.shape[1]:
                decrypt += c[x[n, m, z] ^ d[key[k1]]]
                m += 1
                if m == x.shape[1]:
                    m = 0
                    n += 1
                k1 = (k1 + 1) % len(key)
        print("Encrypted text was: ", decrypt)
    else:
        print("Key doesn't match.")
else:
    print("Thank you. Exiting.")
