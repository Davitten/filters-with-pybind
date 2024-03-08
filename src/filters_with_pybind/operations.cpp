#include <pybind11/pybind11.h>

namespace py = pybind11;
using namespace pybind11::literals;

int add(int i, int j) { return i + j; }

int multiply(int i, int j) { return i * j; }

PYBIND11_MODULE(operations, m) {
  m.doc() = "pybind11 example plugin";
  m.def("add", &add, "A function that adds two numbers", "i"_a, "j"_a);
  m.def("multiply", &multiply, "A function that adds two numbers", "i"_a,
        "j"_a);
}
