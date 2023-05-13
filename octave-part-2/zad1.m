pkg load image;

IMG_RGB = imread('dog-niemiecki-gray.png');

# 2d filter 3x3 z jedynkami
F = [ 1 1 1;
      1 1 1;
      1 1 1 ];
W = conv2(IMG_RGB, F);
W = uint8(W);
imwrite(W, 'zad1_1.png');

# 2d filter 3x3 z wartosciami 0.5
F = [ 0.5 0.5 0.5;
      0.5 0.5 0.5;
      0.5 0.5 0.5 ];
W = conv2(IMG_RGB, F);
W = uint8(W);
imwrite(W, 'zad1_2.png');

# 'Rectangular averaging filter'
avg = fspecial('average', 7);
W = conv2(IMG_RGB, avg);
W = uint8(W);
imwrite(W, 'zad1_3.png');

# 'Sharpening filter'
unsharp = fspecial('unsharp');
W = conv2(IMG_RGB, unsharp);
W = min(max(W, 0), 1);
imwrite(W, 'zad1_4.png');

# Create Gaussian filter
gaussian = fspecial('gaussian');
W = conv2(IMG_RGB, gaussian);
W = uint8(W);
imwrite(W, 'zad1_5.png');

sobel = fspecial('sobel');
W = conv2(IMG_RGB, sobel);
W = uint8(W);
imwrite(W, 'zad1_6.png');
