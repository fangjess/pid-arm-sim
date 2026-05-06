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
        .def("popJoint", &Arm::popJoint)
        .def("removeJoint", &Arm::removeJoint)
        .def("setTarget", &Arm::setTarget)
        .def("getAngle", &Arm::getAngle)
        .def("getAxis", &Arm::getAxis)
        .def("getLength", &Arm::getLength)
        .def("step", &Arm::step);
}