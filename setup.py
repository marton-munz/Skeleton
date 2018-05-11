from setuptools import setup

setup(
    name='Skeleton',
    version='0.1.0',
    description='A simple utility for creating project skeleton for command line tools',
    url='https://github.com/marton-munz/Skeleton',
    author='Marton Munz',
    license= 'MIT',
    packages=['main'],
    scripts=['bin/Skeleton.py'],
    zip_safe=False
)
