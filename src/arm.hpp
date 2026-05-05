#pragma once
#include "joint.hpp"
#include <vector>

class Arm {
    std::vector<Joint> joints;

public:
    void addJoint(Joint j);
    void removeJoint();
    void setTarget(int i, float t);
    float getAngle(int i);
    void step(float dt);
};