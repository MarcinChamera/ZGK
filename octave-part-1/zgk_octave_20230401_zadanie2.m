img1 = imread('zadanie2_kolaz_obraz1.png');
img2 = imread('zadanie2_kolaz_obraz2.png');

[rows_number1, columns_number1, layers_number1] = size(img1);
[rows_number2, columns_number2, layers_number2] = size(img2);
left_side = img1(:, 1:columns_number1/2, :);
right_side = img2(:, columns_number2/2+1:columns_number2, :);
result = cat(2, left_side, right_side);
imwrite(result, 'zgk_octave_20230401_zadanie2_output.png');
