"""
Topic: Variables in Python
==========================
A variable is a NAME that points to an object in memory.
Python is dynamically typed — no type declaration needed.

Run:
  python 01_basics/02_variables.py
"""


def create_variables():
    """Create a variable — just assign a value."""
    print("--- Creating variables ---")

    x = 10                # creates x pointing to int 10
    name = "Ganesh"
    pi = 3.14

    print(x, name, pi)
    print("id of x:", id(x))       # memory address
    print("type of x:", type(x))   # <class 'int'>


def dynamic_typing_demo():
    """Variable can point to any type."""
    print("\n--- Dynamic typing ---")

    v = 5
    print(v, type(v))

    v = "hello"           # perfectly legal
    print(v, type(v))

    v = [1, 2, 3]
    print(v, type(v))


def multiple_assignment():
    """Assign many variables at once."""
    print("\n--- Multiple assignment ---")

    a, b, c = 1, 2, 3
    print(a, b, c)

    # Same value to many
    x = y = z = 100
    print(x, y, z, id(x) == id(y) == id(z))   # True


def swap_variables():
    """Pythonic swap — no temp variable needed."""
    print("\n--- Swap ---")

    a, b = 10, 20
    a, b = b, a
    print("after swap:", a, b)   # 20 10


def unpacking_demo():
    """Unpack collections into variables."""
    print("\n--- Unpacking ---")

    first, second, third = [1, 2, 3]
    print(first, second, third)

    # Catch middle with *
    head, *middle, tail = [1, 2, 3, 4, 5]
    print("head:", head, "middle:", middle, "tail:", tail)

    # Ignore values with _
    name, _, age = ("Ganesh", "unused", 24)
    print(name, age)


def naming_rules():
    """Valid and invalid variable names."""
    print("\n--- Naming rules ---")

    # ✅ Valid
    user_name = "Ganesh"       # snake_case (recommended)
    _private = 10              # leading _ means "internal"
    userName123 = "works"      # camelCase works but not Pythonic
    MAX_RETRIES = 3            # UPPER = constant by convention
    class_ = "Alpha"           # trailing _ to avoid keyword clash

    print(user_name, _private, userName123, MAX_RETRIES, class_)

    # ❌ Invalid — would raise SyntaxError:
    #   2name = "no"        # cannot start with digit
    #   my-name = "no"      # '-' not allowed
    #   class = "no"        # keyword


def scope_demo():
    """LEGB — Local, Enclosing, Global, Built-in."""
    print("\n--- Scope (LEGB) ---")

    g = "global"              # Global from this function's view

    def outer():
        e = "enclosing"
        def inner():
            l = "local"
            print(l, e, g)    # local enclosing global
        inner()
    outer()


def assignment_is_not_copy():
    """IMPORTANT: a = b does NOT copy a list!"""
    print("\n--- a = b is NOT a copy ---")

    a = [1, 2, 3]
    b = a                 # b is a SECOND NAME for the same list
    b.append(4)
    print("a:", a)        # [1, 2, 3, 4]   -> a changed too!
    print("same object?", a is b)   # True

    # To actually copy:
    c = a.copy()          # or a[:], list(a)
    c.append(99)
    print("a:", a, "c:", c)


def constants_convention():
    """Python has no real constants — just the UPPER_CASE convention."""
    print("\n--- Constants (convention) ---")

    PI = 3.14159
    MAX_RETRIES = 3
    DATABASE_URL = "postgresql://localhost/mydb"

    print(PI, MAX_RETRIES, DATABASE_URL)


def main():
    create_variables()
    dynamic_typing_demo()
    multiple_assignment()
    swap_variables()
    unpacking_demo()
    naming_rules()
    scope_demo()
    assignment_is_not_copy()
    constants_convention()


if __name__ == "__main__":
    main()
