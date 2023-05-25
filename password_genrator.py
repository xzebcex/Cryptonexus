# Random Password Generator.

import random


def create_password_generator(characters):
    def create_password(length):
        output = []
        for i in range(length):  # How long do we want the password to be.
            # Add a new random element from characters to output.
            output.append(random.choice(characters))
        # Return a string based on the elements of output.
        return ''.join(output)
    return create_password  # Returns the inner functionto the caller.


alpha_numeric_symbols = create_password_generator(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%0123456789')

password = f"You'r Password > {alpha_numeric_symbols(int(str(input('Enter the desired length of your password: '))))}"
print(password)
