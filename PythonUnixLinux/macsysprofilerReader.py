#!/usr/bin/env python3
import sys

from xml.etree import ElementTree as ET

e = ET.parse('system_profiler.xml')

if __name__ == '__main__':
    for d in e.findall('/array/dict'):
        if d.find('string').text == 'SPSoftwareDateType':
            sp_data = d.find('array').find('dict')
            break
    else:
        print "SPSoftwareDataType NOT FOUND"
        sys.exit(1)

    record = []
    for child in sp_data.getchildren():
        record.append(child.text)
        if child.tag == 'string':
            print("%-15s -> %s" % tuple(record))
            record = []
