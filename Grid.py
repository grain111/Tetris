from Block import Block

class Grid(object):
    
    def __init__(self, dim, screen_size):
        
        self.dim = dim #Tuple
        self.grid_size = screen_size[0] / (dim[0] * 1.)
        self.blocks = []
    
    
    def create_newblock(self):
        self.blocks.append(Block([5,5], self.grid_size, (150, 0, 150), "I"))
        self.blocks.append(Block([8,7], self.grid_size, (150, 0, 150), "T"))
        
    def show(self):
        for block in self.blocks:
            block.show()
            block.update(0.2)
        
    