#!env/bin/python

import sys
import toplevel


def start_cli():

    # Version
    version = '0.1.0'

    if len(sys.argv) == 1:
        print '\nUsage: skeleton <project-name>\n'
        quit()

    toplevel.run(version, sys.argv[1])

