# File Cipher.

import time
import os
import sys
import transposition_cipher # In order to run this program, you must include (transposition_cipher)
import decrypting_transposition_cipher # In order to run this program, you must include (decrypting_transposition_cipher)
 

def main():
    # 'demo.txt'  # input filename.
    input_filename = input(
        '\033[32mEnter the input filename e.g.[example.txt]\n> \033[0m')
    # BE CAREFUL! If a file with the outputFilename name already exists,
    # this program will overwrite that file.
    # 'demo.encrypted.txt'  # Output filename.
    output_filename = input(
        '\033[32mEnter the output filename e.g\n(example.encrypted.txt for encryption)\n(example.decrypted.txt for decryption)]\n> \033[0m')
    # 10  # Select key for cipher.
    key = int(input('\033[32mSelect a key e.g.(10)\n> \033[0m'))
    # set encrypt or decrypt.
    mode = input('\033[32mEnter Encrypt or Decrypt\n> \033[0m')

    # If the input file does not exist, the program terminates early.
    if not os.path.exists(input_filename):
        response = input('The file %s does not exist.' % (input_filename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(output_filename):
        response = input(
            'This will overwrite the file %s. [Y/N] ' % (output_filename))
        if not response.lower().startswith('y'):
            sys.exit()

    # Read in the message from the input file:
    fileObj = open(input_filename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (mode.title()))

    # Measure how long the encryption/decryption takes.
    start_time = time.time()
    if mode == 'encrypt':
        translated = encrypt_transposition_cipher.encrypted_message(key, content)
    elif mode == 'decrypt':
        translated = decrypt_transposition_cipher.decrypted_message(key, content)
    total_time = round(time.time() - start_time, 2)
    print('%sion time: %s seconds' % (mode.title(), total_time))

    # Write out the translated message to the output file.
    output_file_obj = open(output_filename, 'w')
    output_file_obj.write(translated)
    output_file_obj.close()

    print('Done %sing %s (%s characters).' %
          (mode, input_filename, len(content)))
    print('%sed file is %s.' % (mode.title(), output_filename))


# If transpositionCipherFile.py is run (instead of imported as a module),
# call the main() function:
if __name__ == '__main__':
    main()
