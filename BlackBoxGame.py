
# Author: Nathaniel Nguyen
# Date: 08/12/2020
# Description: Simulates the 1-2 player abstract board game - Black Box. Played on a two-dimensional grid, a player
# shoots 'rays' into a black box to deduce the locations of 'atoms' hidden inside where the behavior of the 'rays'
# gives clues to the location of atoms.

class BlackBoxGame():

    """Simulates the board game - Black Box."""

    def __init__(self, atom_list):      #14 Lines

        """Initializes board, player score, number of atoms placed, entry/exit locations, guesses, and ray behavior."""

        self._atoms = 0
        self._points = 25

        self._direction = None
        self._result = None
        self._currentpos = None

        self._guesses = []
        self._entryexitlocations = []

        self._board = [['_' for num in range(0, 10)] for num in range(0, 10)]
        for atom in range(0, len(atom_list)):
            for row in range(0, 10):
                for column in range(0, 10):
                    if atom_list[atom] == (row, column):
                        self._atoms += 1
                        self._board[row][column] = ('O')

    def shoot_ray(self, row_shot, column_shot):     #19 Lines

        """
        Simulates shooting a ray into the board given a row and column of a border square. Returns False if the chosen
        row and column designate a corner square or a non-border square. Otherwise, returns the location of an exit
        border square for a miss or returns true for a hit.
        """

        if (row_shot in range(1, 9) and column_shot in range(1, 9)) \
                or (row_shot, column_shot) in [(0, 0), (0, 9), (9, 0), (9, 9)]:
            return False

        if (row_shot, column_shot) not in self._entryexitlocations:
            self._points -= 1
            self._entryexitlocations.append((row_shot, column_shot))

        self.direction(row_shot, column_shot)
        self._currentpos = (row_shot, column_shot)
        self._result = True

        while (self._result != 'Hit') and (self._result != 'Other Side'):
            self.move(self._currentpos[0], self._currentpos[1])

        else:
            if self._result == 'Other Side' and self._currentpos not in self._entryexitlocations:
                self._points -= 1
                self._entryexitlocations.append(self._currentpos)

        if self._result == 'Other Side':
            return self._currentpos

        elif self._result == 'Hit':
            return

    def move(self, move_row_shot, move_column_shot):        #8 Lines

        """Calls on specific direction methods to 'shoot' the ray."""

        if self._direction == 'Right':
            self.move_Right(move_row_shot, move_column_shot)

        elif self._direction == 'Up':
            self.move_Up(move_row_shot, move_column_shot)

        elif self._direction == 'Left':
            self.move_Left(move_row_shot, move_column_shot)

        elif self._direction == 'Down':
            self.move_Down(move_row_shot, move_column_shot)

        return

    def move_Down(self, row_shot, column_shot):     #23 Lines

        """Moves the 'ray' down on the board. """

        if self._board[row_shot][column_shot] == 'O':
            self._result = 'Hit'
            self._currentpos = (row_shot, column_shot)

        elif row_shot == 9:
            self._result = 'Other Side'
            self._currentpos = (row_shot, column_shot)

        elif (self._board[row_shot + 1][column_shot + 1] == 'O' and self._board[row_shot + 1][column_shot - 1] == 'O') \
                or (row_shot == 0 and self._board[row_shot + 1][column_shot + 1] == 'O') \
                or (row_shot == 0 and self._board[row_shot + 1][column_shot - 1] == 'O'):
            self._result = 'Double Deflect'
            self._direction = 'Up'
            self._currentpos = (row_shot, column_shot)

        elif self._board[row_shot + 1][column_shot + 1] == 'O':
            self._result = 'Deflect Left'
            self._direction = 'Left'
            self._currentpos = (row_shot, column_shot)

        elif self._board[row_shot + 1][column_shot - 1] == 'O':
            self._result = 'Deflect Right'
            self._direction = 'Right'
            self._currentpos = (row_shot, column_shot)

        else:
            self.move_Down(row_shot + 1, column_shot)

        return

    def move_Left(self, row_shot, column_shot):     #23 Lines

        """Moves the 'ray' left on the board."""

        if self._board[row_shot][column_shot] == 'O':
            self._result = 'Hit'
            self._currentpos = (row_shot, column_shot)

        elif column_shot == 0:
            self._result = 'Other Side'
            self._currentpos = (row_shot, column_shot)

        elif (self._board[row_shot - 1][column_shot - 1] == 'O' and self._board[row_shot + 1][column_shot - 1] == 'O') \
                or (column_shot == 9 and self._board[row_shot - 1][column_shot - 1] == 'O') \
                or (column_shot == 9 and self._board[row_shot + 1][column_shot - 1] == 'O'):
            self._result = 'Double Deflect'
            self._direction = 'Right'
            self._currentpos = (row_shot, column_shot)

        elif self._board[row_shot - 1][column_shot - 1] == 'O':
            self._result = 'Deflect Down'
            self._direction = 'Down'
            self._currentpos = (row_shot, column_shot)

        elif self._board[row_shot + 1][column_shot - 1] == 'O':
            self._result = 'Deflect Up'
            self._direction = 'Up'
            self._currentpos = (row_shot, column_shot)

        else:
            self.move_Left(row_shot, column_shot - 1)

        return

    def move_Up(self, row_shot, column_shot):       #23 Lines

        """Moves the 'ray' up on the board."""

        if self._board[row_shot][column_shot] == 'O':
            self._result = 'Hit'
            self._currentpos = (row_shot, column_shot)

        elif row_shot == 0:
            self._result = 'Other Side'
            self._currentpos = (row_shot, column_shot)

        elif (self._board[row_shot - 1][column_shot - 1] == 'O' and self._board[row_shot - 1][column_shot + 1] == 'O') \
                or (row_shot == 9 and self._board[row_shot - 1][column_shot + 1] == 'O') \
                or (row_shot == 9 and self._board[row_shot - 1][column_shot - 1] == 'O'):
            self._result = 'Double Deflect'
            self._direction = 'Down'
            self._currentpos = (row_shot, column_shot)

        elif self._board[row_shot - 1][column_shot + 1] == 'O':
            self._result = 'Deflect Left'
            self._direction = 'Left'
            self._currentpos = (row_shot, column_shot)

        elif self._board[row_shot - 1][column_shot - 1] == 'O':
            self._result = 'Deflect Right'
            self._direction = 'Right'
            self._currentpos = (row_shot, column_shot)

        else:
            self.move_Up(row_shot - 1, column_shot)

        return

    def move_Right(self, row_shot, column_shot):        #23 Lines

        """Moves the 'ray' right on the board."""

        if self._board[row_shot][column_shot] == 'O':
            self._result = 'Hit'
            self._currentpos = (row_shot, column_shot)

        elif column_shot == 9:
            self._result = 'Other Side'
            self._currentpos = (row_shot, column_shot)

        elif (self._board[row_shot - 1][column_shot + 1] == 'O' and self._board[row_shot + 1][column_shot + 1] == 'O') \
                or (column_shot == 9 and self._board[row_shot - 1][column_shot + 1] == 'O') \
                or (column_shot == 9 and self._board[row_shot + 1][column_shot + 1] == 'O'):
            self._result = 'Double Deflect'
            self._direction = 'Left'
            self._currentpos = (row_shot, column_shot)

        elif self._board[row_shot - 1][column_shot + 1] == 'O':
            self._result = 'Deflect Down'
            self._direction = 'Down'
            self._currentpos = (row_shot, column_shot)

        elif self._board[row_shot + 1][column_shot + 1] == 'O':
            self._result = 'Deflect Up'
            self._direction = 'Up'
            self._currentpos = (row_shot, column_shot)

        else:
            self.move_Right(row_shot, column_shot + 1)

        return

    def direction(self, row_shot, column_shot):     #12 Lines

        """Determines direction to shoot the ray from user inputs."""

        if row_shot == 0:
            self._direction = 'Down'
            return

        elif row_shot == 9:
            self._direction = 'Up'
            return

        elif column_shot == 0:
            self._direction = 'Right'
            return

        elif column_shot == 9:
            self._direction = 'Left'
            return

    def guess_atom(self, row_guess, column_guess):      #10 Lines

        """Determines if a guess is correct or not and evaluates points accordingly."""

        if self._board[row_guess][column_guess] == 'O' and (row_guess, column_guess) not in self._guesses:
            self._atoms -= 1
            self._guesses.append((row_guess, column_guess))
            return True

        elif self._board[row_guess][column_guess] == 'O' and (row_guess, column_guess) in self._guesses:
            return

        elif (row_guess, column_guess) not in self._guesses:
            self._points -= 5
            self._guesses.append((row_guess, column_guess))
            return False

    def get_score(self):        #1 Line

        """Returns the current score."""

        return self._points

    def atoms_left(self):       #1 Line

        """Returns the number of atoms that haven't been guessed yet."""

        return self._atoms