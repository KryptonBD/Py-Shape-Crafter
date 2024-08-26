from canvas import Canvas

class Shape:
  '''
  Provide a common class for all shapes
  '''
  def __init__(self, x, y, color):
    self.x = x
    self.y = y
    self.color = color

class Rectangle(Shape):
  '''
  Object to draw a rectangle
  '''
  def __init__(self, width,  height, x, y, color):
    super().__init__(x, y, color)
    self.width = width
    self.height = height

  def draw(self, canvas: Canvas):
    canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square(Shape):
  '''
  Object to draw a square
  '''
  def __init__(self, length, x, y, color):
    super().__init__(x, y, color)
    self.length = length

  def draw(self, canvas: Canvas):
    canvas.data[self.x: self.x + self.length, self.y: self.y + self.length] = self.color

