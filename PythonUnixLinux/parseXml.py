#!/usr/bin/env python3

from xml.etree import ElementTree as ET

if __name__ == '__main__':
    infile = 'tomcat-users.xml'
    tomcat_users = ET.parse(infile)
    for user in [e for e in tomcat_users.findall('./user') if e.get('name') == 'tomcat']:
        print(user.attrib)
