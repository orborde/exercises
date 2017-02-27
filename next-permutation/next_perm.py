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

def find_insertion_point(arr, val, start):
    assert start > 0
    end = len(arr)-1
    for idx in xrange(start+1, end+1):
        if arr[idx] <= val:
            return idx-1
    return end

class InsertionPointTest(unittest.TestCase):
    def test_simples(self):
        self.assertEquals(
            find_insertion_point([2,3,1], 2, 1), 1)
        self.assertEquals(
            find_insertion_point([1,3,2], 1, 1), 2)
        self.assertEquals(
            find_insertion_point([1,4,3,2], 1, 1), 3)


def permute(arr):
    # The right-hand subarray is in descending order. Figure out how
    # far left that subarray goes.
    subarray_start = len(arr) - 1
    while (subarray_start > 0 and
           arr[subarray_start-1] >= arr[subarray_start]):
        subarray_start -= 1

    if subarray_start != 0:
        ins_val = arr[subarray_start - 1]
        ins_point = find_insertion_point(
            arr, ins_val, subarray_start)
        swap_indexes(arr, ins_point, subarray_start - 1)

    reverse_subarray(arr, subarray_start, len(arr) - 1)
        
def test_cycle(arr):
    permutations = list(set(itertools.permutations(arr)))
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

# https://stackoverflow.com/questions/3755136/pythonic-way-to-check-if-a-list-is-sorted-or-not
def is_sorted(l):
    return all(a <= b for a, b in itertools.izip(l[:-1], l[1:]))

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
            # TODO: Not the best way to do this; ideally, we wouldn't
            # bother generating the redundant ones at all.
            if not is_sorted(arr):
                continue
            test_cycle(arr)

if __name__ == '__main__':
    test()
