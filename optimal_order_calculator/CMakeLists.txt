project(optimal_order_calculator)

cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

set(CMAKE_CXX_FLAGS "-march=native -O2 -std=c++11")

include_directories(usr/include/eigen3)

add_executable(optimal_order_calculator
	main.cpp
	)
