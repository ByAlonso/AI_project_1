from tile import Tile
from goal import Goal
from robot import Robot
import random
import time

T = True
F = False
class Grid:
    def __init__(self,cols,rows):
        self.cols = cols
        self.rows = rows
        self.robot_number = 5
        self.goals = []
        self.grid = self.create_grid()
        self.robots = self.generate_robots()
        # self.robots = self.generate_robots_fixed() #test
        
        self.new_goal = None
        self.retrieve_goal()
        
    def create_grid(self):
        grid = self.create_outter_walls()
        self.create_inner_walls(grid)
        self.create_goals(grid)
        return grid
    
    def print_grid(self):
        for row in self.grid:
            for tile in row:
                tile.print_tile()
        self.print_restricted_area()     
        self.print_robot() 
               
    def print_robot(self):
        for row in self.grid:
            for tile in row:
                if tile.robot is not None:
                    tile.robot.print_robot() 
                     
    def select_robot(self,x_coord,y_coord):
        selected_robot = None
        for robot in self.robots:
            self.robots[robot].selected = False
            if self.robots[robot].x_pos == x_coord and self.robots[robot].y_pos == y_coord:
                selected_robot = self.robots[robot]
                if not selected_robot.selected:
                    selected_robot.selected = True
                    for r in self.robots:
                        self.robots[r].forbidden_move = None
        return selected_robot
                
    def retrieve_goal(self):
        if len(self.goals) > 0:
            rand = random.randint(0,len(self.goals) - 1)
            self.new_goal = self.goals.pop(rand)
            self.new_goal.console_goal()
        else:
            self.new_goal = None
            self.game_over()
        
    def check_goal(self,robot):
        arrived = False
        if robot.x_pos == self.new_goal.x_pos and robot.y_pos == self.new_goal.y_pos and robot.name == self.new_goal.clr_name:
            self.retrieve_goal()
            arrived = True
            #Add score to player
        return arrived
        
    def generate_robots(self):
        restricted_area = [[7,7],[8,8],[7,8],[8,7]]
        colors = ['green','blue','yellow','red', 'gray']
        occupied = []
        robot_dict = {}
        n = 0
        while(n < len(colors)):
            rand_x = random.randint(0,15)
            rand_y = random.randint(0,15)
            if not self.grid[rand_y][rand_x].is_goal and [rand_x,rand_y] not in occupied and [rand_x,rand_y] not in restricted_area:
                occupied.append([rand_x,rand_y])
                robot_dict[colors[n]] = Robot(rand_x,rand_y,50,colors[n])
                self.grid[rand_y][rand_x].set_robot(robot_dict[colors[n]])
                n += 1
        return robot_dict
        
    
    def print_restricted_area(self):
        fill(0)
        square(50 * 7, 50 * 7, 100)    
        fill(255) 
           
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
        
    def create_goals(self,grid):
        self.goals.extend([Goal('red','cross',1,2), Goal('blue', 'square', 6, 1), Goal('yellow', 'circle', 3, 6), Goal('green', 'triangle', 6, 5),
                           Goal('yellow', 'triangle', 9, 1), Goal('green', 'circle', 14, 2), Goal('red', 'square', 10, 4), Goal('blue','cross',12,6),
                           Goal('red', 'circle', 1, 13), Goal('yellow', 'cross', 3, 14), Goal('green','square',4,9), Goal('blue', 'triangle', 7, 12),
                           Goal('yellow','square',14,14), Goal('red', 'triangle', 8, 10), Goal('blue', 'circle', 9, 13), Goal('green', 'cross', 13, 11)])
        
        for g in self.goals:
            grid[g.y_pos][g.x_pos].set_goal(g)
        
    def game_over(self):
        print("You have no more chips to pick up")
        
        
        
        
    
