from canvas import Canvas  
from shapes import Square, Rectangle
from InquirerPy import inquirer

canvas_width = input('Enter the canvas width: ')
canvas_height = input('Enter the canvas height: ')

def get_user_input(options: list[str], message: str):
  '''
  Let user choose an option from a list

  :param options list of options to choose from
  :param message message to display to the user
  :return the selected option
  '''
  return inquirer.select(
    message,
    choices = options
  ).execute()

def get_color():
  '''
  Get color from the user 
  
  :return: a tuple represnt the RGB color
  '''
  red = input('How much red (0-255): ')
  green = input('How much green (0-255): ')
  blue = input('How much blue (0-255): ')

  return (int(red), int(green), int(blue))
   
# Let use choose the canvas color
canvas_color = get_user_input(['black', 'white'], 'Please Choose a canvas color')
color = {
  'black': (0, 0, 0),
  'white': (255, 255, 255)
}

# Create the canvas
canvas = Canvas(height=int(canvas_height), width=int(canvas_width), color=color[canvas_color])

while True:
  shape_types = ['Rectangle', 'Square', 'done']
  current_choice = get_user_input(shape_types, 'Please choose a shape type')

  if current_choice == 'Rectangle':
    rx = input('Enter the X axis of the rectangle: ')
    ry = input('Enter the Y axis of the rectangle: ')
    rwidth = input('Enter the width of rectangle: ')
    rheight = input('Enter the height of the rectangle: ')
    rcolor = get_color()

    # Create and draw rectangle
    r1 = Rectangle(x=int(rx), y=int(ry), height=int(rheight), width=int(rwidth), color=rcolor)
    r1.draw(canvas)

  if current_choice == 'Square':
    sx = input('Enter the X axis of the square: ')
    sy = input('Enter the Y axis of the square: ')
    slength = input('Enter the length of the square: ')
    scolor = get_color()

    # Create and draw square
    s1 = Square(x=int(sx), y=int(sy), length=int(slength), color=scolor)
    s1.draw(canvas)

  if current_choice == 'done':
    break

# Save the image
canvas.create('canvas.png')