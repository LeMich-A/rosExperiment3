#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal



# Callbacks definition

def active_cb():
    rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
    # rospy.loginfo("Current location: "+str(feedback))
    pass


def done_cb(status, result):
    if status == 3:
        rospy.loginfo("Goal reached")
    if status == 2 or status == 8:
        rospy.loginfo("Goal cancelled")
    if status == 4:
        rospy.loginfo("Goal aborted")
    

rospy.init_node('goal_pose')



def moveToPose(x, y, z, qx, qy, qz ,qw):
    # 7th intermediate pose
    global navclient
    global finished
    navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    navclient.wait_for_server()


    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = z
    goal.target_pose.pose.orientation.x = qx
    goal.target_pose.pose.orientation.y = qy
    goal.target_pose.pose.orientation.z = qz
    goal.target_pose.pose.orientation.w = qw

    navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    finished = navclient.wait_for_result()

    navclient.wait_for_server()

#   x: -0.4241108841070244
#       y: -4.971571840015072
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: -0.04233999405320077
#       w: 0.9991032603808152

rospy.loginfo("moving to point 1 \n")
moveToPose(-0.0969075442732294, 0.004687225388910832, 0, 0, 0, 0.02874481748424611, 0.9995867823594895)
rospy.loginfo("successfully moved to point 1 \n")




rospy.loginfo("moving to point 2 \n")
moveToPose( -3.0109805064389894, -0.04335539394753214, 0, 0, 0, -0.999325810301277, 0.036714096280532744)
rospy.loginfo("successfully moved to point 2 \n")



rospy.loginfo("moving to point 3 \n")
moveToPose( -5.915080538531674, -1.137882644113799, 0, 0, 0, -0.8081421057010983, 0.5889875524941038)
rospy.loginfo("successfully moved to point 3 \n")



rospy.loginfo("moving to point 4 \n")
moveToPose( -3.6622620881216603, -4.66856490671764, 0, 0, 0, 0.05294831624370281, 0.9985972540553859)
rospy.loginfo("successfully moved to point 4 \n")


rospy.loginfo("moving to point 5 \n")
moveToPose( -0.3200500258758859, -4.743481676439009, 0, 0, 0, -0.013055076917393143, 0.9999147788520184)
rospy.loginfo("successfully moved to point 5 \n")




if not finished:
    rospy.logerr("Action server not available!")
else:
    rospy.loginfo ( navclient.get_result())