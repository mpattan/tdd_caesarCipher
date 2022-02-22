import sys


def get_cipher_value(cipher_input):
    return sum([ord(character) for character in cipher_input])

def encrypt(string_input, cipher):
    string_output = ""
    for char in string_input:
        if char.isupper():
            string_output += chr(((ord(char)-65)+cipher)%26+65)
        else:
            string_output += chr(((ord(char)-97)+cipher)%26+97)
    return string_output



action = sys.argv[1]
string_input = sys.argv[2]
cipher_input = sys.argv[3]

cipher = get_cipher_value(cipher_input)

if action == 'encrypt':
    output = encrypt(string_input, cipher)

print(output)
