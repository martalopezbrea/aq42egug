from distutils.core import setup
from setuptools import find_packages

setup(name='aq42egug',
    version='0.1',
    author='DSSS',
    author_email='name@fau.de',
    packages=find_packages(),
    install_requires=['numpy', 'Pillow', 'ipywidgets'])
