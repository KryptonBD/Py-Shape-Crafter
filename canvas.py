from PIL import Image
import numpy as np
 
class Canvas:
  '''
  Draw all shapes here
  '''

  def __init__(self, width, height, color):
    self.width = width
    self.height = height
    self.color = color

    # Create an array or zeros
    self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
    self.data[:] = self.color #replace the zeros with color

  def create(self, image_path):
    '''
    Save the canvas to an image file
    '''
    img = Image.fromarray(self.data, 'RGB')
    img.save(image_path)
 