#!/usr/bin/env python 

import rospy
from geometry_msgs.msg import Twist,Pose2D
import angles
import math as m
from turtlesim.msg import Pose
import random


Xp=0
Yp=0
Thetap=0

#======================================================
def callback_pose(data):  # associated with subscriber pose
    #gets X and Y from actual pose and store in X and Y global variables 
    global Xp,Yp
    
    Xp = data.x
    Yp = data.y

#==========================================================

def main():
  #init publisher
  rospy.init_node('sendGoal', anonymous=True)		#Our created node 
  pub= rospy.Publisher('/goal', Pose2D, queue_size=10)	#The node should publish to /goal
  rospy.Subscriber("/turtle1/pose", Pose, callback_pose)#And subscribe to turtle1/pose, in order to verify the distance. 
  Xg = random.uniform(0,8)				#First, we create a new int coordinate X.
  Yg = random.uniform(0,8)				#And a int coordinate Y.
  newGoal = Pose2D()					#The new goal type message is Pose2D(), so we create it.
  newGoal.x = Xg
  newGoal.y = Yg
  r=rospy.Rate(10)# ROS rate 10Hz
 
  #ros running
  while not rospy.is_shutdown():
    pub.publish(newGoal)				#We first publish the topic
    Dist=m.sqrt((Xg-Xp)**2+(Yg-Yp)**2) 			#Calculate distance 

    if Dist < 0.1:					#Check if the distance is close to actual goal position
      Xg = random.uniform(0,8)				#If so, create a new coordinate X 
      Yg = random.uniform(0,8)				#And a new coordinate Y to the goal position.
      newGoal.x = Xg 
      newGoal.y = Yg

      pub.publish(newGoal)				#Publish a new goal position and go back do the main loop

  r.sleep() # so the CPU dont reach 100%
    


if __name__ == '__main__':
  main()
