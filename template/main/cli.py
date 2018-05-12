#!env/bin/python

from optparse import OptionParser
import toplevel
from .version import __version__


def start_cli():

    parser = OptionParser(
        description='[Project] v{}'.format(__version__),
        usage='[Project]/[project] <options>',
        version=__version__
    )

    parser.add_option( '-i', '--input', default=None, dest='input', action='store', help="Input file")
    (options, args) = parser.parse_args()

    toplevel.run(options)