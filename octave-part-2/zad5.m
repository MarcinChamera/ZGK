pkg load image;

# rgb to grayscale
img = imread('coins_easy.jpg');
img_gray = rgb2gray(img);

threshold = 0.55;
img_binary_055 = im2bw(img_gray, threshold);
imwrite(img_binary_055, 'zad5_easy_threshold_055.png');

#########################################################

img = imread('coins.jpg');
img_gray = rgb2gray(img);

threshold = 0.45;
img_binary_045 = im2bw(img_gray, threshold);
imwrite(img_binary_045, 'zad5_threshold_045.png');

threshold = 0.55;
img_binary_055 = im2bw(img_gray, threshold);
imwrite(img_binary_055, 'zad5_threshold_055.png');

img_close = bwmorph(img_binary_055, 'close');
imwrite(img_close, 'zad5_close.png');

img_dilate = bwmorph(img_binary_055, 'dilate');
imwrite(img_dilate, 'zad5_dilate.png');

img_remove = bwmorph(img_binary_055, 'remove');
img_remove_dilate = bwmorph(img_remove, 'dilate');
img_remove_dilate_2 = bwmorph(img_remove_dilate, 'dilate');
imwrite(img_remove_dilate, 'zad5_remove_dilate.png');

img_histeq = histeq(img_gray);
threshold = 0.85;
img_binary_085 = im2bw(img_histeq, threshold);
img_binary_085_close = bwmorph(img_binary_085, 'close');
imwrite(img_binary_085_close, 'zad5_histeq_threshold_085_close.png');

