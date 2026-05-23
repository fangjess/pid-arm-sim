# pid-arm-sim
The simulator models a multi-joint robotic arm where each joint is independently controlled by a PID controller. The user can configure up to five joints, toggle each between horizontal and vertical axes of rotation, tune the PID formula live and set target angles, watching the arm move in real time.

## Features
- 2D top-down and side view rendering of arm movement
- Control each joint motor individually: "Current angle" shows how close arm is to your desired target angle, toggle axis of movement for each joint
- Live tuning of PID formula: adjust Kp multiplier to change motor aggressiveness
- Effect of gravity on movement of vertical-axis arms: force of gravity affects torque applied to arms pitching up/down

## Demo
https://github.com/user-attachments/assets/8e6708c7-718d-4ad2-9a7e-de59c03dfdc0

## Development Notes
This project was built as a learning exercise in C++ and motion control systems. Documentation and AI assistance (Claude) was consulted throughout development to understand concepts such as PID control, rotational physics and language syntax. Architectural decisions, design choices and debugging work are my own.

### Built With
- C++17
- CMake
- pybind11
- PyQt6
- Linux
- Google Test
- g++
- Git

### Concepts
- PID Control theory
- C++/Python interop
- Rotational physics simulation
- 2d kinematics
- PyQt6 GUI

### Challenges
- Applying PID control theory and rotational physics, torque calculations
- Using CMake build system
- PyQt6 devlopment, canvas rendering, foreshortening


## Class Diagram
<img width="1320" height="1297" alt="UML class" src="https://github.com/user-attachments/assets/8ca3ae89-a693-4d6b-a0e7-5ff2c8ecb845" />

## Application Wireframe
Made using Figma
<img width="1041" height="688" alt="PID Arm Simulator Wireframe" src="https://github.com/user-attachments/assets/9a0fe472-00fb-422a-a366-49f390b89bdb" />

## To Add:
- Graphical representation of each arms' movement
- Torque clamping; currently there's technically no limit on how much torque can be produced
- Propagation of effect of gravity on joints: currently effect of gravity does not accumulate, each joint reacts to gravity as its own isolated system.
- Adjustment of arm length and mass to affect gravity; right now just has 1 default length and mass
- Ki and Kd gain sliders
