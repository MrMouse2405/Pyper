from setuptools import setup
from Cython.Build import cythonize

setup(
    name="pyper",
    ext_modules = cythonize("Pyper/pyper.py",annotate=True)
)