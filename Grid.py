import time
from random import randint

from Block import Block

class Grid(object):
    
    def __init__(self, screen_size):
        
        self.grid_size = screen_size[0] / 12.
        self.dim = (12, int(screen_size[1] / self.grid_size))
        self.blocks = []
        
        print(self.dim)
    
    
    def create_newblock(self):
        # self.blocks.append(Block([randint(1,self.dim[0]), 4],
        #                          self.grid_size, 
        #                          (150, 0, 150), 
        #                          "O"))
        
        self.blocks.append(Block([5, 4],
                                 self.grid_size, 
                                 (150, 0, 150), 
                                 "O"))
        self.blocks.append(Block([5, 9],
                                 self.grid_size, 
                                 (150, 0, 150), 
                                 "T"))
        
    def run(self):
        for block in self.blocks:
            block.show()
            block.update(0.05)
            block.check_boundries(self.dim[1]-1)
            block.handle_collisions(self.blocks, 1)
            time.sleep(0.2)
            
        if self.blocks[-1].active ==  False:
            print("COOL")
        
    