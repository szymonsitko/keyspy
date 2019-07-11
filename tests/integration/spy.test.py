import sys
import os
import unittest

sys.path.append(os.getcwd())
from main import KeySpy
from constants.hex_codes import HEX_CODES


class KeySpyTest(unittest.TestCase):
    def test_new_spy_instance(self):
        key_spy = KeySpy()
        self.assertEqual(key_spy.hex_codes, HEX_CODES)


if __name__ == "__main__":
    unittest.main()
