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
      
      self.imgList = []
      self.board = None
      self.playerOneCollision = False
      self.playerTwoCollision = False
      
      self.generateBoard()
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
   
   def generateBoard(self):
      """Set the initial board state """
      self.board = [[EMPTY for y in range(boardDimension)] for x in range(boardDimension)]
      for i in range(boardDimension):
         self.board[i][0] = WALL
         self.board[i][boardDimension - 1] = WALL
         self.board[0][i] = WALL
         self.board[boardDimension - 1][i] = WALL
   
   def mark(self, x, y, playerNum):
      """ Mark the board with a player's tail, noting if a collision occured """
      if self.board[x][y] != EMPTY:
         if playerNum == PLAYER_ONE:
            self.playerOneCollision = True
            if self.board[x][y] == PLAYER_TWO:
               self.playerTwoCollision = True
         if playerNum == PLAYER_TWO:
            self.playerTwoCollision = True
            if self.board[x][y] == PLAYER_ONE:
               self.playerOneCollision = True
      self.board[x][y] = playerNum
   
   def playerOneCollision(self):
      return playerOneCollision
   
   def playerTwoCollision(self):
      return playerTwoCollision
   
   def collisionOccured(self):
      return playerOneCollision or playerTwoCollision
   
if __name__ == "__main__":
   root = tkinter.Tk()
   root.title("LightCycle")
   root.geometry(windowSize)
   app = lc_board(master = root)
   
   app.board[1][boardDimension // 2] = PLAYER_ONE
   app.board[boardDimension - 2][boardDimension // 2] = PLAYER_TWO
   app.mark(3, 3, 1)
   app.drawBoard()
   
   # needs to be last, doesn't return
   root.mainloop()