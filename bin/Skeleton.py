#!env/bin/python
import sys
from skeleton_.main import run

ver = '0.1.0'

if len(sys.argv) == 1:
    print '\nUsage: skeleton <project-name>\n'
    quit()

run(ver, sys.argv[1])