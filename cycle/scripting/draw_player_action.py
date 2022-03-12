

from scripting.action import Action


class DrawPlayerAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawPlayerAction is to draw all the players.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawPlayerAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw player action.

        Args:
            cast (Cast): The cast of Players in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_player("scores")
        snake1 = cast.get_first_player("snakes1")
        snake2 = cast.get_first_player("snakes2")
        segments1 = snake1.get_segments()
        segments2 = snake2.get_segments()
        messages = cast.get_players("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_players(segments1)
        self._video_service.draw_players(segments2)
        self._video_service.draw_player(score)
        self._video_service.draw_players(messages, True)
        self._video_service.flush_buffer()