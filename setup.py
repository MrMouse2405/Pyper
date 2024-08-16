from setuptools import setup
from Cython.Build import cythonize

# skip __init__.py, cuz it breaks cython
# but include all other files
setup(
    name="pyper",
    ext_modules = cythonize("src/*.py",annotate=True)
)