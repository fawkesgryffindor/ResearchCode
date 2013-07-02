% function align_depth_rgb(input_folder)
% addpath(genpath('C:\Users\varsha\Documents\Research\toolbox_calib'));
addpath(genpath('/fiddlestix/Users/varsha/Documents/ResearchTools/toolbox_calib/'));
input_folder = '/fiddlestix/Users/varsha/Documents/ResearchTools/RGBDemo-0.4.0-Win32/calib_ims_home_kinect/view0000/';
raw_depth_yml_path = sprintf('%s\\raw\\depth.yml', input_folder);
filename = fopen(raw_depth_yml_path);
% a = csvread(sprintf('%s\\raw\\Untitled.txt', input_folder));
a = csvread(sprintf('%s/raw/Untitled.txt', input_folder));
a = a';
b = a(find(a(:)));
cx_d = 329.04791;
cy_d = 252.78205;
fx_d = 578.57106;
fy_d = 579.11600;
fx_rgb = 525.85262;
fy_rgb = 526.33640;
cx_rgb = 305.79930;
cy_rgb = 265.46451;
% om = [ 0.02175   0.06981  -0.00162 ];
% T = [ -0.04247   0.00754  0.01086 ];
% R = rodrigues(om);
% fx_rgb = 5.2921508098293293e+02;
% fy_rgb = 5.2556393630057437e+02;
% cx_rgb = 3.2894272028759258e+02;
% cy_rgb = 2.6748068171871557e+02;
% fx_d =5.9421434211923247e+02;
% fy_d =5.9104053696870778e+02;
% cx_d =3.3930780975300314e+02;
% cy_d =2.4273913761751615e+02;
R = [ 9.9984628826577793e-01 1.2635359098409581e-03 -1.7487233004436643e-02
    -1.4779096108364480e-03 9.9992385683542895e-01 -1.2251380107679535e-02
    1.7470421412464927e-02 1.2275341476520762e-02 9.9977202419716948e-01 ];
% T = [ 1.9985242312092553e-02, -7.4423738761617583e-04, -1.0916736334336222e-02 ];
T = [-0.0254 -0.00013 -0.00218];
depth_meters = 1./(b*-0.0030711016 + 3.3309495161);
depth_meters(b==2047) = 0;
depth_vals = (reshape(depth_meters, 640, 480))';

[xir, yir] = meshgrid(1:640,1:480);
% xir = xir';
% yir = yir';
XIR_mat = (xir - cx_d).*depth_vals*(1/fx_d);
YIR_mat = (yir - cy_d).*depth_vals*(1/fy_d);
ZIR_mat = depth_vals;
ind = sub2ind(size(depth_vals),yir(:),xir(:));
XIR = XIR_mat(ind);
YIR = YIR_mat(ind);
ZIR = ZIR_mat(ind);
% XIR = reshape(XIR_mat,640*480,1);
% YIR = reshape(YIR_mat,640*480,1);
% ZIR = reshape(ZIR_mat,640*480,1);
mat = [XIR YIR ZIR];
RGB_3D = bsxfun(@plus,mat*R,T);
xrgb = RGB_3D(:,1)*fx_rgb./RGB_3D(:,3) + cx_rgb;
yrgb = RGB_3D(:,2)*fy_rgb./RGB_3D(:,3) + cy_rgb;
xrgb(xrgb<1) = 1;
xrgb(xrgb>640) = 640;
yrgb(yrgb<1) = 1;
yrgb(yrgb>480) = 480;
xrgb = round(xrgb);
yrgb = round(yrgb);
depth_im = imread(sprintf('%s/depth.png', input_folder));
rgb_im = imread(sprintf('%s/color.png', input_folder));
a = zeros(size(rgb_im));
% a(:,:,1) = depth_im;
% a(:,:,2) = depth_im;
% a(:,:,3) = depth_im;
% figure;
% subplot(1,2,1);
% imshow(uint8(a));
ind_ir_red = sub2ind(size(rgb_im),yir(:),xir(:),ones(length(ind),1));
ind_ir_green = sub2ind(size(rgb_im),yir(:),xir(:),2*ones(length(ind),1));
ind_ir_blue = sub2ind(size(rgb_im),yir(:),xir(:),3*ones(length(ind),1));
ind_rgb_red = sub2ind(size(rgb_im),yrgb(:),xrgb(:),ones(length(ind),1));
ind_rgb_green = sub2ind(size(rgb_im),yrgb(:),xrgb(:),2*ones(length(ind),1));
ind_rgb_blue = sub2ind(size(rgb_im),yrgb(:),xrgb(:),3*ones(length(ind),1));
a(ind_ir_red) = rgb_im(ind_rgb_red);    a(ind_ir_green) = rgb_im(ind_rgb_green);    a(ind_ir_blue) = rgb_im(ind_rgb_blue);
% subplot(1,2,2);
% imshow(uint8(a));
 I = edge(depth_im, 'canny');
[xx yy] = ind2sub(size(I), find(I==1));
ind = sub2ind(size(a), xx, yy, 2*ones(length(xx), 1));
A = a;
imshow(A)
imshow(uint8(A))
A(ind) = 255;
imshow(uint8(A))

% end
