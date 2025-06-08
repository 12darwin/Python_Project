import hashlib
import os

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

def save_hash_to_file(filepath, hash_file):
    file_hash = calculate_hash(filepath)
    with open(hash_file, 'w') as f:
        f.write(file_hash)
    print(f"[+] Hash saved to {hash_file}")

def check_integrity(filepath, hash_file):
    if not os.path.exists(hash_file):
        print(f"[!] Hash file not found. Run the script with save option first.")
        return

    current_hash = calculate_hash(filepath)

    with open(hash_file, 'r') as f:
        saved_hash = f.read().strip()

    if current_hash == saved_hash:
        print("✅ File is unchanged.")
    else:
        print("⚠️ File has been modified!")

if __name__ == "__main__":
    file_to_check = "example.txt"
    hash_txt_file = "example_hash.txt"

    choice = input("Do you want to (s)ave hash or (c)heck integrity? [s/c]: ").strip().lower()
    
    if choice == 's':
        save_hash_to_file(file_to_check, hash_txt_file)
    elif choice == 'c':
        check_integrity(file_to_check, hash_txt_file)
    else:
        print("Invalid option. Choose 's' to save hash or 'c' to check integrity.")
