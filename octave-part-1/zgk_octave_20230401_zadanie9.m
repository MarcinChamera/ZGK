# https://octave.sourceforge.io/image/function/imresize.html
pkg load image
img = imread('dog-niemiecki.jpg');

img_resized = imresize(img, [100 100]);

imwrite(img_resized, 'zgk_octave_20230401_zadanie9_output.png');