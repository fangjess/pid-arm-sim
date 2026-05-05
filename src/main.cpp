#include "arm.hpp"

int main() {
    float dt = 0.016f; // 60 ticks per second
    
    Arm arm;
    arm.addJoint(Joint());
    arm.setTarget(0, 90.0f);

    while(true) {
        arm.step(dt);
    }
}