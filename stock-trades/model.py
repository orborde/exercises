import collections
import itertools
from fractions import Fraction

steps = 5
start_price = 10
stocks = 20

def gen_price_history():
    for moves in itertools.product([-1, 1], repeat=steps):
        amount = start_price
        prices = []
        for mov in moves:
            amount += mov
            prices.append(amount)
        assert len(prices) == steps
        yield prices


def sell_at_once():
    histo = collections.defaultdict(int)
    for prices in gen_price_history():
        for pt in range(steps):
            sale = prices[pt] * stocks
            histo[sale] += 1
    return histo

def sell_sharded():
    schedule = []
    for _ in range(steps - 1):
        schedule.append(int(stocks / steps))
    schedule.append(stocks - sum(schedule))

    histo = collections.defaultdict(int)
    for prices in gen_price_history():
        sale = 0
        for amt,price in zip(schedule,prices):
            sale += amt*price
        #print schedule, prices, sale
        histo[sale] += 1
    return histo

def mean(histo):
    sm,ct = 0,0
    for val,wt in histo.items():
        sm += wt*val
        ct += wt
    return Fraction(sm) / Fraction(ct)

def variance(histo):
    u = mean(histo)

    sm,ct = 0,0
    for val,wt in histo.items():
        sm += wt * ( (val-u) ** 2 )
        ct += wt

    return Fraction(sm) / Fraction(ct)


for f in [sell_at_once, sell_sharded]:
    print f.__name__,
    histo = f()
    print int(mean(histo)), int(variance(histo)),
    for k in sorted(histo.keys()):
        print '{}:{}'.format(k, histo[k]),
    print
