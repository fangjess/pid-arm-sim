#pragma once
#include "joint.hpp"
#include <vector>

class Arm {
    std::vector<Joint> joints;

public:
    int getJointCount();
    void addJoint(Joint j);
    void popJoint();
    void removeJoint(int i);
    void setTarget(int i, float t);
    float getAngle(int i);
    Axis getAxis(int i);
    float getLength(int i);
    void toggleAxis(int i);
    void step(float dt);
};