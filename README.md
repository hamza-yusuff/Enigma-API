# Enigma-API

## API - https://97i6zt.deta.dev/docs#/

This API provides access to several encryption and hashing functions. It essentially allows the user to obtain hashes, keys and
encrypted, as well as decrypted, text by exposing existing encryption ciphers and hashing algorithms. In addition to that, the
API has three endpoints, which when given a certain number of parameters, provides the user with prime numbers of any length of
bits. I have built this API using FastAPI to leverage it's async, await and high performance features, which ultimately compensates for the complexities of the encryption and hashing algorithms used.

I have used PyNaCl cryptographic library , which happens to be a Python binding to libsodium (fork of the Networking and Cryptography
library), for some of the endpoints which provide symmetric key encryption and hashing, and for Advanced Encryption Standard (AES), I have built the API endpoint using the CBC mode of AES encryption cipher of PyCryptodome library. The API provides 18 endpoints in total, with half of them facilitating encryption/decryption ciphers through POST request, and the other half does so through GET.
Currently, the API exposes functions for the following ciphers, algorithms and hashes-

- Vigener Cipher (Complete implementation on my own)
- Caesar Cipher (Complete implementation on my own)
- Symmetric Key Cipher of PyNacl library (uses XSAlsa20 stream cipher)
- Advanced Encryption Standard (CBC Mode) of PyCryptodom library
- RSA (Rivest–Shamir–Adleman) -- Assymetric Key Cipher (Complete implementation on my own, and have made some changes )
- Password Hashing -- using key-stretching algos like argon2, argon2i and scrypt from PyNaCl library
- Hashing using SHA 256 or SHA 512 as implemented in PyNaCl library
- Prime Number Retrieval Algorithms - using the PyCryptodom library

For a detailed discussion of the endpoints and corresponding algorithms used, you can continue reading below, otherwise you can skip
ahead to the console of the api - https://qe73tu.deta.dev/docs#/

## Table of Contents

