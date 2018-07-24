# 
# This script edits the minisat sources in-place, 
# does not keep old versions as the changes are expected to be small

# Run as python import-orig-dist.py from extsrc/minisat22 directory.
#
# Note: this is a stripped-down version of minisat-gh/import-orig-dist.py -- the
# latter makes more modifications, so look there first if you need anything else.
#
# (c) 2018, Hari Govind
#

from __future__ import print_function
import os
import glob
import shutil
import fileinput

# substitutions map
smap = {
    'namespace Minisat' : 'namespace muser_Minisat',  #change namespace
    'Minisat::' : 'muser_Minisat::',  #change function calls
    'sort(learnts, reduceDB_lt(ca));' : 'sort(learnts, muser_Minisat::reduceDB_lt(ca));' #correct function call
}
# wrapper map
wmap = {
    'struct reduceDB_lt' : 'namespace muser_Minisat'
}
# list of subdirectories
subdirs = [ 'core', 'simp', 'utils', 'mtl', 'incr' ]

# 1. modify files
print("Making global modifications ...")
for d in subdirs:
    for f in glob.glob(d + '/*.*'):
        print("  "+f)
        for line in fileinput.input(f, inplace=True):
            for (s1,s2) in smap.iteritems():
                line = line.replace(s1, s2)
            print(line, end='')
# 2. wrapping things in namespaces
print("wrapping in namespaces")
for d in subdirs:
    for f in glob.glob(d + '/*.*'):
        print("  "+f)
        for (s1,s2) in wmap.iteritems():
                inside=False
                matchFound=False
                count=0
                for line in fileinput.input(f, inplace=True):
                        if s1 in line and not inside:
                            inside=True
                            print(s2+" {",end='\n')
                        if inside and "{" in line and not line.lstrip().startswith('//'):
                            count=count+line.count("{")
                        if inside and "}" in line and not line.lstrip().startswith('//'):
                            count=count-line.count("}")
                            if count==0:
				                print(line)
				                matchFound=True
                                print("}",end='')
                                inside=False
                        if not matchFound:
				            print(line, end='')
                        matchFound=False
