import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
import getpass
import base64

# Generate key using password
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 = 32 bytes
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Encrypt file
def encrypt_file(filename):
    password = getpass.getpass("Enter password for encryption: ")
    salt = os.urandom(16)
    key = generate_key(password, salt)

    aesgcm = AESGCM(key)
    nonce = os.urandom(12)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = aesgcm.encrypt(nonce, data, None)

    with open(filename + ".enc", "wb") as enc_file:
        enc_file.write(salt + nonce + encrypted_data)

    print("✅ File encrypted successfully!")

# Decrypt file
def decrypt_file(filename):
    password = getpass.getpass("Enter password for decryption: ")

    with open(filename, "rb") as enc_file:
        content = enc_file.read()

    salt = content[:16]
    nonce = content[16:28]
    encrypted_data = content[28:]

    key = generate_key(password, salt)
    aesgcm = AESGCM(key)

    try:
        decrypted_data = aesgcm.decrypt(nonce, encrypted_data, None)
        output_file = filename.replace(".enc", "")

        with open(output_file, "wb") as dec_file:
            dec_file.write(decrypted_data)

        print("✅ File decrypted successfully!")
    except:
        print("❌ Incorrect password or corrupted file!")

# Main menu
def main():
    print("\n=== Advanced Encryption Tool (AES-256) ===")
    print("1. Encrypt a file")
    print("2. Decrypt a file")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        file = input("Enter file name to encrypt: ")
        encrypt_file(file)
    elif choice == "2":
        file = input("Enter file name to decrypt: ")
        decrypt_file(file)
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
