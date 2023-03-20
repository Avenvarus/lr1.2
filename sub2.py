#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo("We've got overflow here")

rospy.init_node('new_even_numbers_sub')
rospy.Subscriber('new_even_numbers', Int32, callback, queue_size=10)
rospy.spin()

if __name__ == '__main__':
    try:
        subscribe_even_numbers()
    except rospy.ROSInterruptException:
        pass
