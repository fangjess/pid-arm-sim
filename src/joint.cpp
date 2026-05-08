#include "joint.hpp"
#include <cmath>

Joint::Joint()
    : target(0.0f)
    , armLength(0.3f)
    , mass(0.5f)
    , axis(Axis::Horizontal)
{
    pid = PIDController();
    motor = MotorSimulator();
}

void Joint::setTarget(float t) {
    target = t;
    pid.resetIntegral();
}

float Joint::getTarget() {
    return target;
}

void Joint::setArmLength(float l) {armLength = l;}

void Joint::toggleAxis() {
    if (axis == Axis::Horizontal) {
        axis = Axis::Vertical;
    } else {
        axis = Axis::Horizontal;
    }
}

float Joint::getAngle() {
    return motor.getAngle();
}

Axis Joint::getAxis() {
    return axis;
}

float Joint::getArmLength() {
    return armLength;
}

float Joint::step(float dt) {
    float error = target - motor.getAngle();
    
    // wrap angles for horizontal rotation
    if (axis == Axis::Horizontal) {
        while (error > 180.0f)  error -= 360.0f;
        while (error < -180.0f) error += 360.0f;
    }

    float torque = pid.step(error, dt);

    // gravity force is calculated if axis of movement is vertical
    // currently affect of gravity on each joint is independent
    // may implement propagation of angle changes in future
    if(axis == Axis::Vertical) {
        float angleRadians = motor.getAngle() * M_PI / 180.0f;
        float gravityForce = mass * 9.81f * armLength * cos(angleRadians);
        torque -= gravityForce;
    }

    return motor.step(torque, dt);
}