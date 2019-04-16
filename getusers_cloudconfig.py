#!/usr/bin/env python3

import sys
import os
import argparse
from pprint import pprint as p
import yaml
coreos_users = ['root','core','fleet','systemd-coredump','systemd-timesync']
ignored_users = '["arifumi","fujisaki","okd","kyokuheki","okuda"]'

def getusers_cloudconfig(f):
    ignored = coreos_users + yaml.load(os.getenv('IGNORED_USERS', ignored_users), Loader=yaml.FullLoader)
    cc = yaml.load(f, Loader=yaml.FullLoader)
    users = set([u['name'] for u in cc['users']] + ignored)
    return sorted(users)

if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description='get user list')
    parser.add_argument('cloudconfig', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input yaml file")
    args = parser.parse_args()
    users = getusers_cloudconfig(args.cloudconfig)
    for u in users:
        print(u)
