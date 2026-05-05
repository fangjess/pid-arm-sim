#include "motor_simulator.hpp"

MotorSimulator::MotorSimulator()
    : inertia(0.01f), damping(0.1f), angle(0.0f), velocity(0.0f) {}

MotorSimulator::MotorSimulator(float i, float d)
    : inertia(i), damping(d), angle(0.0f), velocity(0.0f) {}

float MotorSimulator::getAngle() {return angle;}

float MotorSimulator::step(float torque, float dt) {
    float acceleration = (torque - (damping * velocity)) / inertia;
    velocity += acceleration * dt;
    angle += velocity * dt;
    return angle;
}