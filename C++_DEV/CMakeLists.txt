cmake_minimum_required(VERSION 3.20)
project(C___DEV)

set(CMAKE_CXX_STANDARD 23)

# input.txt에서 값 읽기 위한 설정
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DNDEBUG")

add_executable(C___DEV main.cpp)
