# Encrypting Transposition Cipher


def main():
    message = input('Enter the secret message: ') 
    # Sercret message = 'Unveiling secrets'

    key = int(input('Enter the key: '))

    ciphertext = encrypted_message(key, message)

    """Print the encrypted string in ciphertext to the screen,
    with a | after it in case there are spaces at the end of the 
    encrypted message. """
    print(ciphertext + '|')



def encrypted_message(key, message):
    # Each string in ciphertext represent a coloum in a grid.
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for column in range(key):
        current_index = column

        # Keep looping until current_index goes past the message length.
        while current_index < len(message):
            # Place the character at the current index in mesage at the end of the current column in the cipher text list.
            ciphertext[column] += message[current_index]

            # Move current index over.
            current_index += key

    return ''.join(ciphertext)


if __name__ == '__main__':
    main()
