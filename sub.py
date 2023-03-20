#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def subscriber_callback(msg):
    rospy.loginfo('Received even number:{}'.format(msg.data))

def subscribe_even_numbers():
    rospy.init_node('even_numbers_subscriber', anonymous=False)
    rospy.Subscriber('even_numbers', Int32, subscriber_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscribe_even_numbers()
    except rospy.ROSInterruptException:
        pass
