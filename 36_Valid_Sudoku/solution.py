'''
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

**Example 1:**

```
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

```

**Example 2:**

```
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the5 in the top left corner being modified to8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

```

**Constraints:**

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.
'''
'''
## Approach:

1. Row wise check and check the data is already present in the set [will create a hash map key as row number and value encountered will be saved in the set]
2. Same do with cols wise 
3. For Square wise, we will follow one simple solution:
    1. in that square hashmap, the key will be a tuple of (row//3, col//3)
    so the square hashmap will also contain 9 keys as 

        (0, 0), (0, 1)  …….  (2, 2)
'''


def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c].isnumeric():
                    if (board[r][c] in rows[r]
                        or board[r][c] in cols[c]
                        or board[r][c] in squares[(r // 3, c // 3)]):
                        return False

                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r // 3, c // 3)].add(board[r][c])
        return True
