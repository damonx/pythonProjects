#!/usr/bin/env python3

import numpy as np
from io import StringIO
import io

file_like_string = StringIO("This is a \nmultiline string.\nreadline()should see\nmultiple lines of\ninput")
for i,line in enumerate(file_like_string):
    print("line %s: %s" % (i+1,line))


data = "1, abc , 2\n 3, xxx, 4"
#print(data)
"""
1, abc , 2
 3, xxx, 4
"""

#print(type(data))
"""
<class 'str'>
"""

#np.genfromtxt(StringIO(data), delimiter=",", autostrip=True)
# TypeError: Can't convert 'bytes' object to str implicitly

print('\n')
print(np.genfromtxt(io.BytesIO(data.encode()), delimiter=",", dtype="|S3", autostrip=True))
"""
[[b'1' b'abc' b'2']
 [b'3' b'xxx' b'4']]
"""

print('\n')
print(np.genfromtxt(io.BytesIO(data.encode()), delimiter=",", autostrip=True))
"""
[[  1.  nan   2.]
 [  3.  nan   4.]]
"""
