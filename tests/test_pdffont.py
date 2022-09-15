import unittest

from pdfminer.pdffont import get_widths
from pdfminer.pdffont import get_widths2

# assert get_widths([1]) == {}
# assert get_widths([1,2,3]) == {1:3, 2:3}
# assert get_widths([1,[2,3],6,[7,8]]) == {1:2,2:3, 6:7,7:8}

# assert get_widths2([1]) == {}
# assert get_widths2([1,2,3,4,5]) == {1:(3, (4,5)), 2:(3, (4,5))}
# assert get_widths2([1,[2,3,4,5],6,[7,8,9]]) == {1:(2, (3,4)), 6:(7, (8,9))}


class TestPffont(unittest.TestCase):

    def testPdffont_get_widths(self):
        self.assertEqual(get_widths([1]), {})
        self.assertEqual(get_widths([1, 2, 3]), {1: 3, 2: 3})
        self.assertEqual(get_widths([1, [2, 3], 6, [7, 8]]), {
                         1: 2, 2: 3, 6: 7, 7: 8})

    def testPdffont_get_widths2(self):
        self.assertEqual(get_widths2([1]), {})
        self.assertEqual(get_widths2([1, 2, 3, 4, 5]), {1: (3, (4, 5)),
                                                        2: (3, (4, 5))})
        self.assertEqual(get_widths2([1, [2, 3, 4, 5], 6, [7, 8, 9]]),
                         {1: (2, (3, 4)), 6: (7, (8, 9))})
