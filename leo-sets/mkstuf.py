from tqdm import tqdm

import itertools

stuff = b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

size = 7000000
vendor = itertools.product(stuff, repeat=5)
for _ in tqdm(range(size)):
    tpl = vendor.next()
    key = b''.join(tpl)
    print key
