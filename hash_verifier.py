import hashlib
import os

def calculate_hash(filepath, algorithm='sha256'):
    if not os.path.exists(filepath):
        print(f"[!] File not found: {filepath}")
        return None

    hash_func = getattr(hashlib, algorithm)()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def verify_hash(filepath, known_hash, algorithm='sha256'):
    current_hash = calculate_hash(filepath, algorithm)
    if current_hash is None:
        return

    print(f"[+] Calculated {algorithm.upper()} hash: {current_hash}")
    print(f"[+] Provided   {algorithm.upper()} hash: {known_hash}")

    if current_hash.lower() == known_hash.lower():
        print("[✔] Hash match. File is verified.")
    else:
        print("[✘] Hash mismatch. File may be modified or corrupted.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 hash_verifier.py <file> <known_hash>")
    else:
        filepath = sys.argv[1]
        known_hash = sys.argv[2]
        verify_hash(filepath, known_hash)

