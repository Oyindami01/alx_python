#!/usr/bin/env python3
def raise_exception():
    try:
        raise "TypeException"
    except Exception as e:
        print("Exception has been raised")
        