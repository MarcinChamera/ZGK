dog_img = imread('dog-niemiecki.jpg');
gray_dog_img = imread('zgk_octave_20230401_zadanie7_output1.png');

function retval = covertrgb2gray (img)
    [rows_number, columns_number, channels_number] = size(img);
    if (channels_number > 1)
        red = img(:,:,1);
        green = img(:,:,2);
        blue = img(:,:,3);
        gray_img = 0.298936 * red + 0.587043 * green + 0.114021 * blue;
        retval = gray_img;
    else
        disp('Image is already in grayscale');
        retval = img;
    endif
endfunction

imwrite(covertrgb2gray(dog_img), 'zgk_octave_20230401_zadanie8_output.png');
