#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Helle Thitouane, François Corantin'
__date_creation__ = '14/11/2019'
__last_revision__ = '27/11/2019'
__doc__ = """
:mod:`parentheses_checker` module
:author: {:s}
:creation date: {:s}
:last revision: {:s}


""".format(__author__, __date_creation__, __last_revision__)

import random

class Grid():
    """
    Grid is defined by its dimensions, the position of the finalcase , the positions of
    each player and the number of walls
    it contains.
    Finalcase must be in range of the grid dimensions.
    The grid can't contain more walls than the cases inside.
    
    """
    def __init__(self, dimx, dimy, finalcase, numwalls, players={'d': (2,9)}):
        """
        Create a grid with given dimensions, a final case and walls.
        
        :param dimx: the max x pos
        :type dimx: int
        :param dimy: the max y pos
        :type dimy: int
        :param finalcase: the positions of the finalcase
        :type finalcase: tuple
        :param numwalls: the number of walls in the grid (excluding the grid's borders)
        :type numwalls: int
        :param players: the players and their position
        :type players: dict
        """
        self.__grid = [[0 for x in range(2*dimx+1)] for y in range(2*dimy+1)]
        fx, fy = 2*finalcase[0]+1, 2*finalcase[1]+1
        self.__grid[fy][fx] = "O"
        
        for x in range(2*dimy+1):
            for y in range(2*dimx+1):
                if x in [0,2*dimx] or y in [0,2*dimy]:
                    self.__grid[y][x] = 'X'
        
        __walls = set()
        while len(__walls) < numwalls:
            x = random.randint(0,dimx-1)
            y = random.randint(0,dimy-1)
            pos = random.choice(['E','S'])
            if (x,y) != finalcase and (x,y) not in list(players.values()):
                __walls.add((2*x,2*y,pos))
        for i in __walls:
            if i[2] == 'E':
                self.__grid[i[1]][i[0]] = '+'
                self.__grid[i[1]+1][i[0]] = 'X'
            if i[2] == 'S':
                self.__grid[i[1]][i[0]] = '+'
                self.__grid[i[1]][i[0]+1] = 'X'
        
        for player in players:
            px, py = 2*players[player][0]+1, 2*players[player][1]+1
            self.__grid[py][px] = str(player)
        
        self.__finalcase = finalcase
        self.__players = players

#Réaliser sur le fichier decode.py
#     def from_file(file):
#         """
#         Load a game from a data file.
#         
#         :param file: a file
#         :type file: a stream opened in read mode
#         :UC: None
#         """
#         pass
    
    def __str__(self):
        """
        :return: an external representation of Grid object self
            (useful to print the selected grid for example)
        :rtype: str
        :UC: None
        """
        __copy = self.__grid.copy()
        for ligne in range(len(__copy)):
            for colonne in range(len(__copy[ligne])):
                if __copy[ligne][colonne] == 'X':
                    if ligne % 2 == 0 and colonne % 2 == 0:
                        __copy[ligne][colonne] = '+'
                    elif ligne % 2 == 0 and colonne % 2 == 1:
                        __copy[ligne][colonne] = '-'
                    else:
                        __copy[ligne][colonne] = '|'
                elif __copy[ligne][colonne] == 0:
                    __copy[ligne][colonne] = ' '
        string = ''
        for i in range(len(__copy)):
            string += "".join(__copy[i]) + "\n"
        return string
    
    def __repr__(self):
        """ 
        :return: an external representation of Grid object self
        :rtype: str
        :UC: None
        """
        return self.__str__()
    
    def move(self, player, direction):
        """
        Move a player towards a chosen direction
        
        :param player: name of the player who will move
        :type player: str
        :param direction: a direction
        :type direction: str
        :UC: pos must be in ['N','W','S','E']
        """
        grid = self.__grid
        ppos = self.__players[player]
        nextpos = {'N': (ppos[0],ppos[1]-1), 'W': (ppos[0]-1,ppos[1]), 'S': (ppos[0],ppos[1]+1), 'E': (ppos[0]+1,ppos[1])}
        while self.__grid[nextpos[direction][0]][nextpos[direction][1]] not in ['+','O','-','|']:
            print(self.__grid[nextpos[direction][0]][nextpos[direction][1]])
            print(nextpos)
            if direction == 'N':
                ppos = (ppos[0], ppos[1]-1)
                nextpos[direction] = (ppos[0], ppos[1]-1)
            elif direction == 'W':
                ppos = (ppos[0]-1, ppos[1])
                nextpos[direction] = (ppos[0]-1, ppos[1])
            elif direction == 'S':
                ppos = (ppos[0], ppos[1]+1)
                nextpos[direction] = (ppos[0], ppos[1]+1)
            else:
                ppos = (ppos[0]+1, ppos[1])
                nextpos[direction] = (ppos[0]+1, ppos[1])
        self.__players[player] = ppos[0]//2,ppos[1]//2
        
    def state(self):
        """
        Give the state of the game
        
        :return: - "Finished" if a player reaches the final case
                 - "Unfinished" if not
        :rtype: str
        :UC: None
        """
        if any(self.__players[name] == self.grid.__finalcase for name in self.__players):
            return "Finished"
        else:
            return "Unfinished"



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    
