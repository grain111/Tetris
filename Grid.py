from Block import Block

class Grid(object):
    
    def __init__(self, dim, screen_size):
        
        self.dim = dim #Tuple
        self.grid_size = screen_size[0] / (dim[0] * 1.)
        print(self.grid_size)
    
    
    def create_newblock(self):
        self.active = Block([dim[0]
        
    