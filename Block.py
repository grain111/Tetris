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
                    
    def check_boundries(self):
        for i, row in enumerate(self.shp):
            for j, item in enumerate(row):
                if self.pos[1] + (i + 1) * 20 > height:
                    self.pos[1] = height - (i + 1) * 20
                    self.active = False
                    
    def handle_collisions(self, blocks):
        pass
                
                           
    def update(self, dt):
        for i, row in enumerate(self.shp):
            for j, item in enumerate(row):
                if not self.shp[i][j] == 0:
                    self.shp[i][j][1] += 1
                    time.sleep(dt)
            
    def calc_pos(self):
        for i, row in enumerate(self.shp):
            for j, item in enumerate(row):
                if not self.shp[i][j] == 0:
                    self.shp[i][j] = [self.pos[0] + j, self.pos[1] + i]
        
        