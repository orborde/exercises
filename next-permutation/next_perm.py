import itertools
import unittest

def swap_indexes(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def reverse_subarray(arr, start, end):
    assert start <= end
    # start, end are inclusive
    for left in xrange(start, end+1):
        offset = left - start
        right = end - offset
        if right < left:
            break
        swap_indexes(arr, left, right)

class SubarrayOpsTest(unittest.TestCase):
    def test_full(self):
        arr = [1,2,3]
        reverse_subarray(arr, 0, 2)
        self.assertEquals(arr, [3, 2, 1])

    def test_partial(self):
        arr = [1,2,3,4,5]
        reverse_subarray(arr, 2, 4)
        self.assertEquals(arr, [1,2,5,4,3])

    def test_single(self):
        arr = [1,2,3]
        reverse_subarray(arr, 1, 1)
        self.assertEquals(arr, [1,2,3])

def implies(x, yf):
    if x:
        if not yf():
            return False
    return True

def find_insertion_point(arr, val, start, end):
    assert implies(start > 0, lambda: arr[start-1] < arr[start])
    for idx in xrange(start+1, end+1):
        if arr[idx] <= val:
            return idx-1
    return end

class InsertionPointTest(unittest.TestCase):
    def test_simples(self):
        self.assertEquals(
            find_insertion_point([2,3,1], 2, 1, 2), 1)
        self.assertEquals(
            find_insertion_point([1,3,2], 1, 1, 2), 2)
        self.assertEquals(
            find_insertion_point([1,4,3,2], 1, 1, 3), 3)


def permute(arr):
    # The right-hand subarray is in descending order. Figure out how
    # far left that subarray goes.
    subarray_end = len(arr) - 1
    subarray_start = subarray_end
    while (subarray_start > 0 and
           arr[subarray_start-1] > arr[subarray_start]):
        subarray_start -= 1

    if subarray_start != 0:
        ins_val = arr[subarray_start - 1]
        ins_point = find_insertion_point(
            arr, ins_val, subarray_start, subarray_end)
        swap_indexes(arr, ins_point, subarray_start - 1)

    reverse_subarray(arr, subarray_start, len(arr) - 1)
        
def test_cycle(arr):
    permutations = list(itertools.permutations(arr))
    permutations.sort()
    for idx in xrange(len(permutations)):
        cur = list(permutations[idx])
        succ_idx = (idx+1)%len(permutations)
        succ = list(permutations[succ_idx])
        permute(cur)
        if cur != succ:
            raise Exception(
                'FAIL: permute({}) = {} (expected {})'.format(
                    list(permutations[idx]),
                    cur,
                    succ))


def test():
    for arr_len in xrange(1, 6):
        print 'TESTING LENGTH', arr_len
        arr = range(1, arr_len + 1)
        assert len(arr) == arr_len
        test_cycle(arr)
    for arr_len in xrange(1, 6):
        print 'TESTING W/DUPES LENGTH', arr_len
        elements = range(1, arr_len + 1)
        assert len(elements) == arr_len
        for arr in itertools.product(elements, repeat=arr_len):
            print arr
            test_cycle(arr)

if __name__ == '__main__':
    test()
