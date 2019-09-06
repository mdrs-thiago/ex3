#!/usr/bin/env python 

import rospy
from geometry_msgs.msg import Twist,Pose2D
import angles
import math as m
from turtlesim.msg import Pose
import time

K=0.4 # linear speed Gain 
Kw=-2 #Angular speed Gain
Xg=0
Xp=0
Yg=0
Yp=0
Thetap=0


#=====================================================
def callback_goal(data): # associated with subscriber goal
   #gets X and Y from goal pose and store in X and Y global variables 
    global Xg,Yg

    Xg = data.x
    Yg = data.y
#======================================================
def callback_pose(data):  # associated with subscriber pose
    #gets X and Y from actual pose and store in X and Y global variables 
    global Xp,Yp,Thetap
    
    Xp = data.x
    Yp = data.y
    Thetap=data.theta
#==========================================================

def main():
  #init publisher
  rospy.init_node('talker', anonymous=True)
  pub= rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  rospy.Subscriber("/goal", Pose2D, callback_goal)
  rospy.Subscriber("/turtle1/pose", Pose, callback_pose)
  
  r=rospy.Rate(10)# ROS rate 10Hz
  #ros running
  time.sleep(1)
  while not rospy.is_shutdown():
    Dist=m.sqrt((Xg-Xp)**2+(Yg-Yp)**2) #calculate Distance 
    angle=m.atan2((Yg-Yp),(Xg-Xp)) # calculate angle
    anglep=angles.shortest_angular_distance(angle,Thetap) #
    print('Dist: ' + str(Dist))
    print('Angle: ' + str(anglep))
    vel=Twist() # associate Twist struct to vel 
    vel.linear.x=K*Dist # changing linear speed
    vel.angular.z=Kw*anglep # changing angular speed
    pub.publish(vel)  # publishing to turtlesim
    r.sleep() # so the CPU dont reach 100%
    


if __name__ == '__main__':
  main()
