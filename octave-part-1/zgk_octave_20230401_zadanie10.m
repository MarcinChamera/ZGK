max_width = 100;
max_height = 100;

# wszystkie pliki png z tego folderu beda wybrane do przeskalowania
image_files = dir('zadanie10_input/*.png');

for i = 1:numel(image_files)
  image = imread(fullfile('zadanie10_input', image_files(i).name));

  % Get the current dimensions
  current_width = size(image, 2);
  current_height = size(image, 1);

  % Check if scaling is necessary
  if current_width > max_width || current_height > max_height
      % Calculate the scaling factor based on the aspect ratio
      aspect_ratio = current_width / current_height;

      % Scale the image based on the larger dimension
      if current_width > current_height
          new_width = max_width;
          new_height = max_width / aspect_ratio;
      else
          new_height = max_height;
          new_width = max_height * aspect_ratio;
      end

      % Perform the scaling
      scaled_image = imresize(image, [new_height, new_width]);

      scaled_filename = sprintf('scaled_%s', image_files(i).name);
      imwrite(scaled_image, fullfile('zadanie10_output', scaled_filename));
  else
      scaled_image = image;
  end
end
