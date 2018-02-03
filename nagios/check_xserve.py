#!/usr/bin/env python
"""
check_xserve.py

Created by Tim Wilson <wilson@visi.com> on 2008-01-02.
Copyright (c) 2008. This software is in the public domain.

The script requires a licensed copy of Hardware Monitor from Marcel Bresink. See
http://www.bresink.com/osx/HardwareMonitor.html for further information about Hardware
Monitor and to order a license. In addition to the Hardware Monitor GUI, there is a 
command line version included which is called 'hwmonitor'. This script uses hwmonitor
to retrieve values from the hardware sensors.

You will need to set the value of HWMONITORPATH below to the full path to the 
hwmonitor executable.

Typical usage:

$ ./check_xserve -s "CPU Core 1" -w 70 -c 90
SENSOR OK: CPU Core 1: 60 C|temperature=60.0;70.0;90.0;0;

Run 'hwmonitor' with no command line options for a complete list of sensors and their current
values. Then pick one of the sensors to run check_xserve against.
"""

HWMONITORPATH = "/Applications/Utilities/HardwareMonitor.app/Contents/Resources/hwmonitor"

from optparse import OptionParser
import os
import sys

def main():
    usage = "%prog -s <sensor name> -w <value> -c <value> [-t tempunit]"
    parser = OptionParser(usage, version="%prog 1.0")
    parser.set_defaults(tempunit="C")
    parser.add_option("-s", "--sensor", dest="sensorName",
                      help="Check the value of the given sensor.")
    parser.add_option("-w", "--warning", type="float", dest="warningvalue",
                      help="Generate warning state if sensor reading is above this value.")
    parser.add_option("-c", "--critical", type="float", dest="criticalvalue",
                      help="Generate critical state if sensor reading is above this value.")
    parser.add_option("-u", "--unit", dest="tempunit", type="choice", 
                      choices=["C", "F", "K"],
                      help="Set the temperature units to use. Choices are C, F, or K. The default is C.")
    (options, args) = parser.parse_args()
    
    # Now let's grab the output from hwmonitor
    try:
        if options.tempunit != "C":  # Need to pass the temp parameter to hwmonitor if it's not C
            cmdoutput = [line.strip() for line in 
                         os.popen(HWMONITORPATH + " -%s" % options.tempunit.lower()).readlines()]
        else:
            cmdoutput = [line.strip() for line in os.popen(HWMONITORPATH).readlines()]
    except:
        return 4
    sensorDict = {}
    for i in cmdoutput:
        sensor, reading = i.split(':')
        sensorDict[sensor] = reading.strip()
        
    # Retrieve and parse the sensor output.
    try:
        sensorValue = sensorDict[options.sensorName]
    except KeyError:
        print "No sensor '%s'" % options.sensorName
        return 4
    bareSensorValue = float(sensorValue.split()[0]) # get the numeric value without any units
    sensorValueUnits = sensorValue.split()[-1]
    
    # Assemble the performance data section of the check script output.
    labelDict = {'C': 'temperature', 'F': 'temperature', 'K': 'tempertuare',
                 'RPM': 'rpms', 'A': 'amps', 'V': 'volts', 'mAh': 'mAh', 'W': 'watts'}
    try:
        sensorLabel = labelDict[sensorValueUnits]
    except KeyError:
        sensorLabel = "value"
    perfData = "%s=%s;%s;%s;0;" % (sensorLabel, bareSensorValue, options.warningvalue,
                                   options.criticalvalue)
    
    # Compare the sensor output to the warning and critical levels.
    if bareSensorValue >= options.criticalvalue:
        print "SENSOR CRITICAL: %s: %s|%s" % (options.sensorName, sensorValue, perfData)
        return 2
    elif bareSensorValue >= options.warningvalue:
        print "SENSOR WARNING: %s: %s|%s" % (options.sensorName, sensorValue, perfData)
        return 1
    else:
        print "SENSOR OK: %s: %s|%s" % (options.sensorName, sensorValue, perfData)
        return 0

if __name__ == '__main__':
    sys.exit(main())