- [Inspiration](#inspire)
- [Why FastAPI](#fastapi)
- [Usage](#usage)
- [PyNacl Cryptography](#pynacl)
- [PyCryptodome](#pycrypto)
- [HRSA (Implementation of RSA)](#rsa)
- [Caesar Cipher](#caesar)
- [Vigenere Cipher](#vig)
- [Primes](#prime)
- [RSA Public and Private Keys](#keys)
- [Improvements](#improvements)
- [Disclaimer](#disclaimer)
- [Contribution](#contribute)
- [Author](#author)

## Inspiration

<a name='inspire'>

My first foray into the world of computer science was through the world of cryptography. To be more precise, the movie- The Imitation Game - imprinted itself in the mind of 13 year old budding math enthusiastic, me. Ever since then, my interest gradually turned into a commitment to the subject of computer science. To the layman, this field may be limited to computers, but I have discovered over time that in this subject’s core lies complex computations, intricate networks, and an extraordinary need for original thinking.

## WHY FASTAPI (JUST MY THOUGHTS AND THANKS)

<a name='fastapi'>

When it comes to high performance, the existing python web frameworks have always been slow in comparison to their contemporaries, like NodeJS and Go. Also, the cPython implementation of GIL(global interpreter lock) has been a pain for async, await and multi-threading operations with python. Even though, Django has recently added support for async operations, Django channels for instance, it still has a long way to go to compete with NodeJS.

FastAPI seems to have answers to these problems. It’s one of the fastest python web frameworks available and it’s performance is on par with NodeJS and Go. More so, I have found it to be very intuitive to learn and use. Undoubtedly, it has improved the speed of Engima API, as speed is an issue because of the highly complex operations being used by the algorithms for the endpoints.
The reason for this high speed and unconventional provision of asyncio services could be because of the fact that FastAPI was built on starlette ( web framework which suppors ASGI) , and starlette uses uvicorn. The hierarchy is like –
Uvicorn (ASGI Server) -> Starlette (uses Uvicorn) a web framework) -> FastAPI (uses Starlette) an API microframework with several additional features for building APIS, with data validation, etc.

Initially, my plan was to use either Django REST Framework or Flask to built the API, but after comparing Fast API with the other two, I could not stop myself from using FastAPI for this project.

In short, for anyone willing to learn something new for building their APIs, I would highly recommend them to give FastAPI a try.
For more info - https://fastapi.tiangolo.com/

# USAGE

<a name='usage'>

The following are the endpoints of this API -

## Endpoints which facilitate POST Request

### PyNacl

<a name='pynacl'>

PyNaCl is a Python binding to libsodium, which is a fork of the Networking and Cryptography library, and LibSodium is a modern, easy-to-use software library for encryption, decryption, signatures, password hashing and more. These libraries have a stated goal of improving usability, security and speed. More importantly, it does not require the developer to decide which encryption technique to use, and thus largely takes away the stress of knowing the underlying of a cipher and it’s potential vulnerabilities, making the process of encrypting/decrypting data more seamless. In short, it prevents the user from doing cryptography in an insecure way.

It by default provides the most secured and resistant mode of encryption, (for both symmetric and asymmetric) along with the required padding. Currently, it stands as one of the best libraries for cryptography. For more info - https://pynacl.readthedocs.io/en/stable/

### PyNacl Symmetric Key Encryption and Decryption

Symmetric Key Encryption is analogous to a locking/unlocking a safe. With the given key, you can encrypt and decrypt the data to view the contents. The implementation of this encryption is done through pynacl secret key encryption library, which uses XSalsa20 stream cipher to perform the algorithm with the given key. The decryption is also done using the same cipher.

The key passed in the request body must be of 32 bytes and should be kept secret. It is the combination to your “safe” and anyone with this key will be able to decrypt the data, or encrypt new data. To add a layer of randomness, I added some changes to the way the key gets used for the encryption at the end.

#### Encryption

https://97i6zt.deta.dev/nacl/encrypt/

![naclE1](https://user-images.githubusercontent.com/63330003/117166608-59783480-ade8-11eb-9960-74d3204019af.PNG)

![naclE2](https://user-images.githubusercontent.com/63330003/117166630-5e3ce880-ade8-11eb-9624-4790171a3d7f.PNG)

#### Decryption

https://97i6zt.deta.dev/nacl/decrypt/

Notice, in the decryption the same encyrpted text obtained from the encryption API is used along with the same key.

![naclD1](https://user-images.githubusercontent.com/63330003/117166646-609f4280-ade8-11eb-98cf-ee6bf1bb0f81.PNG)

![naclD2](https://user-images.githubusercontent.com/63330003/117166654-63019c80-ade8-11eb-94bd-dbb687b4702f.PNG)

### PyCryptodom

<a name='pycrypto'>

PyCryptodome is a self-contained Python package of low-level cryptographic primitives. PyCryptodome is a fork of PyCrypto. I have used pycrtodome to implement Advanced Standard Encryption ( CBC mode) , and for those who are unaware of the AES, it’s essentially a symmetric key encryption, which uses the given key and an initialization vector ( a 128 bit round key) followed by multiple rounds of permutation and substitution on a 4x4 block of array of bytes to generate the encrypted text.
For more detailed explanation of AES, you can visit the link https://en.wikipedia.org/wiki/Advanced_Encryption_Standard

### Advanced Standard Encryption ( CBC mode)

The key passed in the request body must be either of 128 or 192 or 256 bits, and the key should be kept safe. The mode should be set to "CBC".

#### Encryption

https://97i6zt.deta.dev/cryptodom/aes/encrypt/

![aesE1](https://user-images.githubusercontent.com/63330003/117168830-5716da00-adea-11eb-9edf-f55816fc30b7.PNG)

![aesE2](https://user-images.githubusercontent.com/63330003/117168844-59793400-adea-11eb-8db3-7250e7835263.PNG)

#### Decryption

https://97i6zt.deta.dev/cryptodom/aes/decrypt/

Notice for the Decryption, the endpoint must be provided with a dict containing the initialization vector and encrypted text
obtained from the endpoint which provides the encrypted text, along with the key.

![aesD1](https://user-images.githubusercontent.com/63330003/117169066-934a3a80-adea-11eb-8dae-ac375b60d810.PNG)

![aesD2](https://user-images.githubusercontent.com/63330003/117169080-97765800-adea-11eb-976a-1103ddef6509.PNG)

### HRSA (Implementation of RSA)

<a name='rsa'>

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym RSA comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977.

I implemented this algorithm completely on my own and added changes to the original encryption so that only two prime numbers whose products happen to be larger than 100 would work. However, to ensure the maximum security, its best to use prime numbers of length more than 128 bits and the more the better. To get such HUGE prime numbers, you can use the prime number retrieval endpoints of this Enigma API. More information about the endpoints is given below.
The Algroithm works for all characters with an ASCII value greater than 31, including all alphanumeric characters.

To get the public and private key for RSA,you can use the GET endpoints available in this API.

To know more about RSA, you visit the link - https://en.wikipedia.org/wiki/RSA_(cryptosystem)

#### Encryption

https://97i6zt.deta.dev/hrsa/encryption/

The prime numbers p1 and p2 used to obtain, the private key for encryption, must have a product of greater than 100.

![hrsaE1](https://user-images.githubusercontent.com/63330003/117171420-aa8a2780-adec-11eb-8e7c-003f37b5385e.PNG)

![hrsaE2](https://user-images.githubusercontent.com/63330003/117171434-ae1dae80-adec-11eb-9014-44e095fa0658.PNG)

### Decryption

https://97i6zt.deta.dev/hrsa/decryption/

![hrsaD1](https://user-images.githubusercontent.com/63330003/117171675-e624f180-adec-11eb-8552-ba98bfb43d77.PNG)

![hrsaD2](https://user-images.githubusercontent.com/63330003/117171684-e8874b80-adec-11eb-9491-6a8bbd2a896f.PNG)

### Hashing

<a name='hashing'>

Cryptographic secure hash functions are irreversible transforms of input data to a fixed length digest.

The standard properties of a cryptographic hash make these functions useful both for standalone usage as data integrity checkers, as well as black-box building blocks of other kind of algorithms and data structures.

The endpoints below use hashing algorithms from the PyNacl libaray, and hence are well tested and safe to use.
To know more, you can visit the two links below -

- https://pynacl.readthedocs.io/en/stable/hashing/
- https://pynacl.readthedocs.io/en/stable/password_hashing/

#### Normal Hashing

To use this endpoint, you must specifiy the type of hash function (SHA - 256 or 512) you would like to use for the given message in the request body.
The hash functions available are sha 256 and 512.
To know more - https://en.wikipedia.org/wiki/SHA-2

https://97i6zt.deta.dev/nacl/hashing/

![naclhashing1](https://user-images.githubusercontent.com/63330003/117173764-ec1bd200-adee-11eb-854d-f0c57b686e9c.PNG)

![naclhashing2](https://user-images.githubusercontent.com/63330003/117173779-ee7e2c00-adee-11eb-8e14-bb611de03f3c.PNG)

#### Password Hashing

https://97i6zt.deta.dev/nacl/passwordhash/

To use this endpoint, you must specify the desired key stretching algorithm in the request body and the ones available are - argon2id, argon2i, scrypt.

![naclpasswordhash1](https://user-images.githubusercontent.com/63330003/117174198-49b01e80-adef-11eb-8616-f3cb1b1a3dc7.PNG)

![naclpasswordhash2](https://user-images.githubusercontent.com/63330003/117174235-53d21d00-adef-11eb-8334-f12b4345804b.PNG)

#### Password Hashing Verfiy

https://97i6zt.deta.dev/nacl/verifypasswordhash/

For using this endpoint, you have to provide the password/text along with its corresponding hash, generated from the endpoint
password hashing ( right above) . If the hashing provided is of the password/text given in the request body, then the endpoint returns true, otherwise returns false.

![verifyhash1](https://user-images.githubusercontent.com/63330003/117174662-c6db9380-adef-11eb-8b9c-7cb24e655f6b.PNG)

![verifyhash2](https://user-images.githubusercontent.com/63330003/117174670-c8a55700-adef-11eb-92ac-22371bde2009.PNG)

## Endpoints which facilitate GET Request

### Caesar Cipher

<a name='caesar'>

Implemented the Caesar Cipher completely on my own, and exposed the algorithm with the following endpoint below. It works on both positive and negative shift, and to use the endpoint, you must provide the text to be encrypted and the shift to be used on the text.

#### Encrypts the message with the given Shift and Caesar Cipher

https://97i6zt.deta.dev/caesarencrypt/{message}/{shift}/

![caesarE](https://user-images.githubusercontent.com/63330003/117176621-e2e03480-adf1-11eb-97dc-be1de8a9fb88.PNG)

#### Decrypts the encrypted message with the given Shift and Caesar Cipher

https://97i6zt.deta.dev/caesardecrypt/{message}/{shift}/

![caesarD](https://user-images.githubusercontent.com/63330003/117176676-eecbf680-adf1-11eb-860b-69c5310345da.PNG)

### Vigenere Cipher

<a name='vig'>

Implemented the Vigenere Cipher completely on my own, and exposed the algorithm with the following endpoint below. It works on key of any length, and to use the endpoint, you must provide the text to be encrypted and the key to be used on the text.
Howevere, the cipher implemented works best with lowercase letters only.

#### Encrypts the message with the given Key and Vigenere Cipher

https://97i6zt.deta.dev/vigenereencrypt/{message}/{key}/

![vigenreE](https://user-images.githubusercontent.com/63330003/117177011-5b46f580-adf2-11eb-8219-f42e35607c5c.PNG)

#### Decrypts the message with the given Key and Vigenere Cipher

For the decryption, you just have to provide the encrypted message and the same key used for encryption

https://97i6zt.deta.dev/vigeneredecrypt/{message}/{key}/

### Prime Numbers

<a name='prime'>

The mere existence of prime numbers has always been a mystery to me, and at this point, I can quite confidently say whoever is reading this would be aware of the importance of prime numbers in cryptography.
If you need a refresher on the definition of a prime number, it's a number larger than 1 that's divisible only by itself and 1.
If I had to put it simply, modern encryption algorithms exploit the fact that we can easily take two large primes and multiply them together to get a new, super-large number, but that no computer yet created can take that super-large number and quickly figure out which two primes went into making it.
Using this particular complexity, public key cryptography, such as RSA, use prime numbers to encrypt/decrypt data.
To know more, you can visit the link - https://math.berkeley.edu/~kpmann/encryption.pdf
Below, the following endpoints allows you to retrieve large prime numbers quickly, and all you have to do is just provide the length of prime number ( length in bits). You can use the endpoints to generate large primes for RSA.

#### Prime number generation using a unique ID

Generates a prime number of length k bits by extracting a unique value from the ID given as parameter. To look into the algorithm I used, you can view the source code in the eucild_prime.py file.

https://97i6zt.deta.dev/hrsaprime/{ID}/

![primeID](https://user-images.githubusercontent.com/63330003/117179414-e628ef80-adf4-11eb-9d5b-f724847b04f1.PNG)

#### Prime number generation using the desired length (n)

Generates a prime number of n bits ( n of the parameter)

https://97i6zt.deta.dev/nprime/{n}/

![nprimebits](https://user-images.githubusercontent.com/63330003/117179516-035dbe00-adf5-11eb-81ea-7b723e1690e0.PNG)

#### List of k Prime number generation of specific lengths

Generates a list of k (length of list) prime numbers, which contains one prime number of all lengths starting from 'start' (length of bits) bits to 'end' bits (length of bits) K must be equal to the value start-end+1 . To look into the algorithm I used, you can view the source code in the eucild_prime.py file.

https://97i6zt.deta.dev/kprime/{k}/{start}/{end}/

![listprime1](https://user-images.githubusercontent.com/63330003/117179725-3c962e00-adf5-11eb-9af5-e0afad0a0a78.PNG)

![listprime2](https://user-images.githubusercontent.com/63330003/117179734-3ef88800-adf5-11eb-8eb3-5b1054adfc97.PNG)

### RSA Public and Private Keys

<a name='keys'>

Implemented the Extended Euclidean Algorithm, along with RSA cipher completely on my own to generate the desired public key and the
corresponding private key. To look into the algorithm I used, you can view the source code in the keys.py and prime_euclid.py file.

#### PUBLIC KEY RSA

Computes and returns the public key for RSA cipher using the prime numbers p1 and p2. Product of p1 and p2 must be greater than 100 for the algorithm to work correctly.

https://97i6zt.deta.dev/hrsa/publickey/{p1}/{p2}/

![hrsapublic](https://user-images.githubusercontent.com/63330003/117180253-d067fa00-adf5-11eb-976b-1a4fea65206e.PNG)

#### PRIVATE KEY RSA

Computes and returns the private key for RSA cipher using the prime numbers p1,p2 and the public key e. Product of p1 and p2 must be
greater than 100 for the algorithm to work correctly.

https://97i6zt.deta.dev/hrsa/hrsa/privatekey/{e}/{p1}/{p2}/

![hrsaprivate](https://user-images.githubusercontent.com/63330003/117180306-e07fd980-adf5-11eb-9d2c-6086f88fff4e.PNG)

## Improvements

<a name='improvements'>

In the foreseeable future, I would like to add endpoints to authenticate users and allow them to
store their keys throught the API. That way, they do not have to send the cryptographic keys in
request body every time they make a call for the desired resource. This is important beacuse sending keys can jeopardize the whole process of encryption/decryption. Basically, I will soon integrate database to the API.

## Disclaimer

<a name='disclaimer'>

I have built this project to explore and learn about the world of cryptography, with a renewed sense of curosity. Hence, it's made purely for learning purposes. However, anyone willing to use this API is more than welcome to do so. Thanks!

## Contributing

<a name='contribute'>

Bug reports and pull requests are welcome on GitHub at @hamza-yusuff

## Author

<a name='author'>

Hamza Yusuff - Email: [hbyusuff@uwaterloo.ca](#hbyusuff@uwaterloo.ca)
