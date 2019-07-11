import sys
import os
import unittest

sys.path.append(os.getcwd())
from lib.replace_surroundings import replace_surroundings


class ReplaceSurroundings(unittest.TestCase):
    def test_remove_both_chars_surrounding(self):
        char_to_replace = "'"
        example_input = "'something'"
        output = replace_surroundings(char_to_replace, example_input)
        self.assertEqual(output, example_input[1:len(example_input) - 1])

    def test_string_not_containing_same_chars_surrounding(self):
        char_to_replace = "'"
        example_input = "'example-input@"
        output = replace_surroundings(char_to_replace, example_input)
        self.assertEqual(output, example_input)


if __name__ == "__main__":
    unittest.main()
