import unittest
from pdfminer.rijndael import RijndaelDecryptor


class Runlength(unittest.TestCase):

    def decoding(self):
        key = bytes.fromhex('00010203050607080a0b0c0d0f101112')
        ciphertext = bytes.fromhex('d8f532538289ef7d06b506a4fd5be9c9')
        aux = RijndaelDecryptor(key, 128).decrypt(ciphertext).hex()
        self.assertEqual(aux, '506812a45f08c889b97f5980038b8359')