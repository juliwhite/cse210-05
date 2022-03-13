from scripting.action import Action

class MovePlayersAction(Action): #moveplayeraction
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

        actors = cast.get_all_actors()
        for player in actors:
            player.move_next()
       