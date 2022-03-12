

import constants

from casting.cast import Cast
from casting.score import Score
from casting.snake_1 import Snake1
from casting.snake_2 import Snake2
from scripting.script import Script
from scripting.control_player_action import ControlPlayerAction
from scripting.move_player_action import MovePlayerAction
from scripting.handle_collisions_action import HandleCollisionsAction
from scripting.draw_player_action import DrawPlayerAction
from directing.game import Game
from services.keyboard_service import KeyboardService
from services.video_service import VideoService
from shared.color import Color
from shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_player("snakes1", Snake1())
    cast.add_player("snakes2", Snake2())
    cast.add_player("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlPlayerAction(keyboard_service))
    script.add_action("update", MovePlayerAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawPlayerAction(video_service))
    
    director = Game(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()