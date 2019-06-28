#!/usr/bin/env python3

import sys
import argparse
import json
#from pprint import pprint as p
from getusers_cloudconfig import getusers_cloudconfig
from getusers_passwd import getusers_passwd

def diff(f_cc, f_passwd):
    users_cc = set(getusers_cloudconfig(f_cc))
    users_passwd = set(getusers_passwd(f_passwd))
    print('cloudconfig: {}'.format(sorted(users_cc)), file=sys.stderr)
    print('passwd: {}'.format(sorted(users_passwd)), file=sys.stderr)
    invalid_users = users_passwd - users_cc
    tba_users = users_cc - users_passwd
    d = {
        'cloudconfig': sorted(users_cc),
        'passwd': sorted(users_passwd),
        'invalid': sorted(invalid_users),
        'tba': sorted(tba_users),
    }
    print('invalid: {}'.format(sorted(invalid_users)), file=sys.stderr)
    print('tba: {}'.format(sorted(tba_users)), file=sys.stderr)
    #p('{}'.format(d), stream=sys.stderr)
    jsonstr = json.dumps(d)
    print('{}'.format(jsonstr))

if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description='get user list')
    parser.add_argument('cloudconfig', nargs='?', type=argparse.FileType('r'), default="/config.yml", help="cloud-config.yml")
    parser.add_argument('passwd', nargs='?', type=argparse.FileType('r'), default="/passwd", help="passwd")
    args = parser.parse_args()
    diff(args.cloudconfig, args.passwd)
