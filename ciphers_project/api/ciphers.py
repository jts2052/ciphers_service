def caesar_encode(plain_text, shift):
    cipher_text = ''
    for c in plain_text:
        if c.isalpha():
            if c.islower():
                c_encoded = ord('a') + (ord(c) - ord('a') + shift) % 26
            else:
                c_encoded = ord('A') + (ord(c) - ord('A') + shift) % 26
            cipher_text += chr(c_encoded)
        else:
            cipher_text += c
    return cipher_text