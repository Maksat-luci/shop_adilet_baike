
from tkinter import *
import random


tk = Tk()

tk.title('python game')

tk.resizable(0, 0)

canvas = Canvas(tk, width=500, height=400, highlightthickness=0)

canvas.pack()

tk.update()


class Ball:
    def init(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)

        self.canvas.move(self.id, 245, 250)
        starts = [-2 , -1, 1, 2]

        random.shuffle(starts)
        self.x = starts[0]

        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False


    def hit_blocks(self):
        pos = self.canvas.coords(self.id)
        blocks_pos = self.canvas.coords(self.blocks.id)
        if pos[2] >= blocks_pos[0] and pos[0] <= blocks_pos[2]:
            if pos[3] >= blocks_pos[1] and pos[3] <= blocks_pos[3]:
                return True
        return False

    def reverse(self):
        self.y = 1.5

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.hit_bottom = True
            canvas.create_text(250, 120, text='You lose', font=('Courier', 30), fill='red')
        if self.hit_paddle():
            self.y = -2
        if pos[0] <= 0:
            self.x = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2


class Paddle:
    def init(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        random.shuffle(start_1)
        self.starting_point_x = start_1[0]
        self.canvas.move(self.id, self.starting_point_x, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)

        self.started = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    def turn_right(self, event):
        self.x = 3

    def turn_left(self, event):
        self.x = -3

    def start_game(self, event):
        self.started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0

        elif pos[2] >= self.canvas_width:
            self.x = 0


class Score:
    def init(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id  = canvas.create_text(450, 10, text=self.score, font=('Courier', 20), fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)


class Blocks:
    def init(self, canvas, color, x, y):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x+100, y+10, fill=color)

    def is_touched(self, b):
        a = self.canvas.coords(self.id)
        if len(a) == 0:
            return False
        if( (b[0] >= a[0] and b[0] <= a[2]) or (b[2] >= a[0] and b[2] <= a[2]) ) and ( (b[1] >= a[1] and b[1] <= a[3]) or (b[3] >= a[1] and b[3] <= a[3]) ):
            score.hit()
            return True
        return False

    def draw(self):
        if self.is_touched(ball.canvas.coords(ball.id)):
            self.canvas.delete(self.id)
            ball.reverse()



def is_touched(canvas, a_id, b_id):
    a = canvas.coords(a_id)
    b = canvas.coords(b_id)
    if len(a) == 0 or len(b) ==0:
        return False
    return ( (b[0] >= a[0] and b[0] <= a[2]) or (b[2] >= a[0] and b[2] <= a[2]) ) and ( (b[1] >= a[1] and b[1] <= a[3]) or (b[3] >= a[1] and b[3] <= a[3]) )


score = Score(canvas, 'green')
paddle = Paddle(canvas, 'White')
ball = Ball(canvas, paddle, score, 'red')
blocks = [
    Blocks(canvas, 'blue', x*105, y*15) for x in range(4) for y in range(6)
]
while not ball.hit_bottom:
    if paddle.started == True:
        ball.draw()
        paddle.draw()
        for block in blocks:
            block.draw()

    tk.update_idletasks()
    tk.update()
    import time
    time.sleep(0.01)

time.sleep(1)