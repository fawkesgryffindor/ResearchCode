# This project requires OpenCV and libfreenect
cmake_minimum_required(VERSION 2.8)
SET(CMAKE_CXX_FLAGS "-std=c++0x")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
set(LIBS ${LIBS} ${OpenCV_LIBRARIES})

set(sources main.cpp)

# Link the required libraries (OpenCV) to the exectuable
add_executable(checkerboard ${sources})
target_link_libraries(checkerboard ${LIBS})

