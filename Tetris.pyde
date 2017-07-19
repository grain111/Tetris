from Grid import Grid

def setup():
    size(400, 700)
    global grid
    grid = Grid((width, height))
    grid.create_newblock()
    
def draw():
    background(51)
    grid.run()
    