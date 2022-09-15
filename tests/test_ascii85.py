import unittest
from pdfminer.ascii85 import ascii85decode
from pdfminer.ascii85 import asciihexdecode


class Runlength(unittest.TestCase):

    def decoding(self):
        a = ascii85decode(b'9jqo^BlbD-BleB1DJ+*+F(f,q')
        self.assertEqual(a, b'Man is distinguished')

        b = ascii85decode(b'9jqo^BlbD-BleB1DJ+*+F(f,q')
        self.assertEqual(b, b'pleasure.')

        c = asciihexdecode(b'61 62 2e6364   65')
        self.assertEqual(c, b'ab.cde')

        d = asciihexdecode(b'61 62 2e6364   657>')
        self.assertEqual(d, b'ab.cdep')

        e = asciihexdecode(b'7>')
        self.assertEqual(e, b'p')