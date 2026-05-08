#include <pybind11/pybind11.h>
#include "arm.hpp"

namespace py = pybind11;

PYBIND11_MODULE(arm_sim, m) {
    py::enum_<Axis>(m, "Axis")
        .value("Horizontal", Axis::Horizontal)
        .value("Vertical", Axis::Vertical);

    py::class_<Joint>(m, "Joint")
        .def(py::init<>());

    py::class_<Arm>(m, "Arm")
        .def(py::init<>())
        .def("addJoint", &Arm::addJoint)
        .def("addNewJoint", &Arm::addNewJoint)
        .def("popJoint", &Arm::popJoint)
        .def("removeJoint", &Arm::removeJoint)
        .def("setTarget", &Arm::setTarget)
        .def("getTarget", &Arm::getTarget)
        .def("getAngle", &Arm::getAngle)
        .def("getAxis", &Arm::getAxis)
        .def("getLength", &Arm::getLength)
        .def("toggleAxis", &Arm::toggleAxis)
        .def("getJointCount", &Arm::getJointCount)
        .def("getKp", &Arm::getKp)
        .def("setKp", &Arm::setKp)
        .def("step", &Arm::step);
}