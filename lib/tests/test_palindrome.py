"""
Tests for the longest_palindromic_substring function.

Ex:
- Input: ""             → Output: ""
- Input: "a"            → Output: "a"
- Input: "babad"        → Output: "bab" or "aba"
- Input: "cbbd"         → Output: "bb"
- Input: "racecar"      → Output: "racecar"
- Input: "abcdef"       → Output: any single character (e.g., "a")
"""

import pytest
from lib.palindrome import longest_palindromic_substring


def test_basic_palindromes():
    """Test basic palindrome cases with multiple assertions."""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("aba") == "aba"
    assert longest_palindromic_substring("abba") == "abba"
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("noon") == "noon"


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("aa") == "aa"
    assert longest_palindromic_substring("aaaa") == "aaaa"
    # For strings with no palindromes longer than 1, any single char is valid
    result = longest_palindromic_substring("abcdef")
    assert result in ["a", "b", "c", "d", "e", "f"]
    assert len(result) == 1
