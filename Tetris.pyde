from Block import Block

bl = Block([400/2, 700/2], (50, 0, 50), "Z")

def setup():
    size(400, 700)
    
def draw():
    background(51)
    bl.show()
    