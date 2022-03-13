

import constants
from casting.actor import Actor
from scripting.action import Action
from shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a cycle collides
    with another cycle or with its segments, or the game is over.
    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._red_wins = "--"

    def execute(self, cast, script):
        """Executes the handle collisions action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if a cycle collides with one of it or it's opponent's segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        cycles = cast.get_actors("cycles")

        cycle1 = cycles[0]
        cycle2 = cycles[1]

        head1 = cycle1.get_segments()[0]
        segment1 = cycle1.get_segments()[1:]

        head2 = cycle2.get_segments()[0]
        segment2 = cycle2.get_segments()[1:]

        for section1 in segment1: 
            if head1.get_position().equals(section1.get_position()): 
                self._is_game_over = True
                self._red_wins = False
            if head2.get_position().equals(section1.get_position()): 
                self._is_game_over = True
                self._red_wins = True

        for section2 in segment2:
            if head1.get_position().equals(section2.get_position()): 
                self._is_game_over = True
                self._red_wins = False
            if head2.get_position().equals(section2.get_position()): 
                self._is_game_over = True
                self._red_wins = True
        
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the losing cycle white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over == True:
            
            cycles = cast.get_actors("cycles")

            cycle1 = cycles[0]
            segments1 = cycle1.get_segments()
            cycle2 = cycles[1]
            segments2 = cycle2.get_segments()
            

            if self._red_wins == True:
                player_color = "Red"
                cycle = cycles[1]
                
            else:
                player_color = "Green"
                cycle = cycles[0]

            
            #segments = cycle.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"{player_color} wins! Game over.")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)

            for segment in segments2:
                segment.set_color(constants.WHITE)