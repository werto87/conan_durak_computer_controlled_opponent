cmake_minimum_required(VERSION 3.15)
project(test_package CXX)

find_package(durak_computer_controlled_opponent REQUIRED CONFIG)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE durak_computer_controlled_opponent::durak_computer_controlled_opponent)