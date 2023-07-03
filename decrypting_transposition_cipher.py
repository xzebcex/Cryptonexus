# Decryption of Transposition Cipher.

import math



def main():
    message = 'Miedeet me outs'  # message = Meet me outside.
    key = int(input('Enter the key: ')) # use key 12.

    plaintext = decrypted_message(key, message)

    # print with a '|' at the end of the decrypted message.
    print(plaintext + '|')

    


def decrypted_message(key, message):
    num_of_columns = int(math.ceil(len(message) / float(key)))
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)
    plaintext = [''] * num_of_columns

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1  # point to column.

        
        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            column = 0
            row += 1

    return ''.join(plaintext)


# call the main() function.
if __name__ == '__main__':
    main()
