import turtle
from walker2 import Walker

turtle.penup()
turtle.hideturtle()

def on_motion(event):
    x = event.x - turtle.window_width() / 2
    y = -event.y + turtle.window_height() / 2
    print(x, y)

# turtle.getcanvas().bind("<Motion>", on_motion)

walker = Walker()

def move(x, y):
    walker.jump(x, y)

turtle.onscreenclick(move)

while True:
    walker.step()
    turtle.goto(walker.getX(), walker.getY())
    turtle.dot(5, "blue")


turtle.screen.mainloop()