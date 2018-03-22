FAMILIES = {
    'position': {0,1,2,3,4},  # leftmost=0
    'color': {'red','purple','green','white','blue'},
    'drink' : {'whiskey','beer','wine','absinthe','rum'},
    'person': {'contee','winslow','marcolla','natsiou','finch'},
    'heirloom':{'ring','pendant','diamond','snufftin','medal'},
    'place':{'karnaca','dunwall','fraeport','baleton','dabokva'},
}

ALL_ATOMS = set()
for fam in FAMILIES.values():
    for atom in fam:
        assert atom not in ALL_ATOMS
        ALL_ATOMS.add(atom)

def valid(x,y):
    assert x in ALL_ATOMS
    assert y in ALL_ATOMS

def equiv(x,y):
    valid(x,y)
    def could_be_true(world):
        pass
    return could_be_true

def is_next_to(x,y):
    valid(x,y)
    def could_be_true(world):
        pass
    return could_be_true

def is_left_of(x,y):
    valid(x,y)
    def could_be_true(world):
        pass
    return could_be_true

BASE_THEOREMS = [
    equiv('marcolla', 'red'),
    equiv('winslow', 0),    
    is_next_to('winslow', 'green'),
    is_left_of('purple', 'blue'),
    equiv('purple', 'whiskey'),
    equiv('karnaca', 'white'),
    is_next_to('ring', 'karnaca'),
    equiv('contee', 'medal'),
    equiv('dunwall', 'diamond'),
    is_next_to('fraeport', 'snufftin'),
    is_next_to('fraeport', 'rum'),
    equiv('finch', 'beer'),
    equiv('baleton', 'wine'),
    equiv(2, 'absinthe'),
    equiv('natsiou', 'dabokva'),
]
