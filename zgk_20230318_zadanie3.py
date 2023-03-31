import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
gi.require_foreign("cairo")

TRIANGLE_SIZE = 2000
levels = 5

def sierpinski(ctx, level):
    if level == 0:
        ctx.set_source_rgb(0.0, 0.0, 0.0)
        ctx.move_to(TRIANGLE_SIZE / 2, 0)
        ctx.line_to(TRIANGLE_SIZE / 2 + TRIANGLE_SIZE / 4, TRIANGLE_SIZE / 2)
        ctx.line_to(TRIANGLE_SIZE / 2 - TRIANGLE_SIZE / 4, TRIANGLE_SIZE / 2)
        ctx.close_path()
        ctx.fill()
    elif level > 0:
        size = TRIANGLE_SIZE / (2 ** level)
        ctx.save()
        ctx.scale(0.5, 0.5)
        ctx.translate(200, 0)
        sierpinski(ctx, level-1)
        ctx.restore()
        ctx.save()
        ctx.scale(0.5, 0.5)
        ctx.translate(size / 2 + 200, size)
        sierpinski(ctx, level-1)
        ctx.restore()
        ctx.save()
        ctx.scale(0.5, 0.5)
        ctx.translate(-size / 2 + 200, size)
        sierpinski(ctx, level-1)
        ctx.restore()


def rysuj(wdg, ctx):
    sierpinski(ctx, levels)

win = Gtk.Window()
win.set_title("Okno GTK")
win.set_default_size(640, 480)
win.connect("destroy", Gtk.main_quit)
da = Gtk.DrawingArea()
da.set_size_request(640, 480)
da.connect("draw", rysuj)
win.add(da)
win.show_all()
Gtk.main()