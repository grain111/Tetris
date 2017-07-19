import time

class Block(object):
    
    shapes = {"I":[[1],[1],[1],[1]],
              "T":[[1,1,1],[0,1,0]],
              "O":[[1,1],[1,1]],
              "L":[[1,0],[1,0],[1,1]],
              "J":[[0,1],[0,1],[1,1]],
              "S":[[0,1,1],[1,1,0]],
              "Z":[[1,1,0],[0,1,1]],
                   }
    
    def __init__(self, pos, a, clr, shp):
        
        self.clr = clr
        self.pos = pos
        self.shp = self.shapes[shp]
        self.active = True
        self.a = a
        
        self.calc_pos()
        
    def show(self):
        
        for i, row in enumerate(self.shp):
            for j, pos in enumerate(row):
                if not pos == 0:
                    fill(self.clr[0], self.clr[1], self.clr[2])
                    rect(pos[0] * self.a, pos[1] * self.a, self.a, self.a)
                    
    def items(self):
        for i, row in enumerate(self.shp):
            for j, item in enumerate(row):
                yield i, j, item
        
                    
    def check_boundries(self, lim):
        for i, j, item in self.items():
            if not item == 0:
                if item[1] == lim:
                    self.active = False
                    
    # def handle_collisions(self, blocks, dir):
    #     for i, row in enumerate(self.shp):
    #         for j, item in enumerate(row):
    #             if not item == 0:
    #                 for block in blocks:
    #                     if not block == self:
    #                         for rw in block.shp:
    #                             if dir == 1 and [item[0], item[1]+1] in rw:
    #                                 self.active = False
    
    def handle_collisions(self, blocks, dir):
        for i, j, item in self.items():
            for block in blocks:
                if not block == self and not item == 0:
                    for rw in block.shp:
                        if dir == 1 and [item[0], item[1]+1] in rw:
                            self.active = False            
                            
    def update(self, dt):
        if self.active:
            self.pos[1] += 1
            self.calc_pos()
            
    def calc_pos(self):
        for i, j, item in self.items():
            if not self.shp[i][j] == 0:
                self.shp[i][j] = [self.pos[0] + j, self.pos[1] + i]
        
        