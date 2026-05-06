#include <pybind11/pybind11.h>
#include "arm.hpp"

namespace py = pybind11;

PYBIND11_MODULE(arm_sim, m) {
    py::class_<Arm>(m, "Arm")
        .def(py::init<>())
        .def("addJoint", &Arm::addJoint)
        .def("removeJoint", &Arm::removeJoint)
        .def("setTarget", &Arm::setTarget)
        .def("getAngle", &Arm::getAngle)
        .def("step", &Arm::step);

    py::class_<Joint>(m, "Joint")
        .def(py::init<>());
}