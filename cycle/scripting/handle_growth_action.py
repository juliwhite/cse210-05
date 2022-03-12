from scripting.action import Action

class HandleGrowthAction(Action):
    """
    An update action that handles growth of the cycle actors.
    
    The responsibility of HandleGrowthAction is to handle the growth of the tail of each cycle
    at regular intervals when the game is going.
    """

    
    def __init__(self):
        """Constructs a new HandleGrowthAction."""
        self.game_timer = 0

    def execute(self, cast, script):
        """Executes the handle growth action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self.game_timer += 1

        game_over = cast.get_first_actor("messages")

        
        # The growth of the cycles is determined by this value. 1 = every frame, 2 = every other frame, 15 = every second, 30 = every other second, etc.
        #                    V
        if self.game_timer % 5 == 0 and game_over == None:
            cycles = cast.get_actors("cycles")

            cycle1 = cycles[0]
            cycle2 = cycles[1]

            cycle1.grow_tail(1)
            cycle2.grow_tail(1)

