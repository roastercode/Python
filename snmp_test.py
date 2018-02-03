#!/usr/bin/env python
''' snmp test
test things in python arround the snmp library '''


#import string
#import re
import sys
import pysnmp
#import socket
#import pysnmp
#from pysnmp import *


def getline():
    ''' read line from sys  '''
    return sys.stdin.readline().strip()


def output(line):
    ''' print the output '''
    sys.stdout.write(line + "\n")
    sys.stdout.flush()

    def main():
        ''' print line definition '''
        logger.info("starting pass_persist daemon")

        try:
            while True:
                command = getline()

            if command == "":
                logger.info("stopping pass_persist daemon")
                sys.exit(0)

              # snmpd 5.4.2.1 sends a PING before every snmp command
            elif command == "PING":
                output("PONG")

            elif command == "set":
                oid = getline()
                type_and_value = getline()
                logger.info("%s %s %s" % (command, oid, type_and_value))
                #snmp_set(oid, type_and_value)
                # set not supported yet...
                output("not-writable")

            elif command == "get":
                oid = getline()
                logger.info("%s %s" % (command, oid))
                snmp_get(oid)

            elif command == "getnext":
                oid = getline()
                logger.info("%s %s" % (command, oid))
                snmp_getnext(oid)

            else:
                logger.error("Unknown command: %s" % command)

# If we get an exception, spit it out to the log then quit
# (by propagating exception).
# snmpd will restart the script on the next request.
        except Exception, e:
            logger.exception("")
        raise
