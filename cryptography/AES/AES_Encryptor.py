from cryptography.fernet import Fernet
import sys
import os

# Generate and save the key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Load the key from file
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the file and delete the original
def encrypt_file(filename, key):
    with open(filename, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(filename + ".enc", "wb") as enc_file:
        enc_file.write(encrypted)
    os.remove(filename)  # Delete original file
    print(f"{filename} encrypted!")

# Decrypt the file and delete the encrypted version
def decrypt_file(filename, key):
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data)
    output_file = filename.replace(".enc", "")
    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted)
    os.remove(filename)  # Delete encrypted file
    print(f"{filename} decrypted!")

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 file_encryptor.py <encrypt/decrypt> <filename>")
        sys.exit()

    action = sys.argv[1]
    filename = sys.argv[2]

    try:
        key = load_key()
    except FileNotFoundError:
        key = generate_key()

    if action == "encrypt":
        encrypt_file(filename, key)
    elif action == "decrypt":
        decrypt_file(filename, key)
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
