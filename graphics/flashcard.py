from __future__ import division
# import necessary files
import sys
sys.path.append('./common')
from core import *      # These are all file names located in the
from graphics import *  # "common" folder.

# kivy files
from kivy.uix.label import Label
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.graphics import PushMatrix, PopMatrix, Translate, Scale, Rotate, Mesh
from kivy.clock import Clock as kivyClock
from kivy.core.image import Image

# other
from random import random

class FlashcardData(object):
  def __init__(self, data_loc):
    self.flashcard_data = []
    self._read_in_data(data_loc)

  def _read_in_data(self, data_loc):
    self.flashcard_data = [("Hit C", None, 60),("Hit D", None, 62),\
        ("Hit E", None, 64),("Hit F", None, 65)]
#    with open(data_loc) as f:
#      begin = False
#      for line in f.readlines()
#        if "{" in line and not begin:
#          begin = True

  def answer_at_idx(self, idx):
    return self.flashcard_data[idx][2]

class Flashcard(Widget):
  def __init__(self, pos, w, h, text, img, answer):
    super(Flashcard, self).__init__()
    self.text = text
    self.img = img
    self.answer = answer
    self.pos = pos

    self.w = w
    self.h = h

    self.label = Label(text = self.text, pos = (self.pos[0] - self.w/2,\
        self.pos[1] - self.h/6), size = (self.w, self.h),\
        valign='top', font_size = '24sp')
    
    self.canvas.add(Color(random(), random(), random()))
    self.bg = Rectangle(pos = (self.pos[0] - self.w/2, self.pos[1] - self.h/2))
    self.bg.size = self.w, self.h

  def show(self):
    self.canvas.add(self.bg)
    self.add_widget(self.label)

  def hide(self):
    self.canvas.remove(self.bg)
    self.remove_widget(self.label)

# a collection of flashcards
# handles input logic

class Deck(Widget):
  pause_len = 0.5
  w = 300
  h = 400
  def __init__(self, data_loc, pos):
    super(Deck, self).__init__()
    self.data = FlashcardData(data_loc)
    self.num_flash = len(self.data.flashcard_data)
    self.flashcards = []
    for flash in self.data.flashcard_data:
      self.flashcards.append(Flashcard(pos, self.w, self.h, \
          flash[0], flash[1], flash[2]))
      self.add_widget(self.flashcards[-1])
    self.ptr = 0
    self.pos = pos

    self.response = Label(text = "", pos = (self.pos[0] - self.w/2,\
        self.pos[1] - 5*self.h/6), size = (self.w, self.h),\
        valign='top', font_size = '24sp')

    self.flashcards[self.ptr].show()
    self.add_widget(self.response)
    self.pause = 0.5
    self.show_response_text = False

  def answer_cb(self, answer):
    if answer != self.data.answer_at_idx(self.ptr):
      self.response.text = "WRONG"
    else:
      self.response.text = "RIGHT"
      self.flashcards[self.ptr].hide()
      self.ptr = (self.ptr + 1) % self.num_flash
      self.flashcards[self.ptr].show()
      self.remove_widget(self.response)
      self.add_widget(self.response)
    self.show_response_text = True
    self.pause = self.pause_len

  def on_update(self, dt):
    if self.show_response_text == True:
      self.pause -= dt
      if self.pause <= 0:
        self.response.text = ""
        self.show_response_text = False

