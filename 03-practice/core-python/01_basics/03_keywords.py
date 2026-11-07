"""
Topic: Keywords in Python
=========================
Keywords are reserved words. You cannot use them as variable, function,
or class names. There are 35 keywords in Python (plus 3 soft keywords).

Run:
  python 01_basics/03_keywords.py
"""

# Program to demonstrate the use of keywords in Python
import keyword

print("========================== Python Keywords: ==========================")
print(keyword.kwlist)
print()
print("Total number of keywords:", len(keyword.kwlist))
