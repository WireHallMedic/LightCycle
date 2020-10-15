import tkinter
import threading
import time
from lc_constants import *

#declare constants
windowWidth = 800
windowHeight = 500
windowSize = "{}x{}".format(windowWidth, windowHeight)
tileSize = 10

class Board(tkinter.Frame):

   def __init__(self):
      """Initialize frame"""
      root = tkinter.Tk()
      root.title("LightCycle")
      root.geometry(windowSize)
      super(Board, self).__init__(root)
      self.canvas = tkinter.Canvas(root, width = windowWidth, height = windowHeight)
      self.canvas.pack()
      
      self.imgArr = None
      self.board = None
      self.playerOneCollision = False
      self.playerTwoCollision = False
      self.generateBoard()
      self.generateImgArr()
      self.running = False
      self.loopThread = threading.Thread(target = self.drawLoop, daemon = True)
      self.loopThread.start()
   
   def drawLoop(self):
      while True:
         if self.running:
            self.drawBoard()
            time.sleep(.1)
   
   def drawBoard(self):
      """Draws the board as a table of squares 
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
            self.imgList.append(self.canvas.create_rectangle(x * tileSize, y * tileSize, (x * tileSize) + tileSize - 1, (y * tileSize) + tileSize - 1, fill = color))"""
      self.canvas.update_idletasks()
   
   def generateBoard(self):
      """Set the initial board state """
      self.board = [[EMPTY for y in range(boardDimension)] for x in range(boardDimension)]
      for i in range(boardDimension):
         self.board[i][0] = WALL
         self.board[i][boardDimension - 1] = WALL
         self.board[0][i] = WALL
         self.board[boardDimension - 1][i] = WALL
   
   def generateImgArr(self):
      """Set the full image array """
      self.imgArr = [[None for y in range(boardDimension)] for x in range(boardDimension)]
      for x in range(boardDimension):
         for y in range(boardDimension):
            self.setImgArrCell(x, y)
   
   def setImgArrCell(self, x, y):
      color = EMPTY_COLOR
      if self.board[x][y] == PLAYER_ONE:
         color = HOST_COLOR
      elif self.board[x][y] == PLAYER_TWO:
         color = CLIENT_COLOR
      elif self.board[x][y] == WALL:
         color = WALL_COLOR
      oldTile = self.imgArr[x][y]
      self.imgArr[x][y] = self.canvas.create_rectangle(x * tileSize, y * tileSize, (x * tileSize) + tileSize - 1, (y * tileSize) + tileSize - 1, fill = color)
      if getattr(oldTile, "destroy", None) is not None:
         oldTile.destroy()
   
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
      self.setImgArrCell(x, y)
   
   def playerOneCollision(self):
      return playerOneCollision
   
   def playerTwoCollision(self):
      return playerTwoCollision
   
   def collisionOccured(self):
      return playerOneCollision or playerTwoCollision
   
   def destroy(self):
      """Terminate the timer on the way out, or it keeps running."""
      tkinter.Frame.destroy(self)
   
if __name__ == "__main__":
   app = Board()
   app.mark(1, boardDimension // 2, PLAYER_ONE)
   app.mark(boardDimension - 2, boardDimension // 2, PLAYER_TWO)
   app.running = True
   app.mainloop()
   