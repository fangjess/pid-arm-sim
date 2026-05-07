#include "pid_controller.hpp"

PIDController::PIDController()
    : kp(1.0f), ki(0.01f), kd(0.1f), integral(0.0f), prevError(0.0f) {}

PIDController::PIDController(float a, float b, float c)
    : kp(a), ki(b), kd(c), integral(0.0f), prevError(0.0f) {}

void PIDController::resetIntegral() {
    integral = 0;
    prevError = 0;
}

float PIDController::step(float error, float dt) {
    float de = error - prevError;
    while (de > 180.0f)  de -= 360.0f;
    while (de < -180.0f) de += 360.0f;

    float derivative = de / dt; // how fast error is changing
    prevError = error;
    integral += error * dt;
    
    float torque =
        (kp * error) +
        (ki * integral) +
        (kd * derivative);
    return torque;
}