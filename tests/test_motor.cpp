#include <gtest/gtest.h>
#include "../src/motor_simulator.hpp"

TEST(motorTests, testPositiveMovement) {
    MotorSimulator motor;
    float position = motor.step(100.0f, 0.001f);
    EXPECT_GT(position, 0.0f);
}

TEST(motorTests, testNegativeMovement) {
    MotorSimulator motor;
    float position = motor.step(-100.0f, 0.001f);
    EXPECT_LT(position, 0.0f);
}

TEST(motorTests, testNoMovement) {
    MotorSimulator motor;
    float position = motor.step(0.0f, 0.001f);
    EXPECT_FLOAT_EQ(position, 0.0f);
}