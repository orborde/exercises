def bitsize(n):
    """
    >>> bitsize(3)
    2
    >>> bitsize(1)
    1
    >>> bitsize(0)
    0
    """
    rs = 0
    while n > 0:
        rs += 1
        n = n / 2
    return rs

def bits(n):
    """Converts to little-endian binary.

    >>> bits(3)
    [1, 1]
    >>> bits(2)
    [0, 1]
    """
    rs = []
    while n > 0:
        rs.append(n%2)
        n = n / 2
    return rs
        
def hamming_matrix(codeword_length):
    parity_covers = []
    for col in xrange(codeword_length):
        bitnum = col + 1
        colbits = bits(bitnum)
        if len(parity_covers) < len(colbits):
            parity_covers.append([0] * col)
        assert len(colbits) == len(parity_covers)
        for i in xrange(len(colbits)):
            parity_covers[i].append(colbits[i])
    return parity_covers

if __name__ == '__main__':
    import doctest
    fails, _ = doctest.testmod()
    assert fails == 0

    for row in hamming_matrix(7):
        print row

