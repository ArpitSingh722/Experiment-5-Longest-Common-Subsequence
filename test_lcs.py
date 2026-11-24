import unittest
from lcs import longest_common_subsequence


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_known_example(self):
        lcs, length = longest_common_subsequence(list("ABCBDAB"), list("BDCABA"))
        self.assertEqual(length, 4)
        self.assertEqual(len(lcs), 4)

    def test_no_common_elements(self):
        lcs, length = longest_common_subsequence(list("ABC"), list("XYZ"))
        self.assertEqual(lcs, [])
        self.assertEqual(length, 0)

    def test_identical_sequences(self):
        lcs, length = longest_common_subsequence(list("PYTHON"), list("PYTHON"))
        self.assertEqual(lcs, list("PYTHON"))
        self.assertEqual(length, 6)

    def test_empty_sequences(self):
        lcs, length = longest_common_subsequence([], list("ABC"))
        self.assertEqual(lcs, [])
        self.assertEqual(length, 0)


if __name__ == "__main__":
    unittest.main()
