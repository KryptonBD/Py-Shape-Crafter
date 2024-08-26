from canvas import Canvas  
from shapes import Square, Rectangle
from InquirerPy import inquirer

canvas_width = input('Enter the canvas width: ')
canvas_height = input('Enter the canvas height: ')

def let_user_pick(options: list[str], message: str):
  return inquirer.select(
    message,
    choices = options
  ).execute()
    

canvas_color = let_user_pick(['black', 'white'], 'Please Choose a canvas color')
color = {
  'black': (0, 0, 0),
  'white': (255, 255, 255)
}

canvas = Canvas(height=int(canvas_height), width=int(canvas_width), color=color[canvas_color])

while True:
  shape_types = ['Rectangle', 'Square', 'done']
  current_choice = let_user_pick(shape_types, 'Please choose a shape type')

  if current_choice == 'Rectangle':
    rx = input('Enter the X axis of the rectangle: ')
    ry = input('Enter the Y axis of the rectangle: ')
    rwidth = input('Enter the width of rectangle: ')
    rheight = input('Enter the height of the rectangle: ')
    red = input('How much red (0-255): ')
    green = input('How much green (0-255): ')
    blue = input('How much blue (0-255): ')
    rcolor = (int(red), int(green), int(blue))

    r1 = Rectangle(x=int(rx), y=int(ry), height=int(rheight), width=int(rwidth), color=rcolor)
    r1.draw(canvas)

  if current_choice == 'Square':
    sx = input('Enter the X axis of the square: ')
    sy = input('Enter the Y axis of the square: ')
    slength = input('Enter the length of the square: ')
    red = input('How much red (0-255): ')
    green = input('How much green (0-255): ')
    blue = input('How much blue (0-255): ')
    scolor = (int(red), int(green), int(blue))

    s1 = Square(x=int(sx), y=int(sy), length=int(slength), color=scolor)
    s1.draw(canvas)

  if current_choice == 'done':
    break

canvas.create('canvas.png')