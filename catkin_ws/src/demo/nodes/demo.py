#!/usr/bin/env python
import rospy
import rostest
import unittest
import sys
import time
from std_msgs.msg import Duration

__author__ = ''

PKG = 'demo'
NAME = 'lap_time_test'

class TesterClass(unittest.TestCase):
    
    def __init__(self, *args):
        self.message_received = False
        self.message_received_raw = None
        rospy.init_node(NAME, anonymous=True)
        super(TesterClass, self).__init__(*args)

    def test_passed(self): # test names must start with 'test_'
        sub = rospy.Subscriber('/lap_time', Duration, self.callback)

        while not self.message_received:
            time.sleep(0.1)

        self.assertTrue(rospy.Duration(30) > self.message_received_raw)

    def callback(self, msg):
        self.message_received = True
        self.message_received_raw = msg.data

if __name__ == '__main__':
  rostest.rosrun(PKG, NAME, TesterClass, sys.argv)
