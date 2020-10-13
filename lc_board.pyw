import tkinter

#declare constants
windowWidth = 800
windowHeight = 500
windowSize = "{}x{}".format(windowWidth, windowHeight)
    

class lc_board(tkinter.Frame):

   def __init__(self, master):
      """Initialize frame"""
      super(lc_board, self).__init__(master)
      self.canvas = tkinter.Canvas(master, width = windowWidth, height = windowHeight)
      self.canvas.pack()
         
if __name__ == "__main__":
   root = tkinter.Tk()
   root.title("LightCycle")
   root.geometry(windowSize)
   app = lc_board(master = root)
   root.mainloop()