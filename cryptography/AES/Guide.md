AES Encryption Guide

This folder contains the following files:

- file_encryptor.txt: Python code used to encrypt and decrypt messages.
- secret.key: The key used for decryption.

---

Encrypting the File

To encrypt a file using the terminal, run the following command:

python3 AES_Encryptor.py encrypt message.txt

- This will create a new encrypted file: message.txt.enc.
- The original file (message.txt) will be deleted, making it unrecoverable without the secret key.

---

Decrypting the File

To decrypt the file, run the following command:

python3 AES_Encryptor.py decrypt message.txt.enc

- This will decrypt the file using the secret key.
- The encrypted file (message.txt.enc) will be deleted as it is no longer needed.

---

Important Notes:

- Backup your secret key (secret.key). If lost, you won't be able to decrypt your files.
- Ensure you enter the commands correctly to avoid any errors.
