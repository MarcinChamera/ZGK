import cairo
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gdk
import random
import math

class Ball:
    def __init__(self, x, y, r, vx, vy):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self, ctx):
        ctx.arc(self.x, self.y, self.r, 0, 2 * math.pi)
        ctx.fill()

class Racket:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, ctx):
        ctx.rectangle(self.x, self.y, self.w, self.h)
        ctx.fill()

class Game(Gtk.Window):
    def __init__(self):
        super(Game, self).__init__()
        self.width = 640
        self.height = 480
        self.ball = Ball(self.width / 2, self.height / 2, 10, 200, 200)
        self.racket = Racket(self.width / 2 - 50, self.height - 20, 100, 10)
        self.set_default_size(self.width, self.height)
        self.connect("destroy", Gtk.main_quit)
        self.area = Gtk.DrawingArea()
        self.area.connect("draw", self.on_draw)
        self.connect("key-press-event", self.on_key_press)
        self.add(self.area)
        self.show_all()
        self.last_time = 0
        self.tid = None
        self.toggle_animation()

    def toggle_animation(self):
        if self.tid is None:
            self.tid = GLib.timeout_add(20, self.on_timeout, None)
        else:
            GLib.source_remove(self.tid)
            self.tid = None

    def on_timeout(self, user_data):
        current_time = GLib.get_monotonic_time()
        dt = 0.02
        self.last_time = current_time
        self.ball.update(dt)
        return True

    def on_draw(self, widget, ctx):
        ctx.set_source_rgb(0, 0, 0)
        ctx.rectangle(0, 0, self.width, self.height)
        ctx.fill()

        # kolizje z krawedziami
        if self.ball.y > self.height - self.ball.r:
            Gtk.main_quit()
        if self.ball.x - self.ball.r < 0:
            self.ball.vx = abs(self.ball.vx)
            self.ball.vx += random.uniform(0, 1)
        elif self.ball.x + self.ball.r > self.width:
            self.ball.vx = -abs(self.ball.vx)
            self.ball.vx -= random.uniform(0, 1)
        elif self.ball.y - self.ball.r < 0:
            self.ball.vy = abs(self.ball.vy)
            self.ball.vy += random.uniform(0, 1)

        # kolizje z rakieta
        if (self.ball.y + self.ball.r >= self.racket.y and
            self.ball.x >= self.racket.x and
            self.ball.x <= self.racket.x + self.racket.w):
            self.ball.vy = -abs(self.ball.vy)

        # rysuj rakiete i pilke
        ctx.set_source_rgb(1, 1, 1)
        self.ball.draw(ctx)
        self.racket.draw(ctx)

        # rysuje ponownie po 10ms
        GLib.timeout_add(10, self.redraw)

    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_Left and self.racket.x >= 20:
            self.racket.x -= 20
        if event.keyval == Gdk.KEY_Right and self.racket.x <= self.width - self.racket.w - 20:
            self.racket.x += 20

    def redraw(self):
        self.area.queue_draw()
        return True

if __name__ == "__main__":
    game = Game()
    Gtk.main()