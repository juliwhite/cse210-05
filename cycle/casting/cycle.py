from casting.actor import Actor
from shared.point import Point
import constants

class Cycle(Actor):
    """
    A bike with a light trail behind it
    
    The responsibility of Cycle is to move itself.
    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        """Constructs a new Cycle actor."""
        super().__init__()
        self._segments = []
        # self._prepare_body()
        self._cycle_color = constants.YELLOW

    def get_segments(self):
        """Returns a list of the segments in the cycle."""
        return self._segments

    def move_next(self):
        """Moves every segment in the cycle"""
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Returns the first segment of the cycle"""
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """Grows the tail of the cycle by one"""
        for _ in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._cycle_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """Turns the the cycle by changing the velocity of the head."""
        self._segments[0].set_velocity(velocity)
    
    def prepare_body(self, color):
        """Prepares the body of the cycle"""

        self._cycle_color = color
        if color == constants.RED:
            x = int(constants.MAX_X / 2 - 10 * constants.CELL_SIZE)
            y = int(constants.MAX_Y / 2)

        elif color == constants.GREEN:
            x = int(constants.MAX_X / 2 + 10 * constants.CELL_SIZE)
            y = int(constants.MAX_Y / 2)

        else:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
        

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, -1 * constants.CELL_SIZE)
            text = "@" if i == 0 else "#"

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)