import random
import numpy as np
import copy


class Game2048:
    """
    Game '2048'
    """
    def __init__(self, board_size=4):
        self.board_size = board_size
        self.init_number = [2, 4]

        self.game_board = [[0, 0, 0 ,0] for _ in range(board_size)]
        self.init_row = random.sample(range(board_size), 2)
        self.init_col = random.sample(range(board_size), 2)
        for i in range(2):
            self.game_board[self.init_row[i]][self.init_col[i]] = (
                self.init_number[random.randint(0, 1)]
            )

        self.max_number = 4
        self.moving = True

    def move_action(self, board=[[]], action=0, update=False):
        """
        Up: action=0,
        Down: action=1,
        Right: action=2,
        Left: action=3,
        """
        board = copy.deepcopy(self.game_board)
        
        if action == 0:
            board = self.move_up(board)
        elif action == 1:
            board = self.move_down(board)
        elif action == 2:
            board = self.move_right(board)
        elif action == 3:
            board = self.move_left(board)
        else:
            print(f'Action should be chose from {0, 1, 2, 3}')
            return
        
        # judge win or loss
        if self.max_number >= 2048:
            self.success()
            self.moving = False

        # self.moveable = True
        if not self.random_add(board):
            self.moving = False
        else:
            board = self.random_add(board)
            self.game_board = board

    def move_up(self, board=[[]]):
        return self.move(board)

    def move_down(self, board=[[]]):
        board = np.flip(np.array(board), 0)
        board = self.move(board)
        return np.flip(board, 0).tolist()
    
    def move_right(self, board=[[]]):
        board = np.rot90(np.array(board))
        board = self.move(board)
        return np.rot90(board, -1).tolist()
    
    def move_left(self, board=[[]]):
        board = np.rot90(np.array(board), -1)
        board = self.move(board)
        return np.rot90(board).tolist()

    def random_add(self, board=[[]]):
        """
        Add random 2 or 4 after move
        """
        n = self.board_size
        empty_cells = []
        for i in range(n):
            for j in range(n):
                if not board[i][j]:
                    empty_cells.append([i, j])

        # check board status, win or lose
        if not empty_cells:
            if self.end_game(board):
                if self.max_number >= 2048:
                    self.success()
                    return True
                else:
                    self.fail()
                    self.moving = False
                    return False
            else:
                return board

        chose = random.randint(0, len(empty_cells)-1)
        chose = empty_cells[chose]
        add_ind = random.randint(0, 10)
        if add_ind:
            board[chose[0]][chose[1]] = self.init_number[0]
        else:
            board[chose[0]][chose[1]] = self.init_number[1]
        return board

    def move(self, board=[[]]):
        """
        Use 'move up' as base case, for other cases, just flip or rotate board
        """
        new_B = self.empty_board()
        merge_flags = self.merge_flag()
        # record row depth
        flag = [0, 0, 0, 0]
        for row in range(self.board_size):
            for col in range(self.board_size):
                cur_cell = board[row][col]
                if cur_cell:
                    # merge
                    if self.check_ind(flag[col]-1) and new_B[flag[col]-1][col] == cur_cell:
                        # for each cell, it can only be merged one time during each move
                        if not merge_flags[flag[col]-1][col]:
                            new_B[flag[col]-1][col] *= 2
                            # update max number
                            self.max_number = max(
                                self.max_number,
                                new_B[flag[col]-1][col]
                            )
                            merge_flags[flag[col]-1][col] = True
                        else:
                            new_B[flag[col]][col] = cur_cell
                            flag[col] += 1
                    else:
                        new_B[flag[col]][col] = cur_cell
                        # record number of empty row
                        flag[col] += 1
        return new_B
    
    def empty_board(self,):
        return [[0, 0, 0 ,0] for _ in range(self.board_size)]
    
    def merge_flag(self,):
        return [[False, False, False ,False] for _ in range(self.board_size)]
    
    def check_ind(self, i):
        if i >=0 and i < self.board_size:
            return True
        return False

    def success(self):
        print(f'\nYou have won the game with max number {self.max_number}')
    
    def fail(self):
        print(f'\nYou have loss the game with max number {self.max_number}')

    def end_game(self, board=[[]]):
        """
        Check if the game is end when no empty cells
        """
        n = self.board_size
        res = True
        for i in range(n):
            for j in range(n-1):
                if board[i][j] == board[i][j+1]:
                    res = False
        for i in range(n-1):
            for j in range(n):
                if board[i][j] == board[i+1][j]:
                    res = False
        return res

    def check_move(self, test_board=[[]], action=0):
        board = copy.deepcopy(test_board)
        if action == 0:
            board = self.move_up(board)
        elif action == 1:
            board = self.move_down(board)
        elif action == 2:
            board = self.move_right(board)
        elif action == 3:
            board = self.move_left(board)
        # count empty number
        res = 0
        n = self.board_size
        for i in range(n):
            for j in range(n):
                if not board[i][j]:
                    res += 1
        return (board != test_board), res


def solve_2048():
    """
    1. find the best corner (max init number)
    2. move up
    3. move left or right
    4. move down
    """
    game = Game2048()
    times = 1
    action = 0
    while game.moving:
        print(f'\rYou have tried: {times} times. Max: {game.max_number}, {action} ', end='')
        times += 1
        
        left, left_e = game.check_move(game.game_board, action=3)
        right, right_e = game.check_move(game.game_board, action=2)
        down, down_e = game.check_move(game.game_board, action=1)
        if left and right:
            if left_e > right_e:
                action = 3
            else:
                action = 2
        elif left:
            action = 3
        elif right:
            action = 2
        elif down:
            action = 1
        else:
            action = 0
        game.move_action(game.game_board, action=action)
        if action == 0:
            game.move_action(game.game_board, action=1)

# For solving 2048, human can move 4 different direction each time and compute will randomly generate a number
# so, I need to find a method to decide which move will be the best move. 
# Currently, the solution is nothing but fail.
solve_2048()
