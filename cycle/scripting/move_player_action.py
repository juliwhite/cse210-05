
from scripting.action import Action


class MovePlayerAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MovePlayerAction is to move all the players that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move players action.

        Args:
            cast (Cast): The cast of Players in the game.
            script (Script): The script of Actions in the game.
        """

        players = cast.get_all_players()
        for player in players:
            player.move_next()
       