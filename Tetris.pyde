from Block import Block

blocks = []

blocks.append(Block([400/2, 450], (50, 0, 50), "Z"))
blocks.append(Block([200/2, 450], (50, 0, 50), "T"))

def setup():
    size(400, 700)
    
def draw():
    background(51)
    for bl in blocks:
        bl.show()
        bl.update(1)
        if not bl.active:
            blocks.append(Block([400/2, 450], (50, 0, 50), "I"))
    