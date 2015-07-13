# staff.py
# Musical staff that shows notes that you pass it.

# Retains history of notes

import sys
sys.path.append("../common")
from core import *
from graphics import *

space_height = 40
line_thick = 4

class Staff(InstructionGroup):
  
  def __init__(self, type, pos, height, width):
    super(Staff, self).__init__()

    # there is probably a better way to do this. 
    line_notes = []
    space_notes = []
    line_notes_below = []
    line_notes_above = []
    space_notes_below = []
    space_notes_above = []

    # what type of midi notes belong
    if type == "bass":
      line_notes = [43,47,50,53,57]
      space_notes = [45,48,52,55]
      line_notes_below = [33,36,40]
      line_notes_above = [60,64,67,71,74,77]
      space_notes_below = [31,35,37,41]
      space_notes_above = [65,69,72,76]

    elif type == "treble":
      line_notes = [64,67,71,74,77]
      space_notes = [65,69,72,76]
      line_notes_below = [43,47,50,53,57,60]
      line_notes_above = [81,84,88,91,95]
      space_notes_below = [45,48,52,55]
      space_notes_above = [79,83,86,89,93,96]

    self.note_heads = []
    self.note_values = []
    self.lines = []

    # create the lines
    for i in range(5):
      self.add(Line(points = [pos[0],pos[1]+i*space_height,\
          pos[0]+width,pos[1]+i*space_height], width = line_thick))
  
    # here we'll want to add a picture of the staff type
    # todo: add picture




class Note(InstructionGroup):
  
  def __init__(self, pos, line_off_staff):
    self.pos = pos
    self.head = Ellipse(segments = 20)
    self.circle.size = space_height*2, space_height*2
    self.circle.pos = self.pos
    self.line = None
    if line_off_staff:
      self.line = Line(points = [pos[0]-space_height/2, pos[1], \
          pos[0]+space_height/2, pos[1]], width = line_thick)
  
  def show():
    self.add(self.circle)
    if self.line is not None:
      self.add(self.line)

  def hide():
    self.remove(self.circle)
    if self.line is not None:
      self.remove(self.line)

