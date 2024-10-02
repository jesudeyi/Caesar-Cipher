# Caeser_cipher
def caesar_cipher(text, shift):
        result = ""
        
        for char in text:
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += char
        
        return result
option = 'y'
while option == 'y' or option == 'Y':
    try: 
        # Welcome instructions
        print("Which operation do you wish to perform?")
        print("1. Encrypting a message")
        print("2. Decrypting a message") 
        choice = int(input("Enter an option: "))  

        # Encryption
        if choice == 1:
            plainText = input("Enter the message you want to encrypt: ")
            key = int(input("Enter your desired encryption key (shift value): "))
            encryptedText = caesar_cipher(plainText, key)
            print(encryptedText)

         # Decryption   
        elif choice == 2:
            encryptedText = input("Enter the endoded message you want to decrypt: ")
            key = int(input("Enter the correct decryption key (shift value): "))
            reversedKey = key * -1
            decryptedText = caesar_cipher(encryptedText, reversedKey)
            print(decryptedText)
        else:
            print("Input an valid option 1 or 2")
    except ValueError:  
        print("That's not a valid number!")
    print("Do you want to perform another Caeser operation? y/n")
    option = input()


