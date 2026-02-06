  for (let i = 0; i < board.length; i++) {
    const rowMap = new Map();
    for (let j = 0; j < board[i].length; j++) {
      rowMap.set(board[i][j], (rowMap.get(board[i][j]) || 0) + 1);
    }
    for (let [key, value] of rowMap) {
      if (key != ".") {
        if (value > 1) {
          rowWiseResult = false;
        }
      }
    }
  }