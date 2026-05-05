#include "joint.hpp"

Joint::Joint()
    : target(0.0f)
    , gravity(0.0f) 
{
    pid = PIDController();
    motor = MotorSimulator();
}

Joint::Joint(float kp, float ki, float kd, float inertia, float damping, float gravity)
    : pid(kp, ki, kd)
    , motor(inertia, damping)
    , gravity(gravity)
    , target(0.0f)
{}

void Joint::setTarget(float t) {target = t;}

float Joint::step(float dt) {
    float error = target - motor.getAngle();
    float torque = pid.step(error, dt);

    if(gravity > 0) {
        float gravity
    }
}