from django.db import models

import random


#Levels are represeneted by a tuple (TABLE SIZE, NUMBER OF MINES)
BEGGINNER = (9, 10)
INTERMEDIATE = (16, 40)
ADVANCED = (24, 99)

LEVELS = (
    ('B', 'BEGGINNER'),
    ('I', 'INTERMEDIATE'),
    ('A', 'ADVANCED')
)

LEVELS_DICT = {
    'B': BEGGINNER,
    'I': INTERMEDIATE,
    'A': ADVANCED,
}


def is_valid_cell(self, table_size, x_cor, y_cor):
    """
    Returns True if row number and column number is in range
    """
    return x_cor > 0 and x_cor <= table_size and \
           y_cor > 0 and x_cor <= table_size


class Board(models.Model):
    """ 
    A new board is created for each game.
    When a board object is created, the game starts.
    """
    level = models.CharField(max_length=1 ,choices=LEVELS)
    finished = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(Board, self).__init__(*args, **kwargs)
        self.save()
        self.place_mines()

    def place_mines(self):
        """
        Place mines and then create the necesary cells to start
        the game
        """
        table_size = LEVELS_DICT[self.level][0]
        mines = LEVELS_DICT[self.level][1]
        number_of_cells = table_size ** 2
        list_of_mines = []

        while len(list_of_mines) < mines:
            x_cordenade = random.randint(1, table_size)
            y_cordenade = random.randint(1, table_size)

            if (x_cordenade, y_cordenade) not in list_of_mines:
                list_of_mines.append((x_cordenade, y_cordenade))
        
        # Here we create the mined cells
        for i in list_of_mines:
            c = Cell(x_cordenade=i[0], 
                     y_cordenade=i[1],
                     board=self,
                     has_mine=True)
            c.save()
        print("mined cells")
        print(list_of_mines)

        # Here we crete not mined cell
        not_mined_cells = []
        for x in range(1, table_size+1):
            for y in range(1, table_size+1):
                cordenade = (x, y)
                if cordenade not in list_of_mines:
                    c = Cell(x_cordenade=i[0], 
                             y_cordenade=i[1],
                             board=self,
                             has_mine=False)
                    c.save()
                    not_mined_cells.append(cordenade)
        print("not mined cells")
        print(not_mined_cells)


    def get_mines_cordenades(self):
        """
        Return a list of tuples with the mines cordenades
        """
        pass


class Cell(models.Model):
    """
    Model to represent a zone where a user can click or mark as mined.
    """
    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    has_mine = models.BooleanField(default=False)
    marked_as_mined = models.BooleanField(default=False)
    x_cordenade = models.IntegerField()
    y_cordenade = models.IntegerField()
    value = models.IntegerField(blank=True, null=True)
    # value field is the number of mines sourronding this cell

    def number_of_adjacent_mines(self):
        """
        Calculate a value of a cell

        Cell-->Current Cell (x_cor, y_cor)
        N -->  North        (x_cor-1, y_cor)
        S -->  South        (x_cor+1, y_cor)
        E -->  East         (x_cor, y_cor+1)
        W -->  West         (x_cor, y_cor-1)
        N.E--> North-East   (x_cor-1, y_cor+1)
        N.W--> North-West   (x_cor-1, y_cor-1)
        S.E--> South-East   (x_cor+1, y_cor+1)
        S.W--> South-West   (x_cor+1, y_cor-1)
        """
        mines_next = 0
        # --- North ---
        if Cell.objects.filter(x_cordenade=self.x_cordenade - 1, 
                               y_cordenade=self.y_cordenade,
                               has_mine=True, board=self.board).exists():
            mines_next += 1
        # --- South ---
        if Cell.objects.filter(x_cordenade=self.x_cordenade + 1, 
                               y_cordenade=self.y_cordenade,
                               has_mine=True, board=self.board).exists():
            mines_next += 1
        # --- East ---
        if Cell.objects.filter(x_cordenade=self.x_cordenade, 
                               y_cordenade=self.y_cordenade + 1,
                               has_mine=True, board=self.board).exists():
            mines_next += 1
        # --- West ---
        if Cell.objects.filter(x_cordenade=self.x_cordenade, 
                               y_cordenade=self.y_cordenade - 1,
                               has_mine=True, board=self.board).exists():
            mines_next += 1
        # --- North-East ---
        if Cell.objects.filter(x_cordenade=self.x_cordenade - 1, 
                               y_cordenade=self.y_cordenade + 1,
                               has_mine=True, board=self.board).exists():
            mines_next += 1
        # --- North-West ---
        if Cell.objects.filter(x_cordenade=self.x_cordenade - 1, 
                               y_cordenade=self.y_cordenade - 1,
                               has_mine=True, board=self.board).exists():
            mines_next += 1
        # --- South-East ---
        if Cell.objects.filter(x_cordenade=self.x_cordenade + 1, 
                               y_cordenade=self.y_cordenade + 1,
                               has_mine=True, board=self.board).exists():
            mines_next += 1
        # --- South-West ---
        if Cell.objects.filter(x_cordenade=self.x_cordenade + 1, 
                               y_cordenade=self.y_cordenade - 1,
                               has_mine=True, board=self.board).exists():
            mines_next += 1
        
        return mines_next

    def click_on_cell(self):
        pass

