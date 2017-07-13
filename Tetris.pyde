from Block import Block
from Grid import Grid

blocks = []

blocks.append(Block([400/2, 450], (150, 0, 150), "Z"))

def setup():
    size(400, 700)
    grid = Grid((12,30), (width, height))
    grid.create_newblock()
    
def draw():
    background(51)
    for bl in blocks:
        bl.show()
        bl.update(1, blocks)
        if not blocks[-1].active:
            blocks.append(Block([400/2, 450], (150, 0, 150), "I"))
    