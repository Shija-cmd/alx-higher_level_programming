#!/usr/bin/python3
"""My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
