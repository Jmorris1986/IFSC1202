class Sketch:
    def __init__(self, size):
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = 'U'  # U = up, D = down, L = left, R = right
        self.pen = 'U'  # U = pen up, D = pen down
        self.canvas = [[' ' for _ in range(size)] for _ in range(size)]

    def printsketch(self):
        print("Canvas:")
        for y in range(self.size - 1, -1, -1):
            print("|" + ''.join(self.canvas[y]) + "|")
        print("+" + "-" * self.size + "+")
        print(f"Position: ({self.xpos}, {self.ypos})")
        print(f"Direction: {self.direction}")
        print(f"Pen: {'Down' if self.pen == 'D' else 'Up'}")

    def penup(self):
        self.pen = 'U'

    def pendown(self):
        self.pen = 'D'

    def turnleft(self):
        turns = {'U': 'L', 'L': 'D', 'D': 'R', 'R': 'U'}
        self.direction = turns[self.direction]

    def turnright(self):
        turns = {'U': 'R', 'R': 'D', 'D': 'L', 'L': 'U'}
        self.direction = turns[self.direction]

    def move(self, distance):
        for _ in range(distance):
            if self.pen == 'D':
                self.canvas[self.ypos][self.xpos] = '*'

            if self.direction == 'U' and self.ypos < self.size - 1:
                self.ypos += 1
            elif self.direction == 'D' and self.ypos > 0:
                self.ypos -= 1
            elif self.direction == 'R' and self.xpos < self.size - 1:
                self.xpos += 1
            elif self.direction == 'L' and self.xpos > 0:
                self.xpos -= 1

        if self.pen == 'D':
            self.canvas[self.ypos][self.xpos] = '*'


def run_commands(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        size = int(lines[0])
        sketch = Sketch(size)

        for line in lines[1:]:
            if ',' in line:
                cmd, val = line.split(',')
                cmd = int(cmd)
                val = int(val)
                if cmd == 5:
                    sketch.move(val)
            else:
                cmd = int(line)
                if cmd == 1:
                    sketch.penup()
                elif cmd == 2:
                    sketch.pendown()
                elif cmd == 3:
                    sketch.turnright()
                elif cmd == 4:
                    sketch.turnleft()
                elif cmd == 6:
                    sketch.printsketch()


# Example usage
run_commands("Cshape.txt")
