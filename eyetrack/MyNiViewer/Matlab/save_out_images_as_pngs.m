number_index = 0;
burst_index = 0;
for i = 1:27
    burst_index = mod(burst_index + 1, 4);
    if(burst_index<1)
        number_index = number_index + 1;
        burst_index = 1;
    end
    if(number_index < 1)
        number_index = 1;
    end
%     fprintf('%d_%d\n',number_index, burst_index);
    [rgb_image depth_image folder] = display_images(number_index, burst_index);
    imwrite(rgb_image, sprintf('%s/Image_%d_%d.png',folder, number_index, burst_index), 'png');
end
