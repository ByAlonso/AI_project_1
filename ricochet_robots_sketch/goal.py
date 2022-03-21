COLORS = {'red': color(255,0,0), 'blue': color(0,0,255), 'green': color(0,255,0), 'yellow': color(255,255,0)}
class Goal:
    def __init__(self,clr,shp,x_pos,y_pos):
        self.clr = COLORS[clr]
        self.clr_name = clr
        self.shp = shp
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def print_goal(self,x_pos,y_pos):
        strokeWeight(3)
        fill(self.clr)
        stroke(0)
        if self.shp == 'triangle':
            triangle(50 * x_pos + 10,50 * y_pos + 10,50 * x_pos + 10,50 * y_pos + 40,50 * x_pos + 40,50 * y_pos + 25)
        if self.shp == 'square':
            square(50 * x_pos + 15,50 * y_pos + 15,25)
        if self.shp == 'cross':
            stroke(self.clr)
            line(50 * x_pos + 10,50 * y_pos + 10,50 * x_pos + 40,50 * y_pos + 40)
            line(50 * x_pos + 10,50 * y_pos + 40,50 * x_pos + 40,50 * y_pos + 10)
        if self.shp == 'circle':
            circle(50 * x_pos + 25,50 * y_pos + 25,30)
        stroke(153)
        fill(255)
    def console_goal(self):
        print("You have to reach " + self.clr_name + " with shape " + self.shp)
