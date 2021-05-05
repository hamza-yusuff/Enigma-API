from prime_euclid import *
import random

# computes and returns the public key of the two primes prime1 and prime2
# using RSA algorithm
def find_public(prime1, prime2):
    phi = (prime1-1)*(prime2-1)
    n = prime1*prime2
    public=0
    x = max(prime1, prime2)
    y = min(prime1, prime2)
    nonce = random.randint(y,x) # adds another layer of randomization
    for i in range(2, phi):
        if gcd_euclid(i,n)==1 and gcd_euclid(i,phi)==1:
            public = i
            if nonce==x or nonce ==y:
                break
    if public == 0:
        return "No key found"
    else:
        return public

# computes and returns the private key of the e,prime1,prime2 by finding the
# the inverse of e and phi(prime1*prime2) for which the gcd of e and phi is 1
def find_private(e,prime1,prime2):
    phi = (prime1-1)*(prime2-1)
    gcd,x,y = gcd_extended_euclid(e, phi)
    if gcd == 1:
        return x%phi
    else:
        return "Private key does not exist for the given values"

# generates a dict of the public key and the number to be used for modular operation
def generate_public_key(prime1,prime2):
    modulo = prime1*prime2
    res = find_public(prime1,prime2)

    if res == "No key found":
        raise Exception(res)
    else :
        return {"public": res, "modulo": modulo}

# generate a dict of the private key and the number to be used for modular operation
def generate_private_key(e,prime1,prime2):
    modulo = prime1*prime2
    res = find_private(e,prime1, prime2)

    if res == "Private key does not exist for the given values":
        raise Exception(res)
    else:
        return {"private": res, "modulo": modulo}

