import os


class GamePlotter:
    def __init__(self, game):
        self.game = game

        self.horizontal_delimiter = chr(9472)
        self.vertical_delimiter = chr(9474)
        self.top_left_delimiter = chr(9484)
        self.top_right_delimiter = chr(9488)
        self.bottom_left_delimiter = chr(9492)
        self.bottom_right_delimiter = chr(9496)

        self.snake_body = chr(9633)
        self.snake_head = chr(9632)
        self.fruit = chr(9642)

        self.cls_command = 'cls' if os.name == 'nt' else 'clear'

    def plot(self):
        os.system(self.cls_command)

        plot_canvas = []
        heigth = self.game.BOARD_SIZE[0] + 2
        width = self.game.BOARD_SIZE[1] + 2

        for i in range(heigth):
            row = []
            for j in range(width):
                actual_game_position = (i - 1, j - 1)

                if i == 0 and j == 0:
                    row.append(self.top_left_delimiter)

                elif i == 0 and j == width - 1:
                    row.append(self.top_right_delimiter)

                elif i == heigth - 1 and j == 0:
                    row.append(self.bottom_left_delimiter)

                elif i == heigth - 1 and j == width - 1:
                    row.append(self.bottom_right_delimiter)

                elif i in (0, heigth - 1):
                    row.append(self.horizontal_delimiter)

                elif j in (0, width - 1):
                    row.append(self.vertical_delimiter)

                elif actual_game_position == self.game.fruit:
                    row.append(self.fruit)

                elif actual_game_position == self.game.snake[0]:
                    row.append(self.snake_head)

                elif actual_game_position in self.game.snake:
                    row.append(self.snake_body)

                else:
                    row.append(" ")

            plot_canvas.append(row)

        for row in plot_canvas:
            print("".join(row))

    def game_over(self):
        os.system(self.cls_command)
        print("GAME OVER")
        print(f"Your score was {self.game.score}")
        print("Press <n> to start a new game")
