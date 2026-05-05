#pragma once

class MotorSimulator {
    float inertia;
    float damping;
    float angle;
    float velocity;

public:
    MotorSimulator() {}
    MotorSimulator(float inertia, float damping) {}
    float step(float torque, float dt) {}
};