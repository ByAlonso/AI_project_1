class Goal:
    def __init__(self,clr,shp):
        self.clr = clr
        self.shp = shp
        
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
        stroke(153)
        fill(255)
