import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.create_segment(position)

    def create_segment(self, position):
        new_snake_segment = t.Turtle("square")
        new_snake_segment.penup()
        new_snake_segment.color("white")
        new_snake_segment.goto(position)
        self.segments.append(new_snake_segment)


    def extend_segment(self):
        last_segment_position = self.segments[-1].position()
        self.create_segment(last_segment_position)


    # MY INITIAL APPROACH
    # def increase_length(self):
    #     new_snake_segment = t.Turtle("square")
    #     new_snake_segment.penup()
    #     new_snake_segment.color("white")
    #     new_snake_segment.speed("fastest")
    #     self.segments.append(new_snake_segment)
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            pos_to_move_x = self.segments[i - 1].xcor()
            pos_to_move_y = self.segments[i - 1].ycor()
            self.segments[i].goto(pos_to_move_x, pos_to_move_y)

        self.segments[0].forward(MOVE_FORWARD)

    def up(self):
        if self.segments[0].heading() != 270 :
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1200,1200)
        self.segments.clear()
        self.create_snake()