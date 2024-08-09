from pynput.keyboard import Listener
from tkinter import *
from tkinter import ttk
import winsound
import random

tk_window = Tk()
tk_window.geometry("380x180")
tk_window.config(bg="yellow")

left = ttk.Label(tk_window, text="we're meowing now")
left.pack()

# on press event
def on_release(key):
  # 3 distinct meows, i want them to play wheneveri  press a button, a given, and also i want them not to repeat themselves but also be
  # semi random, so i want to create a bag of 3 system and i want a 10% chance to quack
  rng = random.randint(1,5)
  rng2 = random.randint(1,1000)
  if rng2 == 1000:
     winsound.PlaySound("C:\projects\meow-keys\quack.wav".format(rng), winsound.SND_FILENAME | winsound.SND_ASYNC)
  else:
    winsound.PlaySound("C:\projects\meow-keys\meow-{0}.wav".format(rng), winsound.SND_FILENAME | winsound.SND_ASYNC)

keyboard_listener = Listener(on_release=on_release)
keyboard_listener.start()

tk_window.mainloop()
