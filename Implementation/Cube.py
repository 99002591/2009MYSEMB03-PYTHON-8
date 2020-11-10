import pygame

class Cube:
    rows = 9
    cols = 9
    
    def __init__(self, value, row, col, width, height):
        """

            :param : self
                    value
                    row
                    col
                    width
                    height
            :return : None
            :def :  Instance of the class
        """
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        """

        :param :  self
        :return : None
        :def : Draws the grid lines over a already 
               rendered window
        """
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
        """

        :param :  self
                  window
                  g = True
        :return : None
        :def :   Draws the bounding rectangle on an
                 actively updating cells
        """
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(win, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2),
                        y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(win, (0, 255, 100), (x, y, gap, gap), 6)
        else:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 6)

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