# testing/string_operations.py

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def to_uppercase(s):
    return s.upper()

def count_char(s, char):
    return s.count(char)