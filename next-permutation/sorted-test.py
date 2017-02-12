# Figure out exactly how much redundant work we're removing by
# skipping unsorted possible product() outputs.

# https://stackoverflow.com/questions/3755136/pythonic-way-to-check-if-a-list-is-sorted-or-not
def is_sorted(l):
    return all(a <= b for a, b in itertools.izip(l[:-1], l[1:]))

import itertools

for arrlen in xrange(1, 8+1):
    values = range(1, arrlen+1)
    assert len(values) == arrlen
    total_count = 0
    sorted_count = 0
    for arr in itertools.product(values, repeat=arrlen):
        total_count += 1

        if is_sorted(arr):
            sorted_count += 1

    print arrlen, sorted_count, total_count,
    print '{}%'.format(sorted_count*100 / total_count)

