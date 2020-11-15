#!/user/bin/env python
import rospy
from std_msgs.msg import String # import rospy to write a ROS node
def talker(): # I have change schnaker to takler. 
              # The funktion of this method is broadcasting a message like a talker.
    pub = rospy.Publisher('chatter', String, queue_size=8) # I have changed x to pub, pub is abbreviation of publishment. 
                                                           # I think that is easier to understand.
    rospy.init_node('talker', anonymous = True)
    rate = rospy.Rate(20) # I have changed repetitions to rate. 
                          # This name is short and represents the meaning of this methods.
    while not rospy.is_shutdown():
        hello_str = "Moin ROS! The timestamp is: %s" % rospy.get_time() # I have change foo to hello_str. 
                                                                        # That string refers to the function of string while foo is just a name.  
        pub.publish(foo)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass