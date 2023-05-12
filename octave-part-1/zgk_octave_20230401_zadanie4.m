pkg load statistics

a = [ unifrnd(0, 1) unifrnd(2, 10) unifrnd(0, 1)
      unifrnd(-5, -1) unifrnd(0, 1) unifrnd(-5, 5) ];

# sprawdzenie
a
disp("Sprawdzenie el > 1 & el < 0 przed przycieciem:");
a(a > 1.0)
a(a < 0.0)

# przyciecie
disp("Przyciecie:");
a(a > 1.0) = 1.0;
a(a < 0.0) = 0.0

# sprawdzenie
a
disp("Sprawdzenie el > 1 & el < 0 po przycieciu:");
a(a > 1.0)
a(a < 0.0)

