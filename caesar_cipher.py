def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# --- Example Usage ---
if __name__ == "__main__":
    print("=*=*= Caesar Cipher App =*=*=")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    text = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g. 3): "))

    if choice == 'e':
        encrypted = encrypt(text, shift)
        print(f"\nEncrypted Message: {encrypted}")
    elif choice == 'd':
        decrypted = decrypt(text, shift)
        print(f"\nDecrypted Message: {decrypted}")
    else:
        print("Invalid choice. Use 'e' or 'd'.")

