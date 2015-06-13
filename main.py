# import necessary files
import sys
sys.path.append('./common')
from core import *      # These are all file names located in the
from graphics import *  # "common" folder.
from synth import *
from audio import *

sys.path.append('./input')
sys.path.append('./graphics')
from flashcard import *

class KeyboardFlashcardDemo(BaseWidget): 

  notes = [60,62,64,65,67,69,71,72,84]
  
  def __init__(self):
    super(KeyboardFlashcardDemo, self).__init__()
    # set up audio generators
    self.audio = Audio()
    self.synth = Synth('../FluidR3_GM.sf2')
    self.synth.program(0, 0, 40) # chan 0, bank 0, violin
    self.audio.add_generator(self.synth)

    self.deck = Deck("./graphics/flashcard_data.txt", (400,300))
    self.add_widget(self.deck)

  # on key press, the synth will make noises corresponding to pitches in notes
  # will also send a MIDI value to the flashcard deck
  def on_key_down(self, keycode, modifiers):
    if keycode[1] in "123456789":
      note = self.notes[int(keycode[1]) - 1]
      self.synth.noteon(0, note, 127)      
      self.deck.answer_cb(note)

  def on_key_up(self, keycode):
    if keycode[1] in "123456789":
      self.synth.noteoff(0, self.notes[int(keycode[1]) - 1])      
  
  def on_update(self) :
    dt = kivyClock.frametime
    self.deck.on_update(dt)

if len(sys.argv) >= 2:
  mode = int(sys.argv[1])
  run(eval(sys.argv[1]))

else:
  run(KeyboardFlashcardDemo)
