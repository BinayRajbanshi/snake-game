from turtle import  Turtle

FONT = ("Poppins", 20 , "bold")
ALIGN = "center"

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_high_score()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 290)
        self.update_scoreboard()

    def get_high_score(self):
        with open("./high_score.txt") as f:
            self.high_score = int(f.read())

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGN, FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} \t High Score: {self.high_score}", False, ALIGN, FONT)

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()

    #implementing high score instead of game over
    def reset_score(self):
        #check if the score by user is higher or lower than high score
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./high_score.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
