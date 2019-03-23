#/usr/bin/python 
""" Referencce: ROS wiki """
import rospy
import math 
import numpy as np 
from geometry_msgs.msg import PoseStamped, Twist

def twist_to_speeds(linear,angular): 
    if angular >0: 
	left = (linear+angular)
	right = 0.0*(linear+angular) 
	return left, right
    else: 	
    	left = (linear+angular)
    	right = (linear - angular)
   	return left, right



'''if __name__ == '__main__':
    twist_to_speeds(0.5,-0.5) 
    twist_to_speeds(0.5,0.5)
'''

