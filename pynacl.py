
import nacl.secret
import nacl.utils
import nacl.encoding
import nacl.hash
import base64
import nacl.pwhash

# uses the sha 256 or sha 512 to create a hash for the given message
# and returns the message in string format
def nacl_hashing(message, sha=256):

    if sha == 512:
        hasher = nacl.hash.sha512
    else:
        hasher = nacl.hash.sha256
    message = message.encode('utf-8')
    digest = hasher(message, encoder=nacl.encoding.HexEncoder)
    return digest.decode('utf-8')


#password hashing uses key-streching algorithms like argon2, argon2i and scrypt
def get_password_hash(password, algo=None):
    if not isinstance(password, bytes):
        password = password.encode('utf-8')
    if not algo:
        hashed = nacl.pwhash.str(password)
    elif algo == "argon2i":
        hashed = nacl.pwhash.argon2i.str(password)
    elif algo == "scrypt":
        hashed = nacl.pwhash.scrypt.str(password)
    elif algo == 'argon2id':
        hashed = nacl.pwhash.argon2id.str(password)
    return base64.b64encode(hashed)

#verifies the given hash with the password
def verify_password_hash(password, hash):
    if not isinstance(password, bytes):
        password = password.encode('utf-8')
    hash = base64.b64decode(hash)
    try:
        nacl.pwhash.verify(hash, password)
        return True
    except:
        return False


# to create instances of secret key using nacl.secret.SecretBox
# for the encryption and decryption methods
# hashes the given key using sha256 to create the actual secret key for nacl.secret.SecretBox
class nacl_secretkey():

    def __init__(self,key,message):
        # initialises a secret key and message in byte format
        self.key = nacl_hashing(key)[:32].encode('utf-8')

        if isinstance(message, bytes):
            self.message= message
        else:
            self.message = message.encode('utf-8')
        if len(key) != 32:
            raise Exception("Not right length of 32 bytes")

        # uses the built in method to create an instance of the class of nacl.secret.SecretBox
        # that eventually encrypts and decrypts using XSalsa20 stream Cipher
        self.box = nacl.secret.SecretBox(self.key)

# encrypts the text using the given key
# returns the encrypted text (byte format)
# by performing a symmetric key encryption (XSalsa20 stream cipher)
def nacl_secret_key_encrypt_text(key,text):
    # encrypted_text = self.box.encrypt(self.message)
    if not isinstance(key, bytes):
        secret = nacl_secretkey(key, text)
    else:
        raise Exception("key is in bytes")
    encrypted_text = secret.box.encrypt(secret.message)
    # return encrypted_text,('\\').join(str(encrypted_text).split("\\"))[2:-1]]
    return base64.b64encode(encrypted_text)

# decrypts the text using the given key
# returns the decrypted text by performing a symmetric key encryption (XSalsa20 stream cipher)
def nacl_secret_key_decrypt_text(key, text):
    # plaintext = self.box.decrypt(self.encrypted)
    if not isinstance(key, bytes):
        secret = nacl_secretkey(key, text)
    else:
        raise Exception("Key or string is in bytes")

    plaintext = secret.box.decrypt(secret.message)
    return plaintext.decode('utf-8')


# text = nacl_secret_key_encrypt_text("qwertyuiopasdfghjklzxcvbnmqwerty","hamza")
# decrypted = nacl_secret_key_decrypt_text("qwertyuiopasdfghjklzxcvbnmqwerty", base64.b64decode(text))


