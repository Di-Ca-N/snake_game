import random
import enum
from collections import deque


class SnakeGame:
    BOARD_SIZE = (20, 100)
    INITIAL_SNAKE_SIZE = 3
    INITIAL_SPEED = 5
    DIRECTIONS = enum.Enum('Directions', {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1),
    })

    def __init__(self):
        self.fruit = (None, None)
        self.speed = 5
        self.alive = True

        self.score = 0
        self.walls = ()

        self._snake_direction = self.DIRECTIONS.LEFT
        self.snake = deque()

    def new_game(self):
        self.alive = True
        self.init_snake()
        self.spawn_fruit()

    def spawn_fruit(self):
        row = random.randrange(0, self.BOARD_SIZE[0])
        col = random.randrange(0, self.BOARD_SIZE[1])

        while (row, col) in self.snake:
            row = random.randrange(0, self.BOARD_SIZE[0])
            col = random.randrange(0, self.BOARD_SIZE[1])

        self.fruit = (row, col)

    @property
    def snake_direction(self):
        return self._snake_direction

    @snake_direction.setter
    def snake_direction(self, new_direction):
        row_sum = self._snake_direction.value[0] + new_direction.value[0]
        col_sum = self._snake_direction.value[1] + new_direction.value[1]

        if (row_sum, col_sum) != (0, 0):
            self._snake_direction = new_direction

    def init_snake(self):
        self.snake.clear()

        self.snake.append((self.BOARD_SIZE[0] // 2, self.BOARD_SIZE[1] // 2))
        row_mod, col_mod = self.snake_direction.value

        while len(self.snake) < self.INITIAL_SNAKE_SIZE:
            tail_row, tail_col = self.snake[-1]
            self.snake.append(
                (tail_row - row_mod, tail_col - col_mod)
            )

    def move_snake(self):
        if not self.alive:
            return

        row_move, col_move = self.snake_direction.value
        old_row, old_col = self.snake[0]

        new_row = (old_row + row_move) % self.BOARD_SIZE[0]
        new_col = (old_col + col_move) % self.BOARD_SIZE[1]

        new_position = (new_row, new_col)

        self.snake.pop()

        if new_position == self.fruit:
            self.eat_fruit()

        elif new_position in self.snake:
            self.set_game_over()

        elif new_position in self.walls:
            self.set_game_over()

        self.snake.appendleft(new_position)

    def eat_fruit(self):
        self.snake.append(self.fruit)
        self.score += 1
        self.spawn_fruit()
        self.update_speed()

    def update_speed(self):
        self.speed = self.INITIAL_SPEED + (self.score / 5)

    def set_game_over(self):
        self.alive = False
