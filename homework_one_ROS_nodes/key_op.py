#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, Twist
import me416_utilities as mu

class keyboard_operation(object):
    def __init__(self):

        self.publisher = rospy.Publisher('/robot_twist',Twist, queue_size = 10)
        self.SPEED_DELTA = 0.2 
        self.speed_linear = 0.0 
        self.speed_angular = 0.0 
        self.rate = rospy.Rate(50) 
        self.vel_msg = Twist()

    def operation(self): 
        print "'W': increment speed_linear"
        print "'S': decrement speed_linear" 
        print "'D': increment speed_angular" 
        print "'A': decrement speed_angular" 
        print "'Z': set speed_linear to zero" 
        print "'C': set speed_angular to zero" 
        print "'X': set both speed_linear and speed_angular to zero" 
        print "'Q': to quit" 
        
        #to call function which read from the keyboard 
        self.getch = mu._Getch() 

        #waiting in the loop for the keyboard press 
        while not rospy.is_shutdown(): 
            self.key = self.getch() 
            if self.key == 'W':
                if self.speed_linear + self.SPEED_DELTA > 1:
                    self.speed_linear = 1
                    self.speed_linear = self.speed_linear + self.SPEED_DELTA

                else: 
                    self.speed_linear = self.speed_linear + self.SPEED_DELTA 
                rospy.loginfo('Increment linear speed%f', self.speed_linear) 
                self.vel_msg.linear.x = self.speed_linear

            elif self.key == 'S': 
                if self.speed_linear - self.SPEED_DELTA < -1:
                    self.speed_linear = -1
                    self.speed_linear = self.speed_linear - self.SPEED_DELTA

                else:
                    self.speed_linear = self.speed_linear - self.SPEED_DELTA
                rospy.loginfo('Decrement linear speed%f', self.speed_linear)
                self.vel_msg.linear.x = self.speed_linear

            elif self.key == 'D':
                if self.speed_angular + self.SPEED_DELTA >1: 
                    self.speed_angular = 1
                    self.speed_angular = self.speed_angular + self.SPEED_DELTA

                else:
                    self.speed_angular = self.speed_angular + self.SPEED_DELTA
                rospy.loginfo('Increment speed_angular%f',self.speed_angular) 
                self.vel_msg.angular.z = self.speed_angular

            elif self.key == 'A':
                if self.speed_angular - self.SPEED_DELTA < -1:
                    self.speed_angular = -1
                    self.speed_angular = self.speed_angular - self.SPEED_DELTA

                else:
                    self.speed_angular = self.speed_angular - self.SPEED_DELTA
                rospy.loginfo('Decrement speed_angular%f',self.speed_angular)
                self.vel_msg.angular.z = self.speed_angular

            elif self.key == 'Z':
                self.speed_linear = 0.0
                rospy.loginfo('speed linear to 0%f',self.speed_linear)
                self.vel_msg.linear.x = self.speed_linear

            elif self.key == 'C':
                self.speed_angular = 0
                rospy.loginfo('speed angular to 0%f',self.speed_angular)
                self.vel_msg.angular.z = self.speed_angular

            elif self.key == 'X':
                self.speed_angular = 0
                self.speed_linear = 0 
                rospy.loginfo('speed_linear and speed_angular to 0%f, %f',self.speed_linear, self.speed_angular)
                self.vel_msg.linear.x = self.speed_linear
                self.vel_msg.angular.z = self.speed_angular
                
            elif self.key == 'Q': 
                rospy.loginfo('Shutdown Initiated') 
                #self.rospy.signal_shutdown('shutting down initiated by %s' %self.rospy.get_name())
                #rospy.signal_shutdown('Shutting down initiated') 
                rospy.signal_shutdown('Shutting down initiated by %s' % rospy.get_name())

            self.publisher.publish(self.vel_msg)    
            self.rate.sleep() 

        

if __name__ == '__main__': 
    rospy.init_node('Keyboard_opearatio', anonymous = True) 
    sm = keyboard_operation() 
    sm.operation() 
