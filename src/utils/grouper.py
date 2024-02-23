from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    """
    A function for dividing a list into groups of n elements
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
