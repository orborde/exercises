DEBUG=True

heirloom = 'heirloom'
color = 'color'
drink = 'drink'
person = 'person'
place = 'place'
position = 'position'
absinthe = 'absinthe'
baleton = 'baleton'
beer = 'beer'
blue = 'blue'
contee = 'contee'
dabokva = 'dabokva'
diamond = 'diamond'
dunwall = 'dunwall'
finch = 'finch'
fraeport = 'fraeport'
green = 'green'
karnaca = 'karnaca'
marcolla = 'marcolla'
medal = 'medal'
natsiou = 'natsiou'
pendant = 'pendant'
purple = 'purple'
red = 'red'
ring = 'ring'
rum = 'rum'
snufftin = 'snufftin'
whiskey = 'whiskey'
white = 'white'
wine = 'wine'
winslow = 'winslow'

FAMILIES = {
    position: {0,1,2,3,4},  # leftmost=0
    color: {red,purple,green,white,blue},
    drink : {whiskey,beer,wine,absinthe,rum},
    person: {contee,winslow,marcolla,natsiou,finch},
    heirloom:{ring,pendant,diamond,snufftin,medal},
    place:{karnaca,dunwall,fraeport,baleton,dabokva},
}

ALL_ATOMS = set()
for fam, atoms in FAMILIES.items():
    for atom in atoms:
        assert atom not in ALL_ATOMS
        ALL_ATOMS.add(atom)

import itertools

RELATIONS = []
for fa,fb in itertools.combinations(FAMILIES.values(),r=2):
    for ta, tb in itertools.product(fa,fb):
        RELATIONS.append( (ta,tb) )
RELATIONS = [tuple(sorted(r)) for r in RELATIONS]
RELATIONS.sort()
assert len(set(RELATIONS)) == len(RELATIONS)
print len(RELATIONS), 'possible relations'

assert (0,1) not in RELATIONS

def valid(*args):
    for x in args:
        assert x in ALL_ATOMS

def key(x,y):
    valid(x,y)
    return tuple(sorted([x,y]))

def is_related(world,x,y):
    return key(x,y) in world

FAMILY_INDEX = {}
for fam, atoms in FAMILIES.items():
    for atom in atoms:
        FAMILY_INDEX[atom] = fam

def family_of(atom):
    valid(atom)
    return FAMILY_INDEX[atom]
    
class binary_constraint:
    def __init__(self, x, y):
        valid(x,y)
        self.x = x
        self.y = y

def foodle(world,x,y):
    for other_y in FAMILIES[family_of(y)]:
        if other_y == y:
            continue
        
        if is_related(world, x, other_y):
            return False
    return True

class equiv(binary_constraint):
    def could_be(self, world):
        return (foodle(world, self.x, self.y) and
                foodle(world, self.y, self.x))

    def satisfied(self, world):
        return is_related(world, self.x, self.y)

    def __str__(self):
        return 'equiv({}, {})'.format(self.x, self.y)

def relation_count(world, x, family):
    assert family_of(x) != family

    ct = 0
    for y in FAMILIES[family]:
        if is_related(world, x, y):
            ct += 1
    return ct

def unique_relation(world, x, family):
    assert family_of(x) != family

    if relation_count(world, x, family) != 1:
        return None

    for other in FAMILIES[family]:
        if is_related(world,x,other):
            return other

    return None

def find_position(world, x):
    if family_of(x) == position:
        return x

    return unique_relation(world, x, position)

class is_next_to(binary_constraint):
    def could_be(self, world):
        return True  # fuck it
    def satisfied(self, world):
        xp = find_position(world, self.x)
        yp = find_position(world, self.y)

        if xp is None or yp is None:
            return False

        return abs(yp-xp) == 1
    def __str__(self):
        return 'is_next_to({}, {})'.format(self.x, self.y)

class is_left_of(binary_constraint):
    def could_be(self, world):
        xp = find_position(world, self.x)
        yp = find_position(world, self.y)

        # Left-hand side is all the way to the right.
        if xp == 4:
            return False

        # Right-hand side is all the way to the left.
        if yp == 0:
            return False

        if xp is None or yp is None:
            return True

        return self.satisfied(world)

    def satisfied(self, world):
        xp = find_position(world, self.x)
        yp = find_position(world, self.y)

        if xp is None or yp is None:
            return False

        return xp < yp

    def __str__(self):
        return 'is_left_of({}, {})'.format(self.x, self.y)

class uniquely_paired:
    def __init__(self, x):
        self.x = x
        self.xfam = family_of(self.x)

    def could_be(self, world):
        for family in FAMILIES:
            if family == self.xfam:
                continue

            if relation_count(world, self.x, family) > 1:
                return False

        return True

    def satisfied(self, world):
        for family in FAMILIES:
            if family == self.xfam:
                continue

            if relation_count(world, x, family) != 1:
                return False

        return True

    def __str__(self):
        return 'uniquely_paired({} <{}>)'.format(self.x, self.xfam)

BASE_CONSTRAINTS = [
    equiv(marcolla, red),
    equiv(winslow, 0),
    is_next_to(winslow, green),
    is_left_of(purple, blue),
    equiv(purple, whiskey),
    equiv(karnaca, white),
    is_next_to(ring, karnaca),
    equiv(contee, medal),
    equiv(dunwall, diamond),
    is_next_to(fraeport, snufftin),
    is_next_to(fraeport, rum),
    equiv(finch, beer),
    equiv(baleton, wine),
    equiv(2, absinthe),
    equiv(natsiou, dabokva),
]

print len(BASE_CONSTRAINTS), 'base constraints'

GENERATED_CONSTRAINTS = []
for atom in ALL_ATOMS:
    GENERATED_CONSTRAINTS.append(uniquely_paired(atom))
print len(GENERATED_CONSTRAINTS), 'generated constraints'

CONSTRAINTS = BASE_CONSTRAINTS + GENERATED_CONSTRAINTS

def could_be(world):
    for constraint in CONSTRAINTS:
        if not constraint.could_be(world):
            if DEBUG:
                print "couldn't be:", constraint
            return False
    return True

def satisfied(world,debug=DEBUG):
    for constraint in CONSTRAINTS:
        if not constraint.satisfied(world):
            if debug:
                print "doesn't satisfy:", constraint
            return False
    return True

import copy
def solve(world=set(),start=0,depth=0):
    if DEBUG:
        print 'depth', depth,'start',start, sorted(world)

    if not could_be(world):
        if DEBUG:
            print "couldn't be"
        return

    if satisfied(world):
        if DEBUG:
            print 'SOLVE!'
        yield copy.deepcopy(world)

    for idx in xrange(start, len(RELATIONS)):
        prospect = RELATIONS[idx]
        assert prospect not in world

        if DEBUG:
            print 'depth',depth,'trying',prospect

        world.add(prospect)

        for solution in solve(world,start=idx+1,depth=depth+1):
            yield solution

        world.remove(prospect)

for idx, solution in enumerate(solve()):
    num = idx+1
    print num, solution
