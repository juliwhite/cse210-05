

import constants
from casting.player import Player
from scripting.action import Action
from shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the players.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the other player, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Players in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_snake_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_snake_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Players in the game.
        """
        #score = cast.get_first_player("scores")
        snake1 = cast.get_first_player("snakes1")
        snake2 = cast.get_first_player("snakes2")
        head1 = snake1.get_head()
        head2 = snake2.get_head()
        segments1 = snake1.get_segments()
        segments2 = snake2.get_segments()

        for segment in segments2:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for segment in segments1:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
            #points = food.get_points()
            #snake1.grow_tail(points)
            #score.add_points(points)
            
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake1 = cast.get_first_player("snakes1")
        head1 = snake1.get_segments()[0]
        segments1 = snake1.get_segments()[1:]
        
        for segment in segments1:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True

        snake2 = cast.get_first_player("snakes2")
        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]
        
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snakes white if the game is over.
        
        Args:
            cast (Cast): The cast of Players in the game.
        """
        if self._is_game_over:
            snake1 = cast.get_first_player("snakes1")
            segments1 = snake1.get_segments()

            snake2 = cast.get_first_player("snakes2")
            segments2 = snake2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Player()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_player("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)

            for segment in segments2:
                segment.set_color(constants.WHITE)
           
