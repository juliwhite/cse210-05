from casting.cast import Cast
from casting.grow import Grow
from casting.score import Score
from casting.cycle import Cycle
from directing.director import Game
from scripting.script import Script
from scripting.control_player_action import ControlPlayersAction
from scripting.draw_player_action import DrawPlayersAction
from scripting.handle_collisions_action import HandleCollisionsAction
from scripting.handle_growth_action import HandleGrowthAction
from scripting.move_player_action import MovePlayersAction
from directing.director import Game
from services.keyboard_service import KeyboardService
from services.video_service import VideoService
from shared.color import Color
from shared.point import Point
import constants

def main():
    
    # create the cast
    cast = Cast()

    cycle_one = Cycle()
    cycle_two = Cycle()
    
    score_one = Score("One")
    score_two = Score("Two")
    
    cycle_one.prepare_body(constants.RED)
    cycle_two.prepare_body(constants.GREEN)

    cast.add_actor("cycles", cycle_one)
    cast.add_actor("cycles", cycle_two)
    
    score_one.prepare_score("One")
    score_two.prepare_score("Two")
    
    cast.add_actor("scores", score_one)
    cast.add_actor("scores", score_two)
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlPlayersAction(keyboard_service))
    script.add_action("update", MovePlayersAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", HandleGrowthAction())
    script.add_action("output", DrawPlayersAction(video_service))
    
    director = Game(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()