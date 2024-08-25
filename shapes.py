from canvas import Canvas

class Rectangle:
  '''
  Object to draw a rectangle
  '''
  def __init__(self, width,  height, x, y, color):
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    self.color = color

  def draw(self, canvas: Canvas):
    canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
  '''
  Object to draw a square
  '''
  def __init__(self, length, x, y, color):
    self.length = length
    self.x = x
    self.y = y
    self.color = color

  def draw(self, canvas: Canvas):
    canvas.data[self.x: self.x + self.length, self.y: self.y + self.length] = self.color

