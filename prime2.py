from Crypto.PublicKey import RSA
RSAkey = RSA.generate(1024)
print "---"
print getattr(RSAkey.key, 'n')
print "---"
print getattr(RSAkey.key, 'p')
print "---"
print getattr(RSAkey.key, 'q')
