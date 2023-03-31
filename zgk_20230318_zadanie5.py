import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk, Gtk
gi.require_foreign("cairo")

class Odcinek():
    def __init__(self):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

# Klasa Okno dziedziczy po klasie Gtk.Window.
#
class Okno(Gtk.Window):

    # W Pythonie konstruktor klasy nazywa się __init__.
    #
    def __init__(self):
        super(Okno, self).__init__()

        # W Pythonie nie trzeba wstępnie deklarować pól obiektu, wystarczy coś
        # spróbować do nich podstawić i to je automatycznie stworzy. None jest
        # odpowiednikiem pustego wskaźnika lub SQL-owego NULL, oznacza brak
        # wartości.
        #
        self.lista_odcinkow = []

        self.set_title("Okno GTK")
        self.set_default_size(400, 300)
        self.connect("destroy", Gtk.main_quit)
        da = Gtk.DrawingArea()
        da.set_size_request(200, 200)
        da.connect("draw", self.on_draw)
        da.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        da.connect("button-press-event", self.on_button_press)
        self.add(da)
        self.show_all()

    # Dość często stosowaną konwencją jest nadawanie metodom-callbackom
    # wywoływanym w reakcji na zdarzenia nazw pochodzących od tych zdarzeń.
    # W przypadku zdarzenia o nazwie "draw" mamy więc metodę "on_draw".
    # Jak w poprzednich przykładach jako argumenty dostaje referencję do
    # wymagającego przerysowania DrawingArea oraz związany z tym obszarem
    # kontekst rysowania Cairo, ale ponieważ teraz jest to metoda, a nie
    # funkcja, to jako dodatkowy pierwszy argument przekazywana jest
    # referencja do naszego obiektu-okna.
    #
    def on_draw(self, widget, ctx):

        # Biblioteka GTK wypełnia obszar kolorem tła zanim wywoła naszą
        # metodę-callback, robienie tego drugi raz byłoby nadmiarowe.
        #
        # w = widget.get_allocated_width()
        # h = widget.get_allocated_height()
        # ctx.set_source_rgb(1.0, 1.0, 1.0)
        # ctx.rectangle(0, 0, w, h)
        # ctx.fill()

        for odcinek in self.lista_odcinkow:
            if odcinek.x1 is not None:
                ctx.arc(odcinek.x1 * self.get_allocated_width(), odcinek.y1 * self.get_allocated_height(), 8, 0.0, 6.283)    # ciut mniej niż 2π
                ctx.close_path()
                ctx.stroke()

            if odcinek.x2 is not None:
                ctx.move_to(odcinek.x1 * self.get_allocated_width(), odcinek.y1 * self.get_allocated_height())
                ctx.line_to(odcinek.x2 * self.get_allocated_width(), odcinek.y2 * self.get_allocated_height())
                ctx.stroke()

    # Tu jako trzeci argument dostajemy obiekt reprezentujący zdarzenie. Ma on
    # m.in. pola z współrzędnymi kliknięcia wyrażonymi w układzie związanym
    # z DrawingArea, bo to właśnie do niego "podpięliśmy" poniższą metodę
    # obsługi zdarzeń.
    #
    def on_button_press(self, widget, event):
        print(self.get_allocated_width())
        print(self.get_allocated_height())
        # Lewy przycisk myszki ma numer 1, nie obsługuj zdarzenia jeśli
        # to nie on został naciśnięty.
        #
        if event.button != 1:
            return False
        if len(self.lista_odcinkow) == 0 or self.lista_odcinkow[-1].x2 is not None:
            self.lista_odcinkow.append(Odcinek())
            self.lista_odcinkow[-1].x1 = event.x / self.get_allocated_width()
            self.lista_odcinkow[-1].y1 = event.y / self.get_allocated_height()
        elif self.lista_odcinkow[-1].x2 is None:
            self.lista_odcinkow[-1].x2 = event.x / self.get_allocated_width()
            self.lista_odcinkow[-1].y2 = event.y / self.get_allocated_height()

        # Poproś bibliotekę GTK aby przy najbliższej okazji przerysowała
        # nasze DrawingArea.
        #
        widget.queue_draw()

        # Obsłużyliśmy zdarzenie, GTK już nic więcej nie musi z nim robić.
        #
        return True

# Inicjalizacja aplikacji sprowadza się teraz do stworzenia okna
# i uruchomienia pętli obsługi zdarzeń biblioteki GTK.
#
o = Okno()
Gtk.main()