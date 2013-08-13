/* 
 * File:   main.cpp
 * Author: varsha
 *
 * Created on July 4, 2013, 3:50 PM
 */

#include <iostream>
#include <fstream>
#include <string>
//#include <cstdlib>
#include <opencv2/opencv.hpp>
//#include <opencv2/highgui/highgui.hpp>
//#include <opencv/cvaux.h>
//#include <opencv2/imgproc/imgproc.hpp>
//#include <opencv2/calib3d/calib3d.hpp>

using namespace std;
using namespace cv;

int n_boards = 0;
int board_w;
int board_h;

int main(int argc, char** argv) {
    board_w = 4; // Board width in squares
    board_h = 3; // Board height 
    n_boards = 1; // Number of boards
    string output_file_path = "/fiddlestix/Users/varsha/Documents/ResearchEyetrackCode/eyetrack/all_images/table_top_test_0/checkerboard_corners.txt";
    string input_file_path = "/fiddlestix/Users/varsha/Documents/ResearchEyetrackCode/eyetrack/all_images/table_top_test_0/image_file_list.txt";
    //    char *filename = "/fiddlestix/Users/varsha/Documents/ResearchEyetrackCode/eyetrack/all_images/table_top_test_0/IM_k1_0.png";

    ifstream fin(input_file_path.c_str());
    ofstream fout(output_file_path.c_str());
    string file_name;
    // check for bogus paths
    if (!fin.is_open()) {
        cout << "Could not open input file : " << input_file_path << endl;
        return 1;
    }
    if (!fout.is_open()) {
        cout << "Could not open output file : " << output_file_path << endl;
        return 1;
    }
    fout << "FILE_NAME,CORNERS" << endl;

    while (fin.good()) {
        getline(fin, file_name);
        fout<<file_name<<",";
        int board_n = board_w * board_h;
        CvSize board_sz = cvSize(board_w, board_h);

        CvPoint2D32f* corners = new CvPoint2D32f[ board_n ];
        int corner_count;
        int step, frame = 0, successes = 0;

        IplImage *image = cvLoadImage(file_name.c_str());
        IplImage *temp_image = cvCreateImage(cvSize(640, 512), 8, 3);
        IplImage *gray_image = cvCreateImage(cvGetSize(image), 8, 1);

        // Capture Corner views loop until we've got n_boards
        // succesful captures (all corners on the board are found)

        // Find chessboard corners:
        int found =0 , foundcount = 0;
        while(foundcount++<10 && !found) {
            found = cvFindChessboardCorners(image, board_sz, corners,
                    &corner_count, CV_CALIB_CB_ADAPTIVE_THRESH | CV_CALIB_CB_NORMALIZE_IMAGE | CV_CALIB_CB_FILTER_QUADS);
            cout<<found<<" ";
        }
        cout<<endl;

        // Get subpixel accuracy on those corners
        cvCvtColor(image, gray_image, CV_BGR2GRAY);
        cvFindCornerSubPix(gray_image, corners, corner_count, cvSize(11, 11),
                cvSize(-1, -1), cvTermCriteria(CV_TERMCRIT_EPS + CV_TERMCRIT_ITER, 30, 0.1));

        // Draw it
        cvDrawChessboardCorners(image, board_sz, corners, corner_count, found);
        cvResize(image, temp_image);
        cvShowImage("Calibration", temp_image);
        waitKey(10);

        // If we got a good board, add it to our data
        if (corner_count == board_n) {
            for (int j = 0; j < board_n; ++j)
                fout << corners[j].x << "," << corners[j].y << ",";
        } // end if(corner_count == board_n)
        fout<<endl;
    } // end while(fin.good())


    return 0;
}

