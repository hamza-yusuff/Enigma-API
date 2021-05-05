from Crypto.Util import number
import math


#generates a n-bit prime number- fast for any length of n but advisable to have n less than 256
#requires: n to be at least greater than 8
def generate_prime(n):
    return number.getPrime(n)

#uses the unique id passed to extract a unique id for generating two primes
# returns a dict two primes
# requires : unique_id to be alphanumeric with a length greater than 10 and less than equal to 20
def hrsa_prime(unique_id):
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    nums ='0123456789'
    key = ''
    for char in unique_id:
        if char in nums:
            key+=char
        elif char in chars:
            key += str(chars.index(char))
    key = int(key)%256
    prime1 = generate_prime(key)
    prime2 = generate_prime(key)
    return {"prime1": prime1, "prime2": prime2}

# computes and returns a list of k primes starting from a prime
# which is "start" length of bits and ending with a prime which has
# a length of "end" bits
# requires: start>5
def generate_kprimes(k, start, end):
    numberofprimes = []
    if (k==end-start+1):
        bits = start
        for i in range(k):
            numberofprimes.append(number.getPrime(bits))
            bits+=1
        return numberofprimes
    else:
        return "K != end-start+1"


# computes the gcd of a and b, and returns the gcd
def gcd_euclid(a,b):
    return math.gcd(a,b)
#implements the extended euclidean algorithm to compute the coefficients
# and GCD of a and b of the linear diophantine equation found at the end
# of algorithm
def gcd_extended_euclid(a,b):

    if a == 0:
        return b,0,1
    gcd, x1, y1 = gcd_extended_euclid(b % a, a)
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y



