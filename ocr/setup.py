from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("get_info_ticket.pyx")
)


#python setup.py build_ext --inplace
