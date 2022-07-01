#!/usr/bin/python3

if __name__ == "__main__":
    """Guarded my script"""

    from add_0 import add

    b = 1
    d = 2

    print("{:d} + {:d} = {:d}".format(b, d, add(b, d)))
