def caesar_encrypt(text: str, shift: int) -> str:
    """
    Encrypts the given text using Caesar cipher.
    
    :param text: Input string to encrypt
    :param shift: Number of positions to shift each character
    :return: Encrypted string
    """
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) + shift - 65) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) + shift - 97) % 26 + 97))
        else:
            result.append(char)
    return ''.join(result)

def caesar_decrypt(text: str, shift: int) -> str:
    """
    Decrypts the given text using Caesar cipher.
    
    :param text: Input string to decrypt
    :param shift: Number of positions the characters were shifted
    :return: Decrypted string
    """
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    print("Caesar Cipher")
    action = input("Choose action (encrypt/decrypt): ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    
    if action == "encrypt":
        print("Encrypted text:", caesar_encrypt(text, shift))
    elif action == "decrypt":
        print("Decrypted text:", caesar_decrypt(text, shift))
    else:
        print("Invalid action!")