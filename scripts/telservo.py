#!/usr/bin/env python


import rospy
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('command', Float64, queue_size=5)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        hello_str = 1
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        hello_str = 0
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
