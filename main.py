import lc_timer
import lc_board


class LightCycle:

   def __init__(self):
      self.frame = Board()
      self.timer = None

   def destroy(self):
      """Terminate the timer on the way out, or it keeps running."""
      self.timer.destroy()
      tkinter.Frame.destroy(self)