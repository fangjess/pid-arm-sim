#include "arm.hpp"

int Arm::getJointCount() {
    return joints.size();
}

void Arm::addJoint(Joint j) {
    joints.push_back(j);
}

void Arm::popJoint() {
    joints.pop_back();
}

void Arm::removeJoint(int i) {
    joints.erase(joints.begin() + i);
}

void Arm::setTarget(int i, float t) {
    joints[i].setTarget(t);
}

float Arm::getAngle(int i) {
    return joints[i].getAngle();
}

Axis Arm::getAxis(int i) {
    return joints[i].getAxis();
}

float Arm::getLength(int i) {
    return joints[i].getArmLength();
}

void Arm::step(float dt) {
    for (Joint& j : joints) {
        j.step(dt);
    }
}