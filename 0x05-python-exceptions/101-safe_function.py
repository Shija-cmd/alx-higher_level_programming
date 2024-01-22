#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        r = fct(*args)
    except BaseException as er:
        r = None
        print("Exception: {}".format(er), file=sys.stderr)
    finally:
        return r
