import unittest
from pdfminer.arcfour import Arcfour


class arcfour(unittest.TestCase):

    def decoding(self):
        s = Arcfour(b'Key').process(b'Plaintext').hex()
        self.assertEqual(s, 'bbf316e8d940af0ad3')