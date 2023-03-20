#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def publish_even_numbers():
    # Создание пространства имен (namespace)
    pub = rospy.Publisher('even_numbers', Int32, queue_size=10)
    
    pub_new = rospy.Publisher('new_even_numbers', Int32, queue_size=10)
    rospy.init_node('even_numbers_publisher', anonymous=False)
    rate = rospy.Rate(10) # 10Hz
    num = 0 
    
    while not rospy.is_shutdown():
    	
        if num % 2 == 0:
            pub.publish(num)
        num += 1
        if num == 101:
            num = 0
            pub_new.publish(num)
        rate.sleep()


   

if __name__ == '__main__':
    try:
        publish_even_numbers()
    except rospy.ROSInterruptException:
        pass
