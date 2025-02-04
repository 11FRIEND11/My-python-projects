RSA Encryption Guide

This folder consists of the following files:

- file_encryptor.txt: Python code used to encrypt and decrypt messages.
- public.pem: The public key used for encryption.
- private.pem: The private key used for decryption.

---

Encrypting the File

To encrypt a file using the terminal, run the following command:

python3 RSA_Encryptor.py encrypt message.txt

- This will create a new encrypted file: message.txt.enc.
- The original file (message.txt) will be deleted, making it unrecoverable without the private key.

---

Decrypting the File

To decrypt the file, run the following command:

python3 RSA_Encryptor.py decrypt message.txt.enc

- This will decrypt the file using the private key.
- The encrypted file (message.txt.enc) will be deleted as it is no longer needed.

---

Important Notes:

- The private key (private.pem) is necessary for decryption. If you lose it, you won't be able to decrypt your files. Store it in a secure location.
- Ensure you enter the commands correctly to avoid any errors.
