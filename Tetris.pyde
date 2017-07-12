from Block import Block

blocks = []

blocks.append(Block([400/2, 450], (150, 0, 150), "Z"))

def setup():
    size(400, 700)
    
def draw():
    background(51)
    for bl in blocks:
        bl.show()
        bl.update(1, blocks)
        if not blocks[-1].active:
            blocks.append(Block([400/2, 450], (150, 0, 150), "I"))
    