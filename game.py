import random
class RabbitGame:
    def __init__(self):
        self.width = int(input("Enter grid width: "))
        self.height = int(input("Enter grid height: "))
        self.board = [['.' for _ in range(self.width)] for _ in range(self.height)]
        self.rabbit_position = [0, 0]  # Initial position of the rabbit
        self.carrots = self.generate_positions(int(input("Enter number of carrots: ")), exclude=[self.rabbit_position])
        self.holes = self.generate_positions(int(input("Enter number of holes: ")), exclude=self.carrots + [self.rabbit_position])
        self.init_board()

    def generate_positions(self, count, exclude=[]):
        positions = []
        while len(positions) < count:
            pos = [random.randint(0, self.height - 1), random.randint(0, self.width - 1)]
            if pos not in positions and pos not in exclude:
                positions.append(pos)
        return positions

    def init_board(self):
        for carrot in self.carrots:
            self.board[carrot[0]][carrot[1]] = 'c'
        for hole in self.holes:
            self.board[hole[0]][hole[1]] = 'O'
        self.update_rabbit_position(0, 0)

    def update_rabbit_position(self, x, y):
        if self.board[x][y] == 'O':
            print("Oops! Fell into a hole. Game over.")
            exit()
        else:
            # Check if the current position contains a carrot before moving
            if self.rabbit_position in self.carrots:
                self.board[self.rabbit_position[0]][self.rabbit_position[1]] = 'c'
            else:
                self.board[self.rabbit_position[0]][self.rabbit_position[1]] = '.'
            self.rabbit_position = [x, y]
            self.board[x][y] = 'r'


    def move_rabbit(self, direction):
        x, y = self.rabbit_position
        if direction == 'w' and x > 0:
            self.update_rabbit_position(x-1, y)
        elif direction == 's' and x < self.height - 1:
            self.update_rabbit_position(x+1, y)
        elif direction == 'a' and y > 0:
            self.update_rabbit_position(x, y-1)
        elif direction == 'd' and y < self.width - 1:
            self.update_rabbit_position(x, y+1)

    def jump(self, direction):
        x, y = self.rabbit_position
        if direction == 's' and x < self.height - 2:
            # Jump down
            self.update_rabbit_position(x + 2, y)
        elif direction == 'w' and x > 1:
            # Jump up
            self.update_rabbit_position(x - 2, y)
        elif direction == 'd' and y < self.width - 2:
            # Jump right
            self.update_rabbit_position(x, y + 2)
        else:
            print("Cannot jump in that direction!")


    def pick_carrot(self):
        if self.rabbit_position in self.carrots:
            print("Carrot picked!")
            self.carrots.remove(self.rabbit_position)
            self.board[self.rabbit_position[0]][self.rabbit_position[1]] = 'r'
        else:
            print("No carrot here!")

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

def main():
    game = RabbitGame()
    game.print_board()

    while True:
        move = input("Move rabbit (w/a/s/d), jump (j + direction), exit(x), pick carrot (p): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            game.move_rabbit(move)
        elif move.startswith('j'):
            _, direction = move.split()
            game.jump(direction)
        elif move == 'p':
            game.pick_carrot()
        elif move == 'x':
            exit()
        else:
            print("Invalid command!")
            continue
        game.print_board()

if __name__ == "__main__":
    main()
