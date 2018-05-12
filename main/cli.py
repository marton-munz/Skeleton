#!env/bin/python

import sys
import toplevel

def start_cli():

    if len(sys.argv) == 1:
        print '\nUsage: skeleton <project-name>\n'
        quit()

    toplevel.run(sys.argv[1])

