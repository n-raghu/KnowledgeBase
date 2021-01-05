import string


def cipher_using_lookup(text, key, characters = string.ascii_letters, decrypt=False, shift_type="right"):
    n = len(characters)

    if decrypt:
        key = n - key

    if shift_type=="left":
        # if left shift is desired, we simply inverse they sign of the key
        key = -key
    table = str.maketrans(characters, characters[key:]+characters[:key])
    return text.translate(table)


if __name__ == '__main__':
    enc_1 = cipher_using_lookup('This is Full Water', 9)
    print(enc_1)
    print(cipher_using_lookup(enc_1, 9, decrypt=True))
