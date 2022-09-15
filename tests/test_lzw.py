import unittest
from pdfminer.lzw import lzwdecode


class Runlength(unittest.TestCase):

    def decoding(self):
        a = lzwdecode(bytes.fromhex('800b6050220c0c8501'))
        self.assertEqual(a, b'-----A---B')