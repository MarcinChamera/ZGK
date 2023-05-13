pkg load image;

IMG_GRAY = imread('dog-niemiecki-gray.png');
I = double(IMG_GRAY) / 255;

# krawedzie
W = imfilter(I, fspecial('sobel'));

imwrite(W, 'zad3_1.png');

# potrzebne beda teraz 3 kanaly aby moc stworzyc obraz z czerwonym kolorem
red = W;
green = W;
blue = W;

# wszedzie gdzie zostaly wykryte krawedzie na obrazie w grayscale, daj max czerwony
red(red > 0.1) = 1.0;

# pozostale kanaly wyzeruj
green(:) = 0.0;
blue(:) = 0.0;

imwrite(cat(3, red, green, blue), 'zad3_2.png');
