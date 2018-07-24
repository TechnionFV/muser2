# 
# This script edits the minisat sources in-place, 
# does not keep old versions as the changes are expected to be small

# Run as python import-orig-dist.py from mus-2/ directory.
#
# Note: this is a stripped-down version of minisat-gh/import-orig-dist.py -- the
# latter makes more modifications, so look there first if you need anything else.
#
# (c) 2018, Hari Govind
#
#IMPORTANT : Modifies in place. No backup kept
from __future__ import print_function
import os
import glob
import shutil
import fileinput

# substitutions map
smap = {
    'namespace Minisat;' : 'namespace muser_Minisat;',  #change namespace
    'namespace Glucose;' : 'namespace muser_Glucose;',  #change namespace
    'Glucose::' : 'muser_Glucose::', #change function calls
    'Minisat::' : 'muser_Minisat::' #change function calls
}

# 1. modify files
print("Making global modifications ...")
for f in glob.glob('*.*'):
    print("  "+f)
    if 'import-orig-dist' in f :
    	continue
    for line in fileinput.input(f, inplace=True):
        for (s1,s2) in smap.iteritems():
            line = line.replace(s1, s2)
        print(line, end='')
