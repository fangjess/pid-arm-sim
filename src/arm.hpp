#pragma once
#include "joint.hpp"
#include <vector>

class Arm {
    std::vector<Joint> joints;

public:
    int getJointCount();
    void addJoint(Joint j);
    void addNewJoint();
    void popJoint();
    void removeJoint(int i);
    void setTarget(int i, float t);
    float getTarget(int i);
    float getAngle(int i);
    Axis getAxis(int i);
    float getLength(int i);
    void toggleAxis(int i);
    float getKp(int i);
    void setKp(int i, float f);
    void step(float dt);
};