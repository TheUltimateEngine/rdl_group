#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

class BaseController(object):
    def __init__(self):
        # subscription in order to get rotational speed from teleop twist keyboard
        rospy.Subscriber("cmd_vel", Twist, self.callback)
        # publications to motor controllers
        self.base_controller_pub_vl = rospy.Publisher('turtlebot3_burger/wheel_left_joint_controller/command', Float64, queue_size=1)
        self.base_controller_pub_vr = rospy.Publisher('turtlebot3_burger/wheel_right_joint_controller/command', Float64, queue_size=1)

    def callback(self, msg):
        '''
        This callback gets triggered every time a /cmd_vel msg is received
        '''

        # get robot constants and assign them to variables in order to work with them
        wheel_base = rospy.get_param('~distance_between_wheels')
        wheel_diameter = rospy.get_param('~wheel_diameter')

        # calculate velocity for each wheel and assign them to variables as well
        vl = Float64()
        vl.data = (msg.linear.x - msg.angular.z * (wheel_base / 2)) * (2 / wheel_diameter)
        vr = Float64()
        vr.data = (msg.linear.x + msg.angular.z * (wheel_base / 2)) * (2 / wheel_diameter)

        # publish speed values to motor controllers
        self.base_controller_pub_vl.publish(vl)
        self.base_controller_pub_vr.publish(vr)

    def start_base_controller(self):
        # wait for ctrl + c, prevent the node from dying (to allow callbacks to be received)
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('base_controller', anonymous=True)
    base_controller = BaseController()
    base_controller.start_base_controller()
