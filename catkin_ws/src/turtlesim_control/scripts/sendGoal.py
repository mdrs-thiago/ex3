#!/usr/bin/env python 

import rospy
from geometry_msgs.msg import Twist,Pose2D
import angles
import math as m
from turtlesim.msg import Pose
import random
import time

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
  rospy.init_node('sendGoal', anonymous=True)
  pub= rospy.Publisher('/goal', Pose2D, queue_size=10)
  rospy.Subscriber("/turtle1/pose", Pose, callback_pose)
  Xg = random.uniform(0,8)
  Yg = random.uniform(0,8)
  newGoal = Pose2D()
  newGoal.x = Xg
  newGoal.y = Yg
  r=rospy.Rate(10)# ROS rate 10Hz
 
  #ros running
  while not rospy.is_shutdown():
    pub.publish(newGoal)
    Dist=m.sqrt((Xg-Xp)**2+(Yg-Yp)**2) #calculate Distance 
    print(Dist)
    if Dist < 0.1:
      Xg = random.uniform(0,8)
      Yg = random.uniform(0,8)
      newGoal.x = Xg 
      newGoal.y = Yg
      print('----------')
      print(newGoal)
      print('----------')
      pub.publish(newGoal)

  r.sleep() # so the CPU dont reach 100%
    


if __name__ == '__main__':
  main()
