img= imread('zadanie2_kolaz_obraz2.png');

img(:, 30:50, 3) = 255;

imwrite(img, 'zgk_octave_20230401_zadanie3_output.png');
