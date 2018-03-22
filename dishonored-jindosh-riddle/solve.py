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
RELATIONS = list(itertools.combinations(ALL_ATOMS, r=2))
RELATIONS = [tuple(sorted(r)) for r in RELATIONS]
RELATIONS.sort()
print len(RELATIONS), 'possible relations'

RELATION_INDEXES = {relation:idx for idx,relation in enumerate(RELATIONS)}

def valid(*args):
    for x in args:
        assert x in ALL_ATOMS

def key(x,y):
    valid(x,y)
    return tuple(sorted([x,y]))

def is_related(world,x,y):
    return world[RELATION_INDEXES[key(x,y)]]

def set_related(world,x,y,to):
    world[RELATION_INDEXES[key(x,y)]] = to

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
        self._x = x
        self._y = y

def foodle(world,x,y):
    for other_y in FAMILIES[family_of(y)]:
        if other_y == y:
            continue
        
        if is_related(world, x, other_y):
            return False
    return True

class equiv(binary_constraint):
    def could_be(self, world):
        return (foodle(world, self._x, self._y) and
                foodle(world, self._y, self._x))

    def satisfied(self, world):
        return is_related(world, self._x, self._y)

def find_position(world, x):
    if family_of(x) == position:
        return x

class is_next_to(binary_constraint):
    def could_be(self, world):
        return True  # fuck it
    def satisfied(self, world):
        pass

class is_left_of(binary_constraint):
    def could_be(self, world):
        pass
    def satisfied(self, world):
        pass

CONSTRAINTS = [
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

