def validSudoku(board):
  # row wise 
  for i in range(9):
    rows = set()
    for j in range(9):
      if board[i][j] in rows:
        return False
      elif(board[i][j] != "."):
        rows.add(board[i][j])
        
  # column wise 
  for i in range(9):
    cols = set()
    for j in range(9):
      if board[j][i] in cols:
        return False
      elif(board[j][i] != "."):
        cols.add(board[j][i])
    
  #grid wise
  starts = [(0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
          ]
  for i,j in starts:
    grids = set()
    for row in range(i, i+3):
      for col in range(j, j+3):
        if board[row][col] in grids:
          return False
        elif(board[row][col] !="."):
          grids.add(board[row][col])
  return True

board =[
  ["1","2",".",".","3",".",".",".","."],
  ["4",".",".","5",".",".",".",".","."],
  [".","9","1",".",".",".",".",".","3"],
  ["5",".",".",".","6",".",".",".","4"],
  [".",".",".","8",".","3",".",".","5"],
  ["7",".",".",".","2",".",".",".","6"],
  [".",".",".",".",".",".","2",".","."],
  [".",".",".","4","1","9",".",".","8"],
  [".",".",".",".","8",".",".","7","9"]]


answer = validSudoku(board)
print("Answer: ", answer)