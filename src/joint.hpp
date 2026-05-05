#pragma once
#include "motor_simulator.hpp"
#include "pid_controller.hpp"

class Joint {
    PIDController pid;
    MotorSimulator motor;
    float target;
    float gravity; // how much gravity? e.g. 45 degree mount = 0.5 gravity

public:
    Joint() {}
    Joint(float kp, float ki, float kd, float inertia, float damping, float gravity) {}
    void setTarget(float t) {}
    float step(float dt) {} // torque in from controller, position out from motor
};