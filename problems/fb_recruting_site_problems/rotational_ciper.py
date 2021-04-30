# Rotational Cipher One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain
# amount. Rotating a character means replacing it with another character that is a certain number of steps away in
# normal alphabetic or numerical order. For example, if the string "Zebra-493?" is rotated 3 places, the resulting
# string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around
# from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to
# 0). Note that the non-alphanumeric characters remain unchanged. Given a string and a rotation factor,
# return an encrypted string. Signature string rotationalCipher(string input, int rotationFactor) Input 1 <= |input|
# <= 1,000,000 0 <= rotationFactor <= 1,000,000 Output Return the result of rotating input a number of times equal to
# rotationFactor. Example 1 input = Zebra-493? rotationFactor = 3 output = Cheud-726? Example 2 input =
# abcdefghijklmNOPQRSTUVWXYZ0123456789 rotationFactor = 39 output = nopqrstuvwxyzABCDEFGHIJKLM9012345678

# Add any extra import statements you may need here


# Add any helper functions you may need here

def cipher_char(c, rotation_factor):
    if c.islower():
        return chr(97 + (((ord(c) % 97) + rotation_factor) % 26))

    if c.isupper():
        return chr(65 + (((ord(c) % 65) + rotation_factor) % 26))

    if c.isnumeric():
        return chr(48 + (((ord(c) % 48) + rotation_factor) % 10))

    return c


def rotational_cipher(input_string, rotation_factor):
    return "".join(cipher_char(c, rotation_factor) for c in input_string)


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def print_string(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    right_tick = '\u2713'
    wrong_tick = '\u2717'
    if result:
        print(right_tick, 'Test #', test_case_number, sep='')
    else:
        print(wrong_tick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        print_string(expected)
        print(' Your output: ', end='')
        print_string(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotational_cipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotational_cipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    # Add your own test cases here
