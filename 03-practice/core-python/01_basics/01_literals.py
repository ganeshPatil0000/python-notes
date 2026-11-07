"""
Topic: Literals in Python
=========================
A literal is a fixed value written directly in the code.
Examples: 10, 3.14, "hello", True, None, [1, 2, 3]

Run:
  python 01_basics/01_literals.py
"""


def numeric_literals():
    """int, float, complex — and different bases."""
    print("--- Numeric literals ---")

    # int
    a, b, c = 10, -5, 0

    # float
    pi = 3.14
    big = 1.5e3           # 1.5 x 10^3
    print("float:", pi, big)

    # complex (j = sqrt(-1))
    z = 2 + 3j
    print("complex:", z, type(z))

    # Different bases
    print("binary 0b1010 =", 0b1010)   # 10
    print("octal  0o17   =", 0o17)     # 15
    print("hex    0xff   =", 0xff)     # 255

    # Underscore for readability (Python 3.6+)
    salary = 1_00_000       # Indian style
    print("salary:", salary)


def string_literals():
    """Strings: normal, raw, bytes, f-string."""
    print("\n--- String literals ---")

    s1 = "double quotes"
    s2 = 'single quotes'
    s3 = """triple quotes
    can be multi-line"""

    # Raw string — backslash stays as-is
    path = r"C:\new\test"
    print("raw:", path)             # C:\new\test  (no newline)

    # Bytes literal
    data = b"bytes here"
    print("bytes:", data, type(data))

    # f-string
    name, age = "Ganesh", 24
    print(f"f-string: {name} is {age} years old")
    print(f"math: {2 + 3 = }")      # 2 + 3 = 5   (Python 3.8+)

    # A single character is just a string of length 1
    print("char length:", len('A'))


def boolean_and_none():
    """Boolean and None."""
    print("\n--- Boolean and None ---")

    is_active = True
    is_done = False
    print(is_active, is_done)

    # True is 1, False is 0 internally
    print("True + True =", True + True)        # 2
    print("True + 5    =", True + 5)           # 6

    result = None
    if result is None:                         # always use `is None`
        print("result is None")


def collection_literals():
    """list, tuple, set, dict — and the empty-set trap."""
    print("\n--- Collection literals ---")

    nums  = [1, 2, 3]
    point = (4, 5)
    tags  = {"python", "ai"}
    user  = {"name": "Ganesh", "age": 24}

    print(nums, point, tags, user)
    print(type(nums), type(point), type(tags), type(user))

    # Warning: {} is an empty dict, NOT an empty set!
    print("type of {}:   ", type({}))      # <class 'dict'>
    print("type of set():", type(set()))   # <class 'set'>


def ellipsis_literal():
    """The Ellipsis literal: ..."""
    print("\n--- Ellipsis ---")

    def not_ready_yet():
        ...        # valid function body, same as `pass`
    not_ready_yet()
    print("type of ...:", type(...))   # <class 'ellipsis'>


def main():
    numeric_literals()
    string_literals()
    boolean_and_none()
    collection_literals()
    ellipsis_literal()


if __name__ == "__main__":
    main()
