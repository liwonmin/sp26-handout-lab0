"""Tests for Lab 0 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Test cases for the is_palindrome function"""

    def test_classic_palindrome_with_punctuation(self) -> None:
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

    def test_palindrome_with_spaces_and_case(self) -> None:
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_simple_palindromes(self) -> None:
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("12321"))

    def test_empty_and_whitespace(self) -> None:
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("   "))
        self.assertTrue(is_palindrome(" \t\n "))

    def test_non_palindromes(self) -> None:
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertFalse(is_palindrome("0P"))
        self.assertFalse(is_palindrome("palindrome"))

    def test_numbers_and_special_characters(self) -> None:
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("!@#$$#@!"))
        self.assertTrue(is_palindrome("Madam, I'm Adam"))
        self.assertFalse(is_palindrome("12345"))

    def test_single_character(self) -> None:
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))
        self.assertTrue(is_palindrome("7"))
        self.assertTrue(is_palindrome("!"))

    def test_case_insensitivity(self) -> None:
        self.assertTrue(is_palindrome("RaCecAr"))
        self.assertTrue(is_palindrome("Civic"))


if __name__ == '__main__':
    unittest.main(verbosity=2)