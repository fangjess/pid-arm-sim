#include "arm.hpp"
#include <iostream>

int main() {
    float dt = 0.001f;

    Arm arm;
    arm.addJoint(Joint());
    arm.setTarget(0, 90.0f);

    // while(true) {
    //     arm.step(dt);
    // }
    for (int i = 0; i < 700; i++) {
        arm.step(dt);
        std::cout << "tick " << i << ": " << arm.getAngle(0) << "°\n";
    }
}