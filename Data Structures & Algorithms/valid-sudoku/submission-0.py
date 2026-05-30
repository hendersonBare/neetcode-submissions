class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}
        for i in range(len(board)): #rows
            for j in range(len(board[0])): #columns
                curr_val = board[i][j]
                if curr_val == ".":
                    continue
                else:
                    if i in rows:
                        if curr_val in rows[i]:
                            return False
                        else:
                            rows[i].append(curr_val)
                    else:
                        rows[i] = [curr_val]
                    
                    if j in cols:
                        if curr_val in cols[j]:
                            return False
                        else:
                            cols[j].append(curr_val)
                    else:
                        cols[j] = [curr_val]

                    base_row = int((i - (i % 3)) / 3)
                    base_col = int((j - (j % 3)) / 3)

                    if (base_row, base_col) in boxes:
                        if curr_val in boxes[(base_row, base_col)]:
                            return False
                        else:
                            boxes[(base_row, base_col)].append(curr_val)
                    else:
                        boxes[(base_row, base_col)] = [curr_val]

        return True
