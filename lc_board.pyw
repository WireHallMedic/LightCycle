import tkinter
import lc_constants

#declare constants
windowWidth = 800
windowHeight = 500
windowSize = "{}x{}".format(windowWidth, windowHeight)
boardDimension = 31
EMPTY = 0
PLAYER_ONE = 1
PLAYER_TWO = 2
tileSize = 10

class lc_board(tkinter.Frame):

   def __init__(self, master):
      """Initialize frame"""
      super(lc_board, self).__init__(master)
      self.canvas = tkinter.Canvas(master, width = windowWidth, height = windowHeight)
      self.canvas.pack()
      
      self.board = [[0 for y in range(boardDimension)] for x in range(boardDimension)]
      self.imgList = []
      
      self.drawBoard()
   
   def drawBoard(self):
      for item in self.imgList:
         self.canvas.delete(item)
      for x in range(len(self.board)):
         for y in range(len(self.board[0])):
            color = lc_constants.EMPTY_COLOR
            if self.board[x][y] == PLAYER_ONE:
               color = lc_constants.HOST_COLOR
            elif self.board[x][y] == PLAYER_TWO:
               color = lc_constants.CLIENT_COLOR
            self.imgList.append(self.canvas.create_rectangle(x * tileSize, y * tileSize, (x * tileSize) + tileSize - 1, (y * tileSize) + tileSize - 1, fill = color))
      self.canvas.update_idletasks()
   
if __name__ == "__main__":
   root = tkinter.Tk()
   root.title("LightCycle")
   root.geometry(windowSize)
   app = lc_board(master = root)
   root.mainloop()