#!/usr/bin/env python3

import sys
import argparse
from pprint import pprint as p
import yaml

def getusers_passwd(f):
    users = set()
    for l in f:
        fields = l.split(":")
        users.add(fields[0])
    return sorted(users)

if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description='get user list')
    parser.add_argument('passwd', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="passwd")
    args = parser.parse_args()
    users = getusers_passwd(args.passwd)
    for u in users:
        print(u)
