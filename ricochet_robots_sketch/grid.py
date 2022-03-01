from tile import Tile
T = True
F = False
class Grid:
    def __init__(self,cols,rows):
        self.cols = cols
        self.rows = rows
        self.grid = self.create_grid()
        
    def create_grid(self):
        grid = self.create_outter_walls()
        self.create_inner_walls(grid)
        return grid
    
    def print_grid(self):
        for row in self.grid:
            for tile in row:
                tile.print_tile()
                
    def create_outter_walls(self):
        empty_grid = [[Tile(x,y) for x in range(self.cols)] for y in range(self.rows)]
        for row in empty_grid:
            if row == empty_grid[0]:
                row[0].set_walls(True,True,False,False)
                for tile in range(1, len(row) - 1):
                    row[tile].set_walls(True,False,False,False)
                row[-1].set_walls(True,False,False,True)
            elif row == empty_grid[-1]:
                row[0].set_walls(False,True,True,False)
                for tile in range(1, len(row) - 1):
                    row[tile].set_walls(False,False,True,False)
                row[-1].set_walls(False,False,True,True)
            else:
                row[0].set_walls(False,True,False,False)
                row[-1].set_walls(False,False,False,True)
        return empty_grid
    
    def create_inner_walls(self,grid):
        
        grid[0][4].set_walls(T,F,F,T)
        grid[0][5].set_walls(T,T,F,F)
        
        grid[0][10].set_walls(T,F,F,T)
        grid[0][11].set_walls(T,T,F,F)
        #DR
        grid[1][6].set_walls(F,F,T,T)
        grid[1][7].set_walls(F,T,F,F)
        grid[2][6].set_walls(T,F,F,F)
        #DL
        grid[1][9].set_walls(F,T,T,F)
        grid[1][8].set_walls(F,F,F,T)
        grid[2][9].set_walls(T,F,F,F)
        #UL
        grid[2][1].set_walls(T,T,F,F)
        grid[2][0].set_walls(F,T,F,T)
        grid[1][1].set_walls(F,F,T,F)
        #UR
        grid[2][14].set_walls(T,F,F,T)
        grid[2][15].set_walls(F,T,F,T)
        grid[1][14].set_walls(F,F,T,F)
        
        grid[4][10].set_walls(F,F,T,T)
        grid[4][11].set_walls(F,T,F,F)
        grid[5][10].set_walls(T,F,F,F)
        
        grid[4][15].set_walls(F,F,T,T)
        grid[5][15].set_walls(T,F,F,T)
        
        grid[5][0].set_walls(F,T,T,F)
        grid[6][0].set_walls(T,T,F,F)
        
        grid[5][6].set_walls(T,F,F,T)
        grid[5][7].set_walls(F,T,F,F)
        grid[4][6].set_walls(F,F,T,F)
        
        grid[6][3].set_walls(F,T,T,F)
        grid[6][2].set_walls(F,F,F,T)
        grid[7][3].set_walls(T,F,F,F)
        
        grid[6][12].set_walls(T,T,F,F)
        grid[6][11].set_walls(F,F,F,T)
        grid[5][12].set_walls(F,F,T,F)
        
        #CENTER
        grid[7][7].set_walls(T,T,F,F)
        grid[7][6].set_walls(F,F,F,T)
        grid[6][7].set_walls(F,F,T,F)
        grid[8][7].set_walls(F,T,T,F)
        grid[8][6].set_walls(F,F,F,T)
        grid[9][7].set_walls(T,F,F,F)
        grid[8][8].set_walls(F,F,T,T)
        grid[8][9].set_walls(F,T,F,F)
        grid[9][8].set_walls(T,F,F,F)
        grid[7][8].set_walls(T,F,F,T)
        grid[7][9].set_walls(F,T,F,F)
        grid[6][8].set_walls(F,F,T,F)
        
        grid[9][4].set_walls(F,T,T,F)
        grid[9][3].set_walls(F,F,F,T)
        grid[10][4].set_walls(T,F,F,F)
       
        grid[9][15].set_walls(F,F,T,T)
        grid[10][15].set_walls(T,F,F,T)
        
        grid[10][6].set_walls(T,T,F,F)
        grid[10][5].set_walls(F,F,F,T)
        grid[9][6].set_walls(F,F,T,F)
        
        grid[10][8].set_walls(F,F,T,T)
        grid[10][9].set_walls(F,T,F,F)
        grid[11][8].set_walls(T,F,F,F)
        
        grid[10][0].set_walls(F,T,T,F)
        grid[11][0].set_walls(T,T,F,F)
        
        grid[11][13].set_walls(T,T,F,F)
        grid[11][12].set_walls(F,F,F,T)
        grid[10][13].set_walls(F,F,T,F)
        
        grid[12][7].set_walls(T,F,F,T)
        grid[12][8].set_walls(F,T,F,F)
        grid[11][7].set_walls(F,F,T,F)
        
        grid[13][1].set_walls(T,F,F,T)
        grid[13][2].set_walls(F,T,F,F)
        grid[12][1].set_walls(F,F,T,F)
        
        grid[13][9].set_walls(F,T,T,F)
        grid[13][8].set_walls(F,F,F,T)
        grid[14][9].set_walls(T,F,F,F)
        
        grid[14][3].set_walls(F,F,T,T)
        grid[14][4].set_walls(F,T,F,F)
        grid[15][3].set_walls(T,F,T,F)
        
        grid[14][14].set_walls(T,F,F,T)
        grid[14][15].set_walls(F,T,F,T)
        grid[13][14].set_walls(F,F,T,F)
        
        grid[15][4].set_walls(F,F,T,T)
        grid[15][5].set_walls(F,T,T,F)
        
        grid[15][11].set_walls(F,F,T,T)
        grid[15][12].set_walls(F,T,T,F)
        
        
        
        
        
        
        
    
