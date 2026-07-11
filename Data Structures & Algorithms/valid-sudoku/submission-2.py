class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for x in range(9)]
        col_set = [set() for x in range(9)]
        box_set = [set() for x in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == ".":
                    continue
                if curr in row_set[i]:
                    return False
                else:
                    row_set[i].add(curr)
                if curr in col_set[j]:
                    return False
                else:
                    col_set[j].add(curr)
                box_indx = ((i//3)*3) + (j//3)
                if curr in box_set[box_indx]:
                    return False
                else:
                    box_set[box_indx].add(curr)
        return True