

import constants
from scripting.action import Action
from shared.point import Point


class ControlPlayerAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlPlayerAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlPlayersAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control players action.

        Args:
            cast (Cast): The cast of Players in the game.
            script (Script): The script of Actions in the game.
        """

        # left
        if  self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            snake1 = cast.get_first_player("snakes1")
            snake1.turn_head(self._direction)
            
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            snake1 = cast.get_first_player("snakes1")
            snake1.turn_head(self._direction)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            snake1 = cast.get_first_player("snakes1")
            snake1.turn_head(self._direction)
            
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            snake1 = cast.get_first_player("snakes1")
            snake1.turn_head(self._direction)

        
    
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            snake2 = cast.get_first_player("snakes2")
            snake2.turn_head(self._direction)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
            snake2 = cast.get_first_player("snakes2")
            snake2.turn_head(self._direction)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
            snake2 = cast.get_first_player("snakes2")
            snake2.turn_head(self._direction)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)
            snake2 = cast.get_first_player("snakes2")
            snake2.turn_head(self._direction)
        
    