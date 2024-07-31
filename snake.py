import  turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for square in self.position:
            self.create_segment(square)

    def create_segment(self, square):
        new_segment = turtle.Turtle('square')
        new_segment.penup()
        new_segment.speed(0)
        new_segment.color('white')
        new_segment.goto(square)
        self.segments.append(new_segment)

    def move_snake(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
