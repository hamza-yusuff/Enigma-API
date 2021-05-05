from keys import *

characters = ['null', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_']

char_no_nums = ['null', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_']



#encrypts the message using RSA and the index of the character stored in array characters
# devised an algorithm along with RSA to encrypt all characters with an ascii value greater than 32
# requires n to be greater than 100
def hrsa_encrypted(message,public,n):
    cipher = ''
    for char in message:
        pos = characters.index(char)
        encrypt = pow(pos, public, n)
        encrypt = str(encrypt)+char_no_nums[random.randint(2,60)]
        cipher+=encrypt
    return cipher

# decrypts the message using RSA and the index of the character stored in array characters
# devised an algorithm along with RSA to decrypt all characters with an ascii value greater than 32
# requires n to be greater than 100, which means p and q need to be chosen such that their product
# is greater than 100
def hrsa_decrypted(cipher,private,n):
    valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    message = ''
    k=0
    length = len(cipher)
    while k<length:
        pos=''
        while k<length and cipher[k] in valid:
            pos+=cipher[k]
            k=k+1
        k+=1
        decrypt = pow(int(pos), private, n)
        message += characters[decrypt]
    return message



