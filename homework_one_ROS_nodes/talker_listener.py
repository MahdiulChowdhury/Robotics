#!/usr/bin/env python 
import rospy 
from std_msgs.msg import String 

class Talker(): 
	""" publish counts from 0 to 9 """ 
	def __init__(self):
		""" publisher """ 
		self.pub = rospy.Publisher('chatter', String, queue_size = 10) 
		self.count = 0 
	def updateCount (self): 
		#count from 0-9 
		self.count += 1 
		if self.count > 9: 
			self.count = 0
	def talk(self): 
		msg = String() 
		msg.data = 'Alien:come to Mars' 
		"""writing to console""" 
		rospy.loginfo(msg.data) 
		#publish 	
		self.pub.publish(msg.data)
class Listener: 
	""" this class will subscribe to topic "chatter" """ 
	def __init__(self): 
		"""subscribing to chatter topic and call the callback function""" 
		rospy.Subscriber('chatter', String,self.callback) 
	def callback(self, data):
		"""print the receive message on the console""" 
		rospy.loginfo('Human: invitation accepted,gracious --->>>%s', data.data)
def talker_listener(): 
	"""initializing the node""" 
	rospy.init_node('talker_listener', anonymous='True') 
	rate = rospy.Rate(1) 
	to = Talker() 
	lo = Listener() 

	while not rospy.is_shutdown():
		to.talk() 
		to.updateCount() 
		rate.sleep() 
		rospy.sleep(1) 
if __name__ == '__main__': 
	talker_listener()	















