#!env/bin/python

from optparse import OptionParser
import toplevel

def start_cli():

    # Version
    _version = '0.1.0'

    # Command line argument parsing
    descr = '[Project] v'+_version
    parser = OptionParser(usage='[Project]/[project] <options>'.format(_version), version=_version, description=descr)
    parser.add_option('-i', '--input', default=None, dest='input', action='store', help="Input file")
    (options, args) = parser.parse_args()

    toplevel.run()