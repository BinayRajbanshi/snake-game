import turtle as t

class Border(t.Turtle):
    def __init__(self):
        super().__init__()
        self.create_border()

    def create_border(self):
        self.hideturtle()
        self.penup()
        self.goto(-290, 290)
        self.pendown()
        self.pensize(3)
        self.color("white")  # Changed to white to be visible on black background
        for _ in range(4):
            self.forward(580)
            self.right(90)