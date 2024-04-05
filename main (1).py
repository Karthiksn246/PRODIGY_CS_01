def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            ciphertext += chr(shifted)
        else:
            ciphertext += char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
        if choice not in ('e', 'd'):
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue

        text = input("Enter the text: ").strip()

        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        if choice == 'e':
            result = caesar_cipher_encrypt(text, shift)
            print("Encrypted text:", result)
        else:
            result = caesar_cipher_decrypt(text, shift)
            print("Decrypted text:", result)

        another = input("Do you want to continue? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
