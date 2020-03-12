#!/usr/bin/env python

"""
setup.py file for SWIG example
"""
from setuptools import find_packages
from distutils.core import setup, Extension
import os


fastestrplidar_module = Extension('_fastestrplidar',
                                  sources=['fastestrplidar/fastestrplidar_wrap.cxx', 'fastestrplidar/fastestrplidar.cpp'],
                                  extra_objects=["fastestrplidar/librplidar_sdk.a"],
                                  extra_compile_args=['-lpthread', '-lstdc++'])

setup(name='fastestrplidar',
      version='0.1',
      author="Ayo Ayibiowu",
      description="""An Advanced but easy to use Fast Rplidar Library""",
      ext_modules=[fastestrplidar_module],
      py_modules=["fastestrplidar"],
      packages=['fastestrplidar'])


for file in os.listdir(os.getcwd()):
    if file.find('_fastestrplidar.cpython') >= 0:
        os.rename(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), '_fastestrplidar.so'))
        break
