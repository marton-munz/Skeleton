from setuptools import setup

exec(open('main/version.py').read())

setup(
    name='[Project]',
    version=__version__,
    description='',
    url='...',
    author='...',
    author_email='...',
    licence='MIT',
    packages=['main'],
    scripts=['bin/[Project].py'],
    zip_safe=False
)
