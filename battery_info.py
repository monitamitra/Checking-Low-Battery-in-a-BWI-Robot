#!/usr/bin/env python3
import rospy
from slack import send_slack_message
from std_msgs.msg import String
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus, KeyValue
import socket

debug = True # just for testing purposes. will be set to false later
callOnce = True


def callback(data):
    global callOnce
    if callOnce == True:
        for i in range (0, len(data.status)):
            nameOfthis = data.status[i].name

            if nameOfthis == "voltage":
                volt = float(data.status[i].values[0].value)
                
                # if (volt <= 3.3 or debug == True) and callOnce == True:
                if volt <= 3.3 or debug == True:
                    rospy.loginfo(rospy.get_caller_id() + " I heard %s", volt)
                    hostname = socket.gethostname()
                    send_slack_message("Battery of " + hostname + " is low. Heading back to the AHG!")
                    callOnce = False
                    break

def listener():
    rospy.init_node('battery_info', anonymous=True)
    rospy.Subscriber("/diagnostics", DiagnosticArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()