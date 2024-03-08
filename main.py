import filters_with_pybind.operations
from filters_with_pybind import operations, stupid_module
from filters_with_pybind.operations import add

print(filters_with_pybind.operations.add(1, 2))


stupid_module.slow_add(1, 2)
print(add(1, 2))
print(operations.add(1, 2))
