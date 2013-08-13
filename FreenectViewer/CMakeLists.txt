# This project requires OpenCV and libfreenect
cmake_minimum_required(VERSION 2.8)
SET(CMAKE_CXX_FLAGS "-std=c++0x")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
set(LIBS ${LIBS} ${OpenCV_LIBRARIES})

# This project includes a custom macro to find libfreenect
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake")
find_package(Freenect REQUIRED)
include_directories(${Freenect_INCLUDE_DIRS})
set(LIBS ${LIBS} ${Freenect_LIBRARIES})

# Finds location of opengl libs
FIND_PACKAGE( OpenGL )
#FIND_PACKAGE( GLU )
FIND_PACKAGE( GLUT )

set(sources main.cpp)

# Link the required libraries (OpenCV, freenect, face_tracker and libsvm) to the exectuable
add_executable(fviewer ${sources})
target_link_libraries(fviewer ${LIBS} ${OpenGL_LIBRARY} ${GLUT_LIBRARY})

