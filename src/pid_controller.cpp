#include "pid_controller.hpp"

PIDController::PIDController()
    : kp(10.0f), ki(0.01f), kd(0.5f), integral(0.0f), prevError(0.0f) {}

PIDController::PIDController(float a, float b, float c)
    : kp(a), ki(b), kd(c), integral(0.0f), prevError(0.0f) {}

float PIDController::step(float error, float dt) {
    float derivative = (error - prevError) / dt; // how fast error is changing
    prevError = error;
    integral += error * dt;
    float torque =
        (kp * error) +
        (ki * integral) +
        (kd * derivative);
    return torque;
}