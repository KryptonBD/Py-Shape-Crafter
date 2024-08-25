from canvas import Canvas  
from shapes import Square, Rectangle

canvas = Canvas(height=600, width=800, color=(255, 255, 255))

r1 = Rectangle(x=10, y=60, height=300, width=500, color=(0, 240, 100))
r1.draw(canvas)

s1 = Square(length=200, x=400, y=500, color=(120, 100, 200))
s1.draw(canvas)

canvas.create('canvas.png')