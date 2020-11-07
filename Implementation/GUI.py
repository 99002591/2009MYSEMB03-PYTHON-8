# GUI.py
import pygame
pygame.font.init()


class Grid:
    board = [
        [2, 0, 4, 0, 0, 0, 0, 6, 7],
        [3, 0, 0, 4, 7, 0, 0, 0, 5],
        [1, 5, 0, 8, 2, 0, 0, 0, 3],
        [0, 0, 6, 0, 0, 0, 0, 3, 1],
        [8, 0, 2, 1, 0, 5, 6, 0, 4],
        [4, 1, 0, 0, 0, 0, 9, 0, 0],
        [7, 0, 0, 0, 8, 0, 0, 4, 6],
        [6, 0, 0, 0, 1, 2, 0, 0, 0],
        [9, 3, 0, 0, 0, 0, 7, 1, 0]
    ]

    def __init__(self, rows, cols, width, height, win):
        """

        :param: self
                rows: Number of rows
                cols: Number of coloumns
                width: Width of each face
                height: Height of each face
                win: Object of the main display window
        :return : none
        :def : Intance of the class
        """
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height)
                       for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.update_model()
        self.win = win

    def update_model(self):
        """

        :param :   self
        :return :  None
        :def : Updates the model rendered on screen after every operation
        """
        self.model = [[self.cubes[i][j].value for j in range(
            self.cols)] for i in range(self.rows)]

    def draw(self):
        """

        :param :  self
        :return : None
        :def : Draws the cross-grid on the display window
            and draws cubes and fills them
        """

        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (40, 40, 40), (0, i*gap),
                             (self.width, i*gap), thick)
            pygame.draw.line(self.win, (40, 40, 40), (i * gap, 0),
                             (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)

    def solve_gui(self):
        """
        @param : self
        @return : boolean
        @def :  calls the find_empty() function
                calls the valid() function
                does this for all the cells in the grid
                calls update_model() to visualise every step
                Updates the final 2D-list of the puzzle and
                returns True only when the puzzle is solved.
        """
        self.update_model()
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.model, i, (row, col)):
                self.model[row][col] = i
                self.cubes[row][col].set(i)
                self.cubes[row][col].draw_change(self.win, True)
                self.update_model()
                pygame.display.update()
                pygame.time.delay(1)

                if self.solve_gui():
                    return True

                self.model[row][col] = 0
                self.cubes[row][col].set(0)
                self.update_model()
                self.cubes[row][col].draw_change(self.win, False)
                pygame.display.update()
                pygame.time.delay(100)

        return False


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):

        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):

        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2),
                            y + (gap/2 - text.get_height()/2)))

    def draw_change(self, win, g=True):

        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(win, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2),
                        y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(win, (0, 170, 100), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        """

        :param :  self
                  val
        :return : None
        :def :  Value setter
        """
        self.value = val

    def set_temp(self, val):
        """

        :param :  self
                  val
        :return : None
        :def :  Temporary value setter
        """
        self.temp = val


def find_empty(bo):
    """

    :param :  bo (Unsolved board, 2D List)
    :return : tuple of index
    :def :    finds empty cells in the unsolved puzzle
              represented by 0s, and return a tuple 
              of their indexes
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def valid(bo, num, pos):
    """

    :param  : bo (Unsolved board, 2D List)
              num (The number that is being validated)
              pos (The index of the cell being checked)
    :return : boolean
              True > if the number is valid
              False > if the number is invalid
    :def    : This has 3 subsequent main for loops that 
              check for the validity of a number at a cell
              in the order ROW > COL > BOX
    """

    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def redraw_window(win, board):
    """

    :param  : window
              board (Object of the class Grid)
    :return : None
    :def    : Callback function for draw() 
    """
    win.fill((255, 255, 255))
    # Draw grid and board
    board.draw()


def main():
    win = pygame.display.set_mode((540, 540))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540, win)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                board.solve_gui()

            redraw_window(win, board)
            pygame.display.update()


main()
pygame.quit()
