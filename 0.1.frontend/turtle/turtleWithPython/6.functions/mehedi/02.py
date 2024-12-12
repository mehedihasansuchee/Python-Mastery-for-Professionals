from turtle import *        # without forloop

class DrawSquare:
    def __init__(self, size):
        self.t = Turtle()
        self.size = size

    def draw(self):
        self.t.forward(self.size)
        self.t.right(90)
        self.t.forward(self.size)
        self.t.right(90)
        self.t.forward(self.size)
        self.t.right(90)
        self.t.forward(self.size)

    def finish(self):
        done()

square = DrawSquare(size=150)
square.draw()
square.finish()