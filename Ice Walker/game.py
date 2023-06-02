import case

class Game():
    """
    
    """
    def __init__(self, grid, players={'default': (0,0)}):
        """
        Create a Game with given grid and players.
        :param grid: a grid
        :type grid: Grid object
        :param players: a dictionnary whose keys are player names and values are their
                        positions
        :type players: dict
        """
        self.__grid = grid
        self.__players = players
        
        def move(self, player, direction):
            """
            Move a player towards a chosen direction
            
            :param player: name of the player who will move
            :type player: str
            :param direction: a direction
            :type direction: str
            :UC: pos must be in ['N','W','S','E']
            """
            ppos = self.__players[player]
            nextpos = {'N': (ppos[0],ppos[1]-1), 'W': (ppos[0]-1,ppos[1]), 'S': (ppos[0],ppos[1]+1), 'E': (ppos[0]+1,ppos[1])}
            while self.__grid[nextpos[direction]] != 'X':
                if direction == 'N':
                    ppos = (ppos[0], ppos[1]-1)
                    nextpos[direction] = (ppos[0], ppos[0]-2)
                elif direction == 'W':
                    ppos = (ppos[0]-1, ppos[1])
                    nextpos[direction] = (ppos[0]-2, ppos[0])
                elif direction == 'S':
                    ppos = (ppos[0], ppos[1]+1)
                    nextpos[direction] = (ppos[0], ppos[0]+2)
                else:
                    ppos = (ppos[0]+1, ppos[1])
                    nextpos[direction] = (ppos[0]+2, ppos[0])
            self.__players[player] = ppos
        
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