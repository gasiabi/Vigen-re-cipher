alphabet_small = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś',
                  't', 'u', 'w', 'y', 'z', 'ź', 'ż']
alphabet_large = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś',
                  'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż']

dictionary = {
    'A': 0, 'Ą': 1, 'B': 2, 'C': 3, 'Ć': 4, 'D': 5,
    'E': 6, 'Ę': 7, 'F': 8, 'G': 9, 'H': 10, 'I': 11,
    'J': 12, 'K': 13, 'L': 14, 'Ł': 15, 'M': 16, 'N': 17,
    'Ń': 18, 'O': 19, 'Ó': 20, 'P': 21, 'R': 22, 'S': 23,
    'Ś': 24, 'T': 25, 'U': 26, 'W': 27, 'Y': 28, 'Z': 29,
    'Ź': 30, 'Ż': 31,
    'a': 0, 'ą': 1, 'b': 2, 'c': 3, 'ć': 4, 'd': 5,
    'e': 6, 'ę': 7, 'f': 8, 'g': 9, 'h': 10, 'i': 11,
    'j': 12, 'k': 13, 'l': 14, 'ł': 15, 'm': 16, 'n': 17,
    'ń': 18, 'o': 19, 'ó': 20, 'p': 21, 'r': 22, 's': 23,
    'ś': 24, 't': 25, 'u': 26, 'w': 27, 'y': 28, 'z': 29,
    'ź': 30, 'ż': 31
}


# uploading the key from the passwd.txt
def generate_the_key():

    key_text = 'passwd.txt'
    with open(key_text, 'r', encoding='utf-8') as f:
        key_word = f.read().strip()

    return key_word


# encrypting the text with vigenere cipher
def encrypt_the_text(text):
    key = generate_the_key()
    number = 0
    encrypted_text = []
    for letter in text:
        if letter in alphabet_large:
            value = dictionary[letter]
            new_letter = (dictionary[key[number]] + value) % len(alphabet_large)
            encrypted_text.append(alphabet_large[new_letter])
            number += 1
            if number >= len(key):
                number = 0
        elif letter in alphabet_small:
            value = dictionary[letter]
            new_letter = (dictionary[key[number]] + value) % len(alphabet_small)
            encrypted_text.append(alphabet_small[new_letter])
            number += 1
            if number >= len(key):
                number = 0
        else:
            encrypted_text.append(letter)

    final_encrypted_text = ''.join(encrypted_text)

    return final_encrypted_text


# uploading the file and encrypting the while file
def upload_the_file():
    file = 'plain.txt'
    new_file = 'substitute_proprietary.txt'

# utf-8 used to use Polish diacritical marks
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    encrypted_text = encrypt_the_text(text)

    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)

    return text


if __name__ == '__main__':
    upload_the_file()
