#!/usr/bin/env python
import subprocess

uname = 'uname'
uname_arg = '-a'

print("Gathering system information with %s command: \n" % uname)
subprocess.call([uname,uname_arg])

diskspace = 'df'
diskspace_arg = '-h'
print("Gathering diskspace information with %s command: \n" % diskspace)
subprocess.call([diskspace,diskspace_arg])