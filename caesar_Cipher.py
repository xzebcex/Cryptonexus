# caesarCipher


# The string to be encrypted/decrypted:
# message = 'This is my secret message.'
secretMessage = input("Enter the cipher to be encrypted/decrypted: ")

# The encryption/decryption key:
# key = 13
key = int(input("Enter the encryption/decryption key: "))

# Whether the program encrypts or decrypts:
# mode = 'encrypt'  # Set to either 'encrypt' or 'decrypt'.
mode = input("Enter the mode (encrypt/decrypt): ")

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?'

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in secretMessage:
    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

  # Perform encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

# Handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)

        translated += SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated += symbol

    # Output the translated string:
print(translated)

