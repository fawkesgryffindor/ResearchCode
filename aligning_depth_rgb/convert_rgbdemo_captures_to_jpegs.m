function convert_rgbdemo_captures_to_jpegs(input_folder)
% RGBD viewer
% (http://labs.manctl.com/rgbdemo/index.php/Documentation/Viewer) saves
% captured images in a folder in a certain pattern. This function will
% convert each of the ir, depth and rgb pngs into jpgs and store it in the
% destination folder. The reason to convert them to jpegs is so that the
% calibration toolbox can read them.
% INPUTS:
%       input_folder: String such that input_folder contains folders view*/
% JPEGS are saved input_folder/JPEGS/

% input_folder = 'C:\Users\varsha\Documents\Research\RGBDemo-0.4.0-Win32\calib_ims_katie';
% Find the number of images we are dealing with
b = regexp(genpath(input_folder),'(?<=(view))\d+', 'match');
num_captures = max(cellfun(@(x) str2num(x), b));
begin_index = min(cellfun(@(x) str2num(x), b));
for i=begin_index:num_captures
%    depth_yml_path =  sprintf('%s/view%.4d/raw/depth.yml', input_folder, i);
%    depth_yml_file = fopen(depth_yml_path);
   rgb_im = imread(sprintf('%s/view%.4d/color.png', input_folder, i));
   depth_im = imread(sprintf('%s/view%.4d/depth.png', input_folder, i));
   ir_im = imread(sprintf('%s/view%.4d/intensity.png', input_folder, i));
   imwrite(ir_im, sprintf('%s/intensity%.4d.jpg', input_folder, i), 'jpg');
   imwrite(rgb_im, sprintf('%s/color%.4d.jpg', input_folder, i), 'jpg');
end

end