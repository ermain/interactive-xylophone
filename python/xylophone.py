from __future__ import division
import sys
sys.path.append('../common')
from core import *

import random
import numpy as np
import serial


class Xylophone(object):
  notes = [60,62,64,65,67,69,71,72,74,76,77,79,83]
  port = 'COM3' # '/dev/tty.HC-06-DevB'

  def __init__(self, key_hit_cb):
    super(Xylophone, self).__init__()
    # set up serial
    print "setting up serial..."
    try:
      self.ser = serial.Serial(\
            port=self.port,\
            baudrate=9600,\
            parity=serial.PARITY_NONE,\
            timeout=1,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS)
      print "opened port ", self.port
      self.ser.flushInput()
      self.ser.flushOutput()
    except serial.SerialException:
      print "cannot open port ", self.port, "error: ", sys.exc_info()[0]
    except:
      print "unexpected error:", sys.exc_info()[0]
    print "after setting up serial"
    self.first_update = True
    self.on_key_hit_cb = key_hit_cb

  def on_update(self):
    if self.first_update:
      self.first_update = False
      self.ser.flushInput()
    else:
      data_str = self.ser.readline()
      if data_str != "":
        note_idx = int(data_str)
        print note_idx
        self.on_key_hit(self.notes[note_idx])

  def disable(self):
    self.ser.close()

  def enable(self):
    self.ser.open()
 
  def on_key_hit(self, note):
    self.on_key_hit_cb(note)
