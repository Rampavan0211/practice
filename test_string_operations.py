# testing/test_string_operations.py
import pytest
from string_operations import reverse_string, is_palindrome, to_uppercase, count_char

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("12345") == "54321"

def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("HeLLo") == "HELLO"
    assert to_uppercase("") == ""
    assert to_uppercase("12345") == "12345"
    assert to_uppercase("hello world!") == "HELLO WORLD!"

def test_count_char():
    assert count_char("hello", "l") == 2
    assert count_char("hello", "z") == 0
    assert count_char("", "a") == 0
    assert count_char("aaa", "a") == 3
    assert count_char("hello world", "o") == 2

def test_edge_cases():
    # Edge cases for reverse_string
    assert reverse_string("a" * 1000) == "a" * 1000
    
    # Edge cases for is_palindrome
    assert is_palindrome("a" * 1000) == True
    assert is_palindrome("a" * 999 + "b") == False
    
    # Edge cases for to_uppercase
    assert to_uppercase("a" * 1000) == "A" * 1000
    
    # Edge cases for count_char
    assert count_char("a" * 1000, "a") == 1000
    assert count_char("a" * 1000, "b") == 0

def test_non_string_input():
    # Testing non-string inputs
    with pytest.raises(TypeError):
        reverse_string(123)
    with pytest.raises(TypeError):
        is_palindrome(123)
    # with pytest.raises(TypeError):
    #     to_uppercase('ram')
    with pytest.raises(TypeError):
        count_char(123, '1')

def test_special_characters():
    # Testing special characters
    assert reverse_string("!@#$%^&()") == ")(&^%$#@!"
    assert is_palindrome("!@#@@#@!") == True
    assert to_uppercase("!@#") == "!@#"
    assert count_char("!@#$%^&*()", "!") == 1