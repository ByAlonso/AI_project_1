from grid import Grid


n_tiles = 16
margin = 50
def setup():
    size(900, 900)
    grid = Grid(n_tiles,n_tiles)
    background(120);
    translate(margin, margin);
    grid.print_grid()
    
