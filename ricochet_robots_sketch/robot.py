COLORS = {'red': color(255,0,0), 'blue': color(0,0,255), 'green': color(0,255,0), 'yellow': color(255,255,0)}
import time
def is_integer(a, rel_tol=1e-9, abs_tol=0.0):
    b = round(a)
    return abs(a - b) <= rel_tol #max(rel_tol * max(abs(a), abs(b)), abs_tol)


class Robot:
    def __init__(self,x_pos, y_pos, w, clr):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.w = w
        self.name = clr
        self.clr = color(COLORS[clr])
        self.selected = False
        
        # Animation
        self.i = x_pos
        self.j = y_pos
    
    def move_robot(self, grid, dir, step=1):
        grid[self.y_pos][self.x_pos].set_robot(None)
        if dir == 'right':
            move = step if self.x_pos + 1 < 16 and (grid[self.y_pos][self.x_pos].has_right_wall or grid[self.y_pos][self.x_pos + 1].is_occupied) == False else 0
            self.i += move
        elif dir == 'left':
            move = step if self.x_pos - 1 >= 0 and (grid[self.y_pos][self.x_pos].has_left_wall or grid[self.y_pos][self.x_pos - 1].is_occupied) == False else 0
            self.i -= move
        elif dir == 'up':
            move = step if self.y_pos - 1 >= 0 and (grid[self.y_pos][self.x_pos].has_up_wall or grid[self.y_pos - 1][self.x_pos].is_occupied) == False else 0
            self.j -= move
        elif dir == 'down':
            move = step if self.y_pos + 1 < 16 and (grid[self.y_pos][self.x_pos].has_down_wall or grid[self.y_pos + 1][self.x_pos].is_occupied) == False else 0
            self.j += move
        
        
        # print(self.y_pos, self.j, is_integer(self.j))
        self.x_pos = int(round(self.i)) if is_integer(self.i) else self.x_pos
        self.y_pos = int(round(self.j)) if is_integer(self.j) else self.y_pos
        grid[self.y_pos][self.x_pos].set_robot(self)
        if move == 0:
            return False
        else:
            return True        
                
    def print_robot(self):
        w = self.w
        x = self.i * w + w/2
        y = self.j * w + w/2

        fill(self.clr)
        if not self.selected:
            noStroke()   
        ellipse(x, y, w/2.8, w/1.2)
        ellipse(x, y+w/10, w/2, w/2)
        ellipse(x, y+w/3, w/2.5, w/5)
    
        stroke(153)
        fill(255)    
    
