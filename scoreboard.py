from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.pu()
        self.color("black")
        self.goto(-230,270)
        self.ht()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=(FONT))
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER")
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
