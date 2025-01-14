#!/usr/bin/env python

# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from geometry_msgs.msg import Twist, Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *
import actionlib
import rospy


class Rotator():
    def __init__(self):
        self._cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    def move_forward(self):
        keepGoing = 0

        self.twist = Twist()

        r = rospy.Rate(10)
        while not rospy.is_shutdown(): 
            if not keepGoing > 3:
                self.twist.angular.z = 0.6
            elif not keepGoing > 16:
                self.twist.linear.x = 0.4
                self.twist.angular.z = 0.0
            elif keepGoing >= 16:
                self.twist.linear.x = 0.0

            rospy.loginfo('Moving robot: %s', self.twist)
            r.sleep()
            self._cmd_pub.publish(self.twist)
            keepGoing += 1
                  


def main():
    rospy.init_node('rotate')
    try:
        mover = Rotator()
        mover.move_forward()
    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':
    main()
