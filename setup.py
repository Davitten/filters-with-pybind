from pybind11.setup_helpers import Pybind11Extension
from setuptools import setup

ext_modules = [
    Pybind11Extension(
        name="filters_with_pybind.operations",  # as it would be imported
        sources=["src/filters_with_pybind/operations.cpp"],
    ),
]

setup(ext_modules=ext_modules)
