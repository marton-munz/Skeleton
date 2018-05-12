from setuptools import setup

exec(open('main/version.py').read())

setup(
    name='Skeleton',
    version=__version__,
    description='A simple utility for creating project skeleton for command line tools',
    url='https://github.com/marton-munz/Skeleton',
    author='Marton Munz',
    license= 'MIT',
    packages=['main'],
    scripts=['bin/Skeleton.py'],
    zip_safe=False
)
