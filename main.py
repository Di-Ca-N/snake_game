from game import SnakeGame
from inputs import KeyboardListener
from game_input_dispatcher import GameInputDispatcher
from plotter import GamePlotter

import time

game = SnakeGame()
keyboard = KeyboardListener()
plotter = GamePlotter(game)

input_dispatcher = GameInputDispatcher(game)

keyboard.subscribe(input_dispatcher.move_snake)
keyboard.subscribe(input_dispatcher.new_game)

game.new_game()

while True:
    time.sleep(.5/game.speed)
    game.move_snake()

    if game.alive:
        plotter.plot()
    else:
        plotter.game_over()
