#!env/bin/python

from optparse import OptionParser
from [project] import main

# Version
_version = '0.1.0'

# Command line argument parsing
descr = '[Project] v'+_version
parser = OptionParser(usage='[Project]-{}/env/bin/[project] <options>'.format(_version), version=_version, description=descr)
parser.add_option('-i', '--input', default=None, dest='input', action='store', help="Input file")
(options, args) = parser.parse_args()

main.run()