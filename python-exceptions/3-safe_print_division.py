#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        if b == 0:
            return None
        else:
            print("Inside result: {}".format(div))
            return div
