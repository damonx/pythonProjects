#!/usr/bin/env python3
"""
USAGE:
apache_log_parser_split.py some_log_file
This script takes one command line argument: the name of a log file to parse.
It then parses the log file and generates a report which associates remote
hosts with number of bytes transferred to them.

"""

import sys
def dictify_logline(line):
    split_line = line.split()
    return {'remote_host': split_line[0], 'status': split_line[8], 'bytes_sent':split_line[9]}

def generate_log_report(logfile):
    report_dict = {}
    for line in logfile:
        line_dict = dictify_logline(line)
        print(line_dict)
        try:
            bytes_sent = int(line_dict['bytes_sent'])
        except ValueError:
            continue
        report_dict.setdefault(line_dict['remote_host'],[]).append(bytes_sent)

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print(__doc__)
        sys.exit(1)

    infile_name = sys.argv[1]
    try:
        infile = open(infile_name, 'r')
    except IOError:
        print("You must specify a valid file to parse")
        print(__doc__)
        sys.exit(1)

    log_report = generate_log_report(infile)
    print(log_report)
    infile.close()
