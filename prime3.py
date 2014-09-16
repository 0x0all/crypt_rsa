# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
import base64

def make_keys(bits=2048):
    new_key = RSA.generate(bits) 
    public_key = new_key.publickey().exportKey("PEM") 
    private_key = new_key.exportKey("PEM") 
    
    with open("public_key.pem", "w") as f:
        f.write(public_key)
        f.close()
    
    with open("private_key.pem", "w") as f:
        f.write(private_key)
        f.close()
        
def encrypt_RSA(public_key_loc, message):
    key = open(public_key_loc, "r").read()
    rsakey = RSA.importKey(key)
    encrypted = base64.b64encode(rsakey.encrypt(message, 0)[0])

    return encrypted

def decrypt_RSA(private_key_loc, package):
    key = open(private_key_loc, "r").read() 
    rsakey = RSA.importKey(key) 
    decrypted = rsakey.decrypt(base64.b64decode(package)) 
    return decrypted    
    
# make_keys()
# exit()
# -----
message = open("text1", "r").read().strip()
print encrypt_RSA("public_key.pem", message)
exit()
# -----
message2 = open("text2", "r").read().strip()
print decrypt_RSA("private_key.pem", message2)
