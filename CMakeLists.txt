cmake_minimum_required(VERSION 3.10)
project(pid-arm-sim)

set(CMAKE_CXX_STANDARD 17)

set(pybind11_DIR "/home/fangjess/projects/pid-arm-sim/venv/lib/python3.10/site-packages/pybind11/share/cmake/pybind11")
find_package(pybind11 REQUIRED)

add_library(physics SHARED
    src/arm.cpp
    src/joint.cpp
    src/motor_simulator.cpp
    src/pid_controller.cpp
)

add_executable(simulate
    src/main.cpp
)

target_link_libraries(simulate physics)

pybind11_add_module(arm_sim
    src/bindings.cpp
)
target_link_libraries(arm_sim PRIVATE physics)