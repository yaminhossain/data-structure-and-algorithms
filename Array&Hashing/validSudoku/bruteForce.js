const validSudoku = (board) => {
  const rowWiseCalculation = (n) => {
    for (let i = 0; i < n; i++) {
      const rowMap = new Map();
      for (let j = 0; j < board[i].length; j++) {
        rowMap.set(board[i][j], (rowMap.get(board[i][j]) || 0) + 1);
      }
      for (let [key, value] of rowMap) {
        if (key != ".") {
          if (value > 1) {
            return false;
          }
        }
      }
    }
    return true;
  };

  const columnWiseCalculation = (n) => {
    for (let i = 0; i < n; i++) {
      const columnMap = new Map();
      for (let j = 0; j < board.length; j++) {
        columnMap.set(board[j][i], (columnMap.get(board[j][i]) || 0) + 1);
      }
      for (let [key, value] of columnMap) {
        if (key != ".") {
          if (value > 1) {
            columnWiseResult = false;
          }
        }
      }
    }
    return true;
  };

  let rowWiseResult = rowWiseCalculation(board.length);
  let columnWiseResult = columnWiseCalculation(board.length);

  //column

  return columnWiseResult && rowWiseResult;
};

const board = [
  ["1", "2", ".", ".", "3", ".", ".", ".", "."],
  ["4", ".", ".", "5", ".", ".", ".", ".", "."],
  [".", "9", "1", ".", ".", ".", ".", ".", "3"],
  ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
  [".", ".", ".", "8", ".", "3", ".", ".", "5"],
  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
  [".", ".", ".", ".", ".", ".", "2", ".", "."],
  [".", ".", ".", "4", "1", "9", ".", ".", "8"],
  [".", ".", ".", ".", "8", ".", ".", "7", "9"],
];

const result = validSudoku(board);

console.log("Result", result);
