from Grid import Grid

def setup():
    size(400, 700)
    global grid
    grid = Grid((12,30), (width, height))
    grid.create_newblock()
    
def draw():
    background(51)
    grid.show()
    