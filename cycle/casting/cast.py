
class Cast:
    '''
    A collection of players.
    The responsability of a cast is to keep track of a collection of players.
    It has methods for adding, removing ad getting them by a group name.
    '''
    def __init__(self) -> None:
        '''
        Construct a new player. 
        '''
        self._players = {}

    def add_player(self, group, player):
        '''
        Add a player to the given group. 
        '''
        if not group in self._players.keys():
            self._players[group] = []

        if not player in self._players[group]:
            self._players[group].append(player)

    def get_actors(self, group):
        '''
        Gets the players in the given group.
        '''
        results = []
        if group in self._players.keys():
            results = self._players[group].copy()
        return results

    def get_all_actors(self):
        '''
        Gets all the players in the cast.
        '''
        results = []
        for group in self._players:
            results.extend(self._players[group])
        return results

    def get_first_player(self, group):
        '''
        Gets the first player in the given group.
        '''
        result = None
        if group in self._players.keys():
            result = self._players[group][0]
        return result

    def remove_player(self, group, player):
        '''
        Removes a player from the given group. 
        '''
        if group in self._players:
            self._players[group].remove(player)