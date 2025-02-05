import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

# Generate Key
def generate_rsa_keys():
    # private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    #  public key from the private key
    public_key = private_key.public_key()

    # Save private key
    with open("private.pem", "wb") as private_pem:
        private_pem.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    # Save public key
    with open("public.pem", "wb") as public_pem:
        public_pem.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print("RSA keys generated and saved as private.pem and public.pem.")

# Encryptor
def encrypt_file(filename):
    # Load public key
    with open("public.pem", "rb") as public_pem:
        public_key = serialization.load_pem_public_key(public_pem.read())

    # Read file content
    with open(filename, "rb") as file:
        file_data = file.read()

    # Encrypt
    encrypted_data = public_key.encrypt(
        file_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(f"{filename}.enc", "wb") as enc_file:
        enc_file.write(encrypted_data)

    os.remove(filename)
    print(f"{filename} encrypted successfully!")

# Decryptor
def decrypt_file(filename):
    # Load private key
    with open("private.pem", "rb") as private_pem:
        private_key = serialization.load_pem_private_key(private_pem.read(), password=None)

    with open(filename, "rb") as enc_file:
        encrypted_data = enc_file.read()

    # Decrypt data using RSA
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    original_filename = filename.rsplit(".enc", 1)[0]
    with open(original_filename, "wb") as dec_file:
        dec_file.write(decrypted_data)

    os.remove(filename)
    print(f"{filename} decrypted successfully!")

# Main
def main():
    if len(sys.argv) != 3:
        print("Usage: python3 rsa_file_encryptor.py [encrypt|decrypt] [filename]")
        sys.exit(1)

    action = sys.argv[1].lower()
    filename = sys.argv[2]

    if action == "encrypt":
        encrypt_file(filename)
    elif action == "decrypt":
        decrypt_file(filename)
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
        sys.exit(1)

if __name__ == "__main__":
    if not os.path.exists("private.pem") or not os.path.exists("public.pem"):
        generate_rsa_keys()
    main()
