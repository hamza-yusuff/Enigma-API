from Crypto.Cipher import AES
from Crypto.Util.Padding import  pad
from Crypto.Util.Padding import unpad
import base64
#For AES key can be 128 or 192 or 256 bits


# aes_encrypt uses AES encryption to encrypt the given message
# the mode of AES can be specified from either CBC or EAX
# the function uses CBC as default
# the key has to be either 128 or 192 or 256 bits
# return a dictionary with initialization vector and ciphertext if CBC used and
# return a dictionary with tag, nonce and ciphertext fields if EAX used
def AES_encrypt(key, message, mode="CBC"):
    key_length = len(key)
    if (key_length==16 or key_length==24 or key_length==32):
        key = key.encode('utf-8')
        message = message.encode('utf-8')
        if (mode == "CBC"):
            cipher = AES.new(key, AES.MODE_CBC)

            initial_vector = base64.b64encode(cipher.iv)
            ciphertext = cipher.encrypt(pad(message, AES.block_size))
            ciphertext = base64.b64encode(ciphertext)

            return {"iv": initial_vector, "ciphertext": ciphertext}
        # elif (mode == "EAX"):
        #     cipher = AES.new(key, AES.MODE_EAX)
        #     ciphertext, tag = cipher.encrypt_and_digest(message)
        #     tag = base64.b64encode(tag)
        #     ciphertext = base64.b64encode(ciphertext)
        #     nonce = base64.b64encode(cipher.nonce)
        #     return {"tag":tag, "nonce":nonce, "ciphertext":ciphertext}
        else:
            raise Exception("Mode not supported")
    else:
        raise Exception("Key length has to be 128 or 192 or 256 bits")




# aes_decrypt uses AES cipher to decrypt the given encrypted message
# the mode of AES can be specified from either CBC or EAX
# the function uses CBC as default
# the key has to be either 128 or 192 or 256 bits
# parameter info should have tag,nonce and ciphertext fields if EAX mode used and
# parameter info should have iv and ciphertext fields if CBC used
# returns the plaintext or decrypted message
def AES_decrypt(key, info,mode="CBC"):
    key_length = len(key)
    if (key_length == 16 or key_length == 24 or key_length == 32):

        if (mode=="CBC"):

            iv = base64.b64decode(info["iv"])
            ciphertext = base64.b64decode(info["ciphertext"])
            cipher_decrypt = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
            plaintext = unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
            return plaintext.decode()
        # elif (mode=="EAX"):
        #     nonce = base64.b64decode(info["nonce"])
        #     tag = base64.b64decode(info["tag"])
        #     ciphertext = base64.b64decode(info["ciphertext"])
        #     cipher = AES.new(key.encode('utf-8'), AES.MODE_EAX, nonce)
        #     data = cipher.decrypt_and_verify(ciphertext,tag)
        #     return data.decode()
        else:
            raise Exception("Mode not supported")

    else:
        raise Exception("Key length has to be 128 or 192 or 256 bits")


# data=aes_encrypt('mysecretpassword', 'this is my message',"CBC")
# print(aes_decrypt('mysecretpassword',data))