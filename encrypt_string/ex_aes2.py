from Crypto import Random
from Crypto.Cipher import AES
import base64
import os


BS = 16
# pad = lambda s: s[:-ord(s[len(s)-1:])]
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]


class AESCipher:

    def __init__(self, key):
        self.key = key

    def encrypt(self, normal):
        normal = pad(normal)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(normal))

    def decrypt(self, encrypted):
        encrypted = base64.b64decode(encrypted)
        iv = encrypted[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(encrypted[16:]))


key = os.urandom(BS)

a = AESCipher(key)
b = a.encrypt('precio')
print 'encrypted: ' + b
c = a.decrypt(b)
print 'decrypted: ' + c
