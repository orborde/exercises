# Perform brute-force assignment of bit vectors to output values.

import unittest

BITS = set([0, 1])
def isbit(bit):
    return bit in BITS

def bnot(bit):
    assert isbit(bit)
    return 1 - bit

def adjacents(vec):
    for i in xrange(len(vec)):
        left, right = vec[:i], vec[i+1:]
        yield left + (bnot(vec[i]),) + right

class Ops(unittest.TestCase):
    def adj_test(self, start, ends):
        adjs = list(adjacents(start))
        adjs.sort()
        self.assertEquals(len(set(adjs)), len(adjs))
        self.assertEquals(set(adjs), set(ends))
    def test_adjacents(self):
        self.adj_test((0, 0), [(0, 1), (1, 0)])
        self.adj_test((0, 1), [(0, 0), (1, 1)])
        self.adj_test((1, 0), [(0, 0), (1, 1)])
        self.adj_test((1, 1), [(0, 1), (1, 0)])


