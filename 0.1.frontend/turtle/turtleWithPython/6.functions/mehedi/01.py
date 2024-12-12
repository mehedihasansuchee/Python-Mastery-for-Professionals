from turtle import *

class DrawLine:
    def __init__(self, length):
        self.t = Turtle()
        self.length = length

    def draw(self):
        self.t.forward(self.length)
         
    def finish(self):
        done()

line = DrawLine(length=100)
line.draw()
line.finish()