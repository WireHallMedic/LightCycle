import tkinter
from lc_constants import *

#declare constants
windowWidth = 800
windowHeight = 500
windowSize = "{}x{}".format(windowWidth, windowHeight)
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
      """Draws the board as a table of squares """
      for item in self.imgList:
         self.canvas.delete(item)
      self.imgList = []
      for x in range(len(self.board)):
         for y in range(len(self.board[0])):
            color = EMPTY_COLOR
            if self.board[x][y] == PLAYER_ONE:
               color = HOST_COLOR
            elif self.board[x][y] == PLAYER_TWO:
               color = CLIENT_COLOR
            elif self.board[x][y] == WALL:
               color = WALL_COLOR
            self.imgList.append(self.canvas.create_rectangle(x * tileSize, y * tileSize, (x * tileSize) + tileSize - 1, (y * tileSize) + tileSize - 1, fill = color))
      #self.canvas.update_idletasks()
   
   def setBoard(self, boardStr):
      for x in range(boardDimension):
         for y in range(boardDimension):
            charIndex = x + (y * boardDimension)
            self.board[x][y] = Int(boardStr[charIndex])
   
if __name__ == "__main__":
   root = tkinter.Tk()
   root.title("LightCycle")
   root.geometry(windowSize)
   app = lc_board(master = root)
   
   app.board[1][boardDimension // 2] = PLAYER_ONE
   app.board[boardDimension - 2][boardDimension // 2] = PLAYER_TWO
   for i in range(boardDimension):
      app.board[i][0] = WALL
      app.board[i][boardDimension - 1] = WALL
      app.board[0][i] = WALL
      app.board[boardDimension - 1][i] = WALL
   app.drawBoard()
   
   # needs to be last, doesn't return
   root.mainloop()