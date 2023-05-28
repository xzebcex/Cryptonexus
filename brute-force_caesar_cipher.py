# Brute-force Caesar Cipher.

# Default message is ('Unveil') with key 13.
message = 'h19rvy'  
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?'

# Loop through every possible key.
for key in range(len(SYMBOLS)):
    translated = ''

    # Loop through each symbols in message.
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = symbol_index - key

            # Handle the wraparound.
            if translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)

                # Append the decrypted symbol.
                translated = translated + SYMBOLS[translated_index]
            else:
                # Append the symbol after encrypting/decrypting.
                translated = translated + SYMBOLS[translated_index]

    # Display every possible decryption.
    print('key #%s: %s' % (key, translated))
