img = imread('dog-niemiecki.jpg');

red = img(:,:,1);
green = img(:,:,2);
blue = img(:,:,3);

gray1 = 0.298936 * red + 0.587043 * green + 0.114021 * blue;
% gray2 = uint8(double(red) / 3 + double(green) / 3 + double(blue) / 3);

# mala roznica
gray2 = red / 3 + green / 3 + blue / 3;

# duza roznica
gray3 = (red + green + blue) / 3;

imwrite(gray1, 'zgk_octave_20230401_zadanie7_output1.png');
imwrite(gray2, 'zgk_octave_20230401_zadanie7_output2.png');
imwrite(gray3, 'zgk_octave_20230401_zadanie7_output3.png');

