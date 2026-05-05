#include "arm.hpp"

void Arm::addJoint(Joint j) {
    joints.push_back(j);
}

void Arm::removeJoint() {
    joints.pop_back();
}

void Arm::setTarget(int i, float t) {
    joints[i].setTarget(t);
}

void Arm::step(float dt) {
    for (Joint j : joints) {
        j.step(dt);
    }
}