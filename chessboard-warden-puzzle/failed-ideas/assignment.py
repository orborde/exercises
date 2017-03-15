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

def assignment_ok(assignment, total_decodings):
    """Checks whether a (possibly partial) assignment might work.

    In particular, for each possible bit vector, make sure that it
    does (or could) reach all of the other decodings."""
    for codeword, decode in assignment.iteritems():
        neighbor_decodes = set()
        empty_neighbor_ct = 0
        for neighbor in adjacents(codeword):
            if neighbor in assignment:
                if assignment[neighbor] != decode:
                    neighbor_decodes.add(assignment[neighbor])
            else:
                empty_neighbor_ct += 1
        if len(neighbor_decodes) + empty_neighbor_ct < total_decodes:
            return False
    return True

class Assignment(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(assignment_ok({}, 4))
        self.assertTrue(assignment_ok({(0,1,0,1): 0}, 4))
