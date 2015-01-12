import itertools

class Tile(list):
    def __getitem__(self, x):
        return super(Tile, self).__getitem__(x % len(self))

    def rotate(self, x):
        return Tile(self[x:] + self[:x])

COLOURS = ('YELLOW', 'WHITE', 'BLACK', 'RED', 'GREEN', 'BLUE')
YELLOW, WHITE, BLACK, RED, GREEN, BLUE = range(len(COLOURS))

TILES = (
    Tile((WHITE, YELLOW, RED, BLUE, BLACK, GREEN)),
    Tile((RED, BLUE, BLACK, YELLOW, GREEN, WHITE)),
    Tile((WHITE, BLACK, YELLOW, GREEN, BLUE, RED)),
    Tile((WHITE, BLUE, GREEN, YELLOW, BLACK, RED)),
    Tile((GREEN, BLUE, BLACK, YELLOW, RED, WHITE)),
    Tile((RED, YELLOW, GREEN, BLACK, BLUE, WHITE)),
)

CENTER = Tile((WHITE, BLACK, RED, GREEN, BLUE, YELLOW))

def pairwise(it):
    a, b = itertools.tee(it)

    next(b, None)

    return itertools.izip(a, b)

def validate(xs):
    for idx, x in enumerate(xs):
        if x[idx + 3] != CENTER[idx]:
            raise ValueError("Tile does not match center")

    for idx, (a, b) in enumerate(pairwise(xs)):
        if a[idx + 2] != b[idx + 5]:
            raise ValueError("Tile does not match previous anticlockwise tile")

    return xs

def find_solution():
    # For all possible tile permutations..
    for xs in itertools.permutations(TILES):

        # ... try all possible rotations
        for ys in itertools.product(range(len(COLOURS)), repeat=len(COLOURS)):
            try:
                return validate([x.rotate(y) for x, y in zip(xs, ys)])
            except ValueError:
                pass

    raise ValueError("Could not find a solution.")

for x in find_solution():
    print ', '.join(COLOURS[y] for y in x)
