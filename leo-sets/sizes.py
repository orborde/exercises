#from tqdm import tqdm

import itertools

stuff = b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

d = {}
size = 7000000
vendor = itertools.product(stuff, repeat=5)
#for _ in tqdm(range(size)):
for x in range(size):
    if x % 100000 == 0:
        print x
    tpl = vendor.next()
    key = b''.join(tpl)
    d[key] = set()

print 'MEASURE SIZE NOW'
raw_input()
