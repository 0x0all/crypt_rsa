# -*- coding: utf-8 -*-

# http://en.wikipedia.org/wiki/Modular_multiplicative_inverse

# p, q - prime numbers 
p = 3557
q = 2579
e = 3

# e = 3, 5, 17, 257, 65537, 4294967297, 18446744073709551617
# 1 < e < phi

secret_text = 111111

n = p*q
phi = (p-1)*(q-1)

def inverse(a, n):
    t = 0
    newt = 1    
    r = n
    newr = a    
    while (newr != 0):
        quotient = r / newr
        t, newt = newt, t - quotient * newt 
        r, newr = newr, r - quotient * newr
    if r > 1:
        return "a is not invertible"
    if t < 0:
        t += n
        
    return t

d = inverse(e, phi)

print d

open_key = [e, n]
secret_key = [d, n]

# crypt ------------
print "crypt: ",
# c = (secret_text**e) % n
c = pow(secret_text, e, n)
print c

# decrypt ----------
print "decrypt: ",
# m = (c**d) % n
m = pow(c, d, n)
print m
