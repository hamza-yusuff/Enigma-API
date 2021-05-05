import fastapi
from fastapi import HTTPException
import uvicorn
from pynacl import *
from keys import generate_public_key, generate_private_key
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cryptodom import AES_encrypt, AES_decrypt
from rsacipher import *
from prime_euclid import *
from vs import *

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#Base model for post endpoints of Nacl library
class Code(BaseModel):
    key: str
    text: str


class Naclhash(BaseModel):
    message: str
    detail: str

class NaclVerify(BaseModel):
    password: str
    hash: str

#Base model for post endpoints of Cryptodom library
class AES(BaseModel):
    key: str
    text: str
    mode: str

#Base model for AES decryption of Cryptodom Library
class DES(BaseModel):
    key: str
    info: dict
    mode: str

#Base model for post endpoints of HRSA (RSA)
class Hrsa(BaseModel):
    text: str
    key: int
    n : int


#endpoint for getting encrypted message back using caesar cipher
@app.get('/caesarencrypt/{message}/{shift}/')
async def caesarencrypt(message: str, shift: int):
    try:
        return caesar_encrypt(message, shift)
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


#endpoint for getting encrypted message decrypted using caesar cipher
@app.get('/caesardecrypt/{cipher}/{shift}/')
async def caesardecrypt(cipher: str, shift: int):
    try:
        return caesar_decrypt(cipher, shift)
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


#endpoint for getting encrypted message back using vigenere cipher
@app.get('/vigenereencrypt/{message}/{key}/')
async def vigenereEncrypt(message: str, key: str):
    try:
        return vigenere_encrypt(message, key)
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


#endpoint for getting encrypted message decrypted back using vigenere cipher
@app.get('/vigeneredecrypt/{message}/{key}/')
async def vigeneredecrypt(message: str, key: str):
    try:
        return vigenere_decrypt(message, key)
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


# endpoint for getting hashed message back
@app.post('/nacl/hashing/')
async def hashing(naclhash: Naclhash):
   result = nacl_hashing(naclhash.message, naclhash.detail)
   return result

#endpoint for getting password hash
@app.post('/nacl/passwordhash/')
async def password_hashing(naclhash: Naclhash):
    try:
        result = get_password_hash(naclhash.message, naclhash.detail)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


#endpoint for verifying password with hash
@app.post('/nacl/verifypasswordhash/')
async def password_hashing(naclhash: NaclVerify):
    try:
        result = verify_password_hash(naclhash.password, naclhash.hash)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


#endpoint for nacl symmetric key encryption
@app.post('/nacl/encrypt/')
async def nacl_encrypt(code: Code):
    try:
        result = nacl_secret_key_encrypt_text(code.key, code.text)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


#endpoint for nacl symmetric key decryption
@app.post('/nacl/decrypt/')
async def nacl_decrypt(code: Code):
    try:
        result = nacl_secret_key_decrypt_text(code.key, base64.b64decode(code.text))
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")



#endpoint for aes encryption using cryptodom
@app.post('/cryptodom/aes/encrypt/')
async def aes_encrypt(aes: AES):
    try:
        result = AES_encrypt(aes.key, aes.text, aes.mode)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")

#endpoint for aes decryption using cryptodom
@app.post('/cryptodom/aes/decrypt/')
async def aes_decrypt(des: DES):
    try:
        result = AES_decrypt(des.key, des.info, des.mode)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


#endpoint for getting a random prime number using a unique id provided in the url
@app.get('/hrsaprime/{ID}')
async def hrsaprime(ID: str):
    try:
        result = hrsa_prime(ID)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


#endpoint for getting a n bits prime number
@app.get('/nprime/{n}')
async def nprime(n: int):
    try:
        result = generate_prime(n)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")

# endpoint exposes a function which
# computes and returns a list of k primes starting from a prime
# which is "start" length of bits and ending with a prime which has
# a length of "end" bits
@app.get('/kprime/{k}/{start}/{end}/')
async def nprime(k: int, start: int, end: int):
    try:
        result = generate_kprimes(k,start,end)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


# endpoint exposes the public key function of rsa
@app.get('/hrsa/publickey/{p1}/{p2}/')
async def hrsa_publickey(p1: int, p2: int):
    try:
        result = generate_public_key(p1,p2)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")

# endpoint exposes the private key function of rsa
@app.get('/hrsa/privatekey/{e}/{p1}/{p2}/')
async def hrsa_privatekey(e: int, p1: int, p2: int):
    try:
        result = generate_private_key(e,p1,p2)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")



# endpoint exposes the hrsacipher encryption function
@app.post('/hrsa/encryption/')
async def hrsa_encryption(hrsa: Hrsa):
    try:
        result = hrsa_encrypted(hrsa.text, hrsa.key, hrsa.n)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


# endpoint exposes the hrsacipher decryption function
@app.post('/hrsa/decryption/')
async def hrsa_decryption(hrsa: Hrsa):
    try:
        result = hrsa_decrypted(hrsa.text, hrsa.key, hrsa.n)
        return result
    except:
        HTTPException(status_code=404, detail="Algorithm could not compute the desired result")


# uvicorn.run(app)