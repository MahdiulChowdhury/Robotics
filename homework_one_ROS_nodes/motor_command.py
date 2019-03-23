#!/usr/bin/python
import rospy
import motor_command_model as motor_speed
import me416_utilities as me416
from geometry_msgs.msg import PoseStamped, Twist
from me416_lab.msg import MotorSpeedsStamped

# Assign variable names to
class MotorSpeed(object):
    """A class to control motors using PWM on all channels of an H-bridge thorugh GPIO"""

    def __init__(self):
        #rospy.init_node('Motor_Control', anonymous = True)
        self.publisher = rospy.Publisher('/motor_speeds',MotorSpeedsStamped, queue_size = 10)
        self.subscriber = rospy.Subscriber('/robot_twist',Twist,self.callback)
        self.vel_msg = Twist()
        self.msg = MotorSpeedsStamped()
        self.motor_left = me416.MotorSpeedLeft()
        self.motor_right = me416.MotorSpeedRight(.8)
        self.right = 0
        self.left = 0
        print "Hello2"

    def callback(self,data):

        """ Linear Velocity in the x Axix """
        print "HELLO3"
        print "linear.x", data.linear.x
        print "angular.z", data.angular.z
        self.vel_msg = data
        self.left,self.right = motor_speed.twist_to_speeds(self.vel_msg.linear.x, self.vel_msg.angular.z)
        print self.left
        print self.right
        self.msg.header.stamp = rospy.Time.now()
        self.msg.left = self.left
        self.motor_left.set_speed(self.left)
        self.msg.right = self.right
        self.motor_right.set_speed(self.right)
        self.publisher.publish(self.msg)
        #print self.msg.left 
        #print self.msg.right 

    def run(self):
        self.rate = rospy.Rate(10)
        t0 = rospy.Time.now().to_sec()
        rospy.spin()
        return
        #The code below is dead code    



if __name__ == '__main__':
    rospy.init_node('Motor_Control', anonymous = True)
    print "Hello1"
    mov_rot = MotorSpeed()
    mov_rot.run()
