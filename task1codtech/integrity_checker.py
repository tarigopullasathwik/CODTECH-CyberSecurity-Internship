import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print("File not found.")
        return None


def store_hash(file_path, hash_value):
    with open("hashes.txt", "a") as f:
        f.write(f"{file_path}:{hash_value}\n")
    print("Hash stored successfully.")


def check_integrity(file_path):
    current_hash = calculate_hash(file_path)

    if not current_hash:
        return

    if not os.path.exists("hashes.txt"):
        print("No stored hashes found.")
        return

    with open("hashes.txt", "r") as f:
        for line in f:
            stored_file, stored_hash = line.strip().split(":")
            if stored_file == file_path:
                if stored_hash == current_hash:
                    print("File integrity intact. No changes detected.")
                else:
                    print("ALERT! File has been modified.")
                return

    print("File hash not found. Store hash first.")


if __name__ == "__main__":
    print("FILE INTEGRITY CHECKER")
    print("1. Store file hash")
    print("2. Check file integrity")

    choice = input("Enter choice (1/2): ")
    path = input("Enter file path: ")

    if choice == "1":
        file_hash = calculate_hash(path)
        if file_hash:
            store_hash(path, file_hash)
    elif choice == "2":
        check_integrity(path)
    else:
        print("Invalid choice.")
