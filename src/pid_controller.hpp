#pragma once

/*
    kp scales torque based on error
    ki accounts for growing error due to damping
    kd looks at how fast error is decreasing and decreases torque
    integral is accumulation of error from past moments
*/

class PIDController  {
    float kp;
    float ki;
    float kd;
    float integral;
    float prevError;

public:
    PIDController() {}
    PIDController(float kp, float ki, float kd) {}
    float step(float error, float dt) {}
};