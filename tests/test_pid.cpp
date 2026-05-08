#include <gtest/gtest.h>
#include "../src/pid_controller.hpp"

TEST(pidTests, testZeroOutput) {
    PIDController pid;
    float torque = pid.step(0.0f, 0.001f);
    EXPECT_FLOAT_EQ(torque, 0.0f);
}

TEST(pidTests, testPositiveOutput) {
    PIDController pid;
    float torque = pid.step(45.0f, 0.001f);
    EXPECT_GT(torque, 0.0f);
}

TEST(pidTests, testNegativeOutput) {
    PIDController pid;
    float torque = pid.step(-45.0f, 0.001f);
    EXPECT_LT(torque, 0.0f);
}