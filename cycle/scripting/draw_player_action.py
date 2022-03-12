from scripting.action import Action


class DrawPlayersAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        scores = cast.get_actors("scores")
        # food = cast.get_first_actor("foods")
        cycles = cast.get_actors("cycles")

        score_one = scores[0]
        score_two = scores[1]
        
        red_cycle = cycles[0]
        blue_cycle = cycles[1]

        red_segments = red_cycle.get_segments()
        blue_segments = blue_cycle.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        # self._video_service.draw_actor(food)
        self._video_service.draw_actors(red_segments)
        self._video_service.draw_actors(blue_segments)
        self._video_service.draw_actor(score_one)
        self._video_service.draw_actor(score_two)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()