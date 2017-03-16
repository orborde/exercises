def min2deg(minutes):
    """Converts minutes hand position to degrees.

    >>> min2deg(30)
    180
    >>> min2deg(15)
    90
    """
    assert 0 <= minutes < 60
    return (minutes * 360) / 60

def hour2deg(hours):
    """Converts hours hand position to degrees.

    >>> hour2deg(6)
    180
    >>> hour2deg(3)
    90
    """
    assert 0<= hours < 12
    return (hours * 360) / 12

def anglediff(a, b):
    """Returns the absolute value of the difference between two angles.
    """

    """
    >>> anglediff(0, 90)
    90
    >>> anglediff(315, 90)
    135
    """
    # Compute additive inverse of b
    ib = 360 - b
    # Compute the difference.
    diff = (a + ib) % 360
    if diff > 180:
        diff = 360 - diff
    return diff


import doctest
def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite())
    return tests

import itertools
import unittest
class Angle(unittest.TestCase):
    def test_exhaustive(self):
        for a,b in itertools.product(range(360), repeat=2):
            diff = anglediff(a, b)
            self.assertLessEqual(diff, 180)
            loff = (a - diff) % 360
            roff = (a + diff) % 360
            self.assertIn(b, [loff, roff])

def clock_hands_diff(hour, minute):
    """Compute the angle between the two hands on the face of an analog clock.

    >>> clock_hands_diff(3, 15)
    0
    >>> clock_hands_diff(4, 15)
    30
    >>> clock_hands_diff(5, 15)
    60
    >>> clock_hands_diff(0, 1)
    6
    >>> clock_hands_diff(7, 45)
    60
    """
    ang_h = hour2deg(hour)
    ang_m = min2deg(minute)
    return anglediff(ang_h, ang_m)
