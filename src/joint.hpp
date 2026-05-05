#pragma once
#include "motor_simulator.hpp"
#include "pid_controller.hpp"
#include "axis.hpp"

class Joint {
    PIDController pid;
    MotorSimulator motor;
    float target;
    float armLength; // arm length in metres
    float mass; // arm/load mass in kg
    Axis axis; // axis of movement

public:
    Joint() {}
    void setTarget(float t) {}
    void setGravity(float g) {}
    void setArmLength(float l) {}
    void toggleAxis() {}
    float step(float dt) {} // torque in from controller, position out from motor
};