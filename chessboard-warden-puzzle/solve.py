from memoize import memoized

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

def bin2num(bv):
    """Converts little-endian binary to a number. Inverts bits().

    >>> bin2num([])
    0
    >>> bin2num([0])
    0
    >>> bin2num([1])
    1
    >>> bin2num([1,0])
    1
    >>> bin2num([0,1])
    2
    >>> bin2num([1,1])
    3
    >>> bin2num([0,0,1])
    4
    """
    sm = 0
    for b in reversed(bv):
        sm *= 2
        sm += b
    return sm

def flip(v, pos):
    """Flips a bit in a bit vector.

    >>> flip([0, 0, 1], 2)
    [0, 0, 0]
    >>> flip([0, 0, 1], 1)
    [0, 1, 1]
    """
    left = v[:pos]
    right = v[(pos+1):]
    return left + [(1 - v[pos])] + right

def bin2str(v):
    return ''.join(str(b) for b in v)

@memoized
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

def compute_parity(matrix, data):
    parity = []
    for row in matrix:
        p = 0
        assert len(row) == len(data)
        for m,d in zip(row, data):
            p = (p + m*d)%2
        parity.append(p)
    return parity


def send(board, position):
    cur_parity = compute_parity(hamming_matrix(63), board[:63])
    cur_parity = bin2num(cur_parity)
    #print 'parity  =', '{:06b}'.format(cur_parity), cur_parity
    #print 'pos     =', '{:06b}'.format(position), position
    flipnum = cur_parity ^ position
    #print 'flipnum =', '{:06b}'.format(flipnum), flipnum
    if flipnum == 0:
        #print 'No flip!'
        return board
    return flip(board, flipnum - 1)

def receive(board):
    parity = compute_parity(hamming_matrix(63), board[:63])
    return bin2num(parity)

if __name__ == '__main__':
    import doctest
    fails, _ = doctest.testmod()
    assert fails == 0

    for row in hamming_matrix(7):
        print row


    import random
    random.seed(1338)
    board = [random.choice([0, 1]) for _ in xrange(64)]
    pos = random.randint(0,63)
    print 'PROBLEM:'
    print 'pos =', pos
    print 'board   =', bin2str(board)

    permute = send(board, pos)
    #print 'board   =', bin2str(board)
    print 'permute =', bin2str(permute)
    recv = receive(permute)
    print 'recv =', recv
    assert recv == pos
