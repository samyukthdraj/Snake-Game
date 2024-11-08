from turtle import *

POSITIONS = [(0,0), (-20,0), (-40,0)] 
MOVE_DIST = 25
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.segments[0].color("purple")  # Set the color of the snake head

#snake shape being created with 3 squares of dimensions 20x20
    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)
  

#extending the snake
    def add_segment(self,position):
        new_segment = Turtle("square")  # Create a new Turtle object for each segment
        new_segment.color("white")       # Set the color (optional)
        new_segment.penup()             # Prevent drawing lines while moving
        new_segment.goto(position)
        self.segments.append(new_segment)    # Store the segment in a list

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.segments[0].color("purple")

    def extend(self):
        self.add_segment(self.segments[-1].position())
        


#moving the snake forwards  
    def move(self):
        for seg_move in range (len(self.segments) -1 , 0, -1 ): #i want the snake's 3rd square to move to where the 2nd was, 2nd to move to where 1st was, 1st to move in a direction that the user gives.
    # so here in the range (start,stop,step) are basically the parameters, i want it to start from the last so i give len-1, stop at 0 ie the first square, and step to be -1 ie i--
            new_x = self.segments[seg_move-1].xcor() #new x [third square] takes the value of the previous square [2nd square]
            new_y = self.segments[seg_move-1].ycor() #new y [third square] takes the value of the previous square [2nd square]
            self.segments[seg_move].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DIST) #first square moves forward

#snake controlling with keystrokes
    def up(self):
        if self.segments[0].heading() != DOWN: #if head is pointing down the head then shouldnt be allowed to go up 
         self.segments[0].setheading(UP) #change the first square ie the head of the snake
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.segments[0].heading() != LEFT:
         self.segments[0].setheading(RIGHT)