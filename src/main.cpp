#include "arm.hpp"
#include <iostream>

int main() {
    Arm arm;
    arm.addJoint(Joint());  // default horizontal joint
    
    arm.setTarget(0, 170.0f);  // target near the wrap boundary
    
    float dt = 0.001f;
    for (int i = 0; i < 5000; i++) {
        arm.step(dt);
        if (i % 100 == 0) {  // print every 100 ticks
            std::cout << "tick " << i 
                      << " angle: " << arm.getAngle(0) 
                      << "\n";
        }
    }

    // now set target on the other side of the boundary
    std::cout << "\n--- changing target to -170 ---\n\n";
    arm.setTarget(0, -170.0f);

    for (int i = 0; i < 5000; i++) {
        arm.step(dt);
        if (i % 100 == 0) {
            std::cout << "tick " << i 
                      << " angle: " << arm.getAngle(0) 
                      << "\n";
        }
    }

    return 0;
}