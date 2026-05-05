cmake_minimum_required(VERSION 3.10)
project(pid-arm-sim)

set(CMAKE_CXX_STANDARD 17)

add_executable(simulation
    src/main.cpp
    src/arm.cpp
    src/joint.cpp
    src/motor_simulator.cpp
    src/pid_controller.cpp
)