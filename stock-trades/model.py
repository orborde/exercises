#! /usr/bin/env python3

import collections
import itertools
from fractions import Fraction
import statistics

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
    for prices in gen_price_history():
        for pt in range(steps):
            sale = prices[pt] * stocks
            yield sale

def sell_sharded():
    base_schedule = []
    for _ in range(steps - 1):
        base_schedule.append(int(stocks / steps))
    base_schedule.append(stocks - sum(base_schedule))

    for schedule in itertools.permutations(base_schedule):
        for prices in gen_price_history():
            sale = 0
            for amt,price in zip(schedule,prices):
                sale += amt*price
            #print(schedule, prices, sale)
            yield sale


for f in [sell_at_once, sell_sharded]:
    print(f.__name__,end=' ')
    outcomes = list(f())
    histo = collections.defaultdict(int)
    for d in outcomes:
        histo[d] += 1

    print(int(statistics.mean(outcomes)), int(statistics.variance(outcomes)),end=' ')
    for k in sorted(histo.keys()):
        print('{}:{}'.format(k, histo[k]),end=' ')
    print()
