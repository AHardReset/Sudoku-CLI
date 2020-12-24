class Sudoku:
    def __init__(self, board:list[list] = []) -> None:
        """Init the Sudoku with a known board or generate a new one.

        Args:
            board (list[list], optional): Board to init the Sudoku. Defaults to [].
        """
        if board == []:
            self.board = self.generate_board()
        else:
            self.board = board

    @staticmethod
    def generate_board() -> list[list]:
        """Generates a sudoku board

        Returns:
            list[list]: Sudoku board generated
        """
        base = 3
        side = base*base

        # pattern for a baseline valid solution
        def pattern(r,c): return (base*(r%base)+r//base+c)%side

        # randomize rows, columns and numbers (of valid base pattern)
        from random import sample
        def shuffle(s): return sample(s,len(s)) 
        rBase = range(base) 
        rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1,base*base+1))

        # produce board using randomized baseline pattern
        board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

        squares = side*side
        empties = squares * 3//4
        for p in sample(range(squares),empties):
            board[p//side][p%side] = 0
        return board

    def is_valid(self, num:int, pos:tuple) -> bool:
        """Returns if a number is valid to be placed in the (pos)ition
        in terms of Sudoku rules.

        Args:
            num (int): Candidate number
            pos (tuple): Position (2D) in board

        Returns:
            bool: True if is valid under Sudoku rules
        """
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False
        
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 +3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False
        return True

    def find_empty(self)-> tuple:
        """Finds the next empty (zero) position in the board.

        Returns:
            tuple: Position of the next zero in the board. (-1, -1)
            if there's no exists.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return(i,j)
        return (-1, -1)

    def solve(self) -> bool:
        """Recursive method to solve a Sudoku puzzle with
        the Backtracking algorithm.

        Returns:
            bool: True if the board was solved. False if is
            not posible.
        """
        find = self.find_empty()
        if find == (-1, -1):
            return True
        row, col = find

        for i in range(1,10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True
                self.board[row][col] = 0
        return False 
        
    def __str__(self) -> str:
        """Str representation of the board. Intended for the print()
        python function

        Returns:
            str: String representation of the Sudoku board.
        """
        print_str = ""
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print_str += "-----------------------\n"
            
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print_str += " | "

                print_str += str(self.board[i][j])
                print_str += "\n" if j == len(self.board[0]) -1 else " "
        return print_str

"""
Test board.
board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
        ]
"""