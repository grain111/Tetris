class Block(object):
    
    shapes = {"I":[[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]],
              "T":[[1,1,1,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]],
              "O":[[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]],
              "L":[[1,0,0,0],[1,0,0,0],[1,1,0,0],[0,0,0,0]],
              "J":[[0,1,0,0],[0,1,0,0],[1,1,0,0],[0,0,0,0]],
              "S":[[0,1,1,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]],
              "Z":[[1,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],
                   }
    
    def __init__(self, pos, clr, shp):
        
        self.clr = clr
        self.pos = pos
        self.shp = self.shapes[shp]
        self.active = True
        
    def show(self):
        
        for i, row in enumerate(self.shp):
            for j, item in enumerate(row):
                if item == 1:
                    rect(self.pos[0] + j * 20, self.pos[1] + i * 20, 20, 20)
                    
    def check_boundries(self):
        for i, row in enumerate(self.shp):
            for j, item in enumerate(row):
                if self.pos[1] + (i - 1) * 20 > height:
                    self.pos[1] = height - (i - 1) * 20
                    self.active = False
                           
    def update(self, dt):
        if self.active:
            self.pos[1] += dt
            self.check_boundries()
        