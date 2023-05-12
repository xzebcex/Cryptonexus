# Reverse Cipher

secret_message = input('Enter cipher: ')
translated = ''

i = len(secret_message) - 1
while i >= 0:
    translated += secret_message[i]
    i -= 1

print(translated)
