


# --- vigenere cipher
# works best with lower case letters only

# implements the vigenere cipher on the given string, using the provided key
# the encrypted key is always given in lower case letters
def vigenere_encrypt(string, key):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    string_len = len(string)

    # checks and expands the key if its smaller than string
    key_len = len(key)
    while key_len < string_len:
        key +=key
        key_len = len(key)


    key_pos = 0
    encrypted =""
    for char in string:
        if char in chars:
            pos = chars.find(char)
            char_key = key[key_pos]
            char_key_pos = chars.find(char_key)
            key_pos += 1
            new_pos = (pos+char_key_pos)%26
            new_char = chars[new_pos]
            encrypted+=new_char
        else:
            encrypted+=char
    return encrypted



# implements the decryption of the vigenere cipher on the given string, using the provided key
def vigenere_decrypt(string, key):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    string_len = len(string)

    # checks and expands the key if its smaller than string
    key_len = len(key)
    while key_len < string_len:
        key += key
        key_len = len(key)

    key_pos = 0
    encrypted = ""
    for char in string:
        if char in chars:
            pos = chars.find(char)
            char_key = key[key_pos]
            char_key_pos = chars.find(char_key)
            key_pos += 1
            new_pos = (pos - char_key_pos) % 26
            new_char = chars[new_pos]
            encrypted += new_char
        else:
            encrypted += char
    return encrypted




#implements the caesar cipher and works on both upper case and lower case letters
# and  both negative positive shifts
def caesar_encrypt(word, shift):
    w = list(word)
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(w)):
        if w[i] in upper:
            index = upper.index(w[i])
            f = index + shift % 26
            if f >= 26:
                f = abs(26 - (index + shift % 26))

            w[i] = upper[f]
        elif w[i] in lower:
            index = lower.index(w[i])
            f = index + shift % 26
            if f >= 26:
                f = abs(26 - (index + shift % 26))

            w[i] = lower[f]
    encrypted = ''.join(w)
    return encrypted


#implements the decryptiono of caesar cipher and works on both upper case and lower case letters
#and  both negative positive shifts
def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher,-1*shift)

# string = "hamza yusuff is THE WORST hell ya 123"
# encrypt = caesar_encrypt(string,15)
# print(encrypt)
# text = caesar_decrypt(encrypt, 15)
# print(text)

