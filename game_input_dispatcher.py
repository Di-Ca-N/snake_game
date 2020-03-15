from pynput.keyboard import Key, KeyCode


class GameInputDispatcher:
    def __init__(self, game):
        self.game = game
        self.commands = {
            Key.up: self.game.DIRECTIONS.UP,
            Key.left: self.game.DIRECTIONS.LEFT,
            Key.down: self.game.DIRECTIONS.DOWN,
            Key.right: self.game.DIRECTIONS.RIGHT,
        }

    def move_snake(self, key):
        self.game.snake_direction = self.commands.get(
            key,
            self.game.snake_direction
        )

    def new_game(self, key):
        if key == KeyCode(char='n') and not self.game.alive:
            self.game.new_game()
