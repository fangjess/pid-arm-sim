# pid-arm-sim
The simulator models a multi-joint robotic arm where each joint is independently controlled by a PID controller. The user can configure up to five joints, toggle each between horizontal and vertical axes of rotation, tune the PID formula live and set target angles, watching the arm move in real time.

## Concepts
- PID Control theory
- C++/Python interop
- Rotational physics simulation
- 2d kinematics
- PyQt6 GUI

## Development Notes
This project was built as a learning exercise in C++ and motion control systems. Documentation and AI assistance (Claude) was consulted throughout development to understand concepts such as PID control, rotational physics and language syntax. Architectural decisions, design choices and debugging work are my own.

## Challenges
- Applying PID control theory and rotational physics, torque calculations
- CMake build system
- PyQt6 devlopment, canvas rendering, foreshortening

## Demo
https://github.com/user-attachments/assets/304731a4-64b7-43ac-959e-8390f241dddc

## Class Diagram
<img width="1320" height="1297" alt="UML class" src="https://github.com/user-attachments/assets/8ca3ae89-a693-4d6b-a0e7-5ff2c8ecb845" />

## Application Wireframe
Made using Figma
<img width="1041" height="688" alt="PID Arm Simulator Wireframe" src="https://github.com/user-attachments/assets/9a0fe472-00fb-422a-a366-49f390b89bdb" />

## To Add:
- Control panel showing current angle for comparison to target angle
- Graphical representation of each arms' movement
- Torque clamping; currently there's technically no limit on how much torque can be produced
- Effect of gravity on joints
- Ki and Kd gain sliders
