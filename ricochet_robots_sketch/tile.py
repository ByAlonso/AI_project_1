class Tile:
    def __init__(self,x_pos, y_pos):
        self.robot = None
        self.goal = None
        self.is_goal = False
        self.has_up_wall = False
        self.has_left_wall = False
        self.has_right_wall = False
        self.has_down_wall = False
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def set_walls(self,up,left,down,right):
        self.has_up_wall = up
        self.has_left_wall = left
        self.has_down_wall = down
        self.has_right_wall = right
        
    def set_goal(self,goal):
        self.is_goal = True
        self.goal = goal
        
    def set_robot(self,robot):
        self.robot = robot
        # self.is_occupied = True if robot is not None else False
        
    def print_tile(self):
        strokeWeight(0)
        square(50 * self.x_pos, 50 * self.y_pos, 50)
        if self.goal is not None:
            self.goal.print_goal(self.x_pos,self.y_pos)
        self.print_walls()
        
        
        
    def print_walls(self):
        strokeWeight(8)
        stroke(0)
        if self.has_up_wall:
            line(50 * self.x_pos, 50 * self.y_pos,50 * self.x_pos + 50, 50 * self.y_pos)
        if self.has_left_wall:
            line(50 * self.x_pos, 50 * self.y_pos,50 * self.x_pos, 50 * self.y_pos + 50)
        if self.has_down_wall:
            line(50 * self.x_pos, 50 * self.y_pos + 50,50 * self.x_pos + 50, 50 * self.y_pos + 50)
        if self.has_right_wall:
            line(50 * self.x_pos + 50, 50 * self.y_pos,50 * self.x_pos + 50, 50 * self.y_pos + 50)
        stroke(153)
            
    
        
        
            
        
