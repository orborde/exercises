# Abortive attempt at some kind of "checksum" strategy.

def checksum(bits):
    """
    >>> checksum([1, 0, 1])
    2
    """
    sm = 0
    for bit, val in zip(bits, range(len(bits))):
        sm += val * bit
    return sm % len(bits)

import itertools
def checkstrat():
    pass

if __name__ == '__main__':
    import doctest
    fails, _ = doctest.testmod()
    assert fails == 0

