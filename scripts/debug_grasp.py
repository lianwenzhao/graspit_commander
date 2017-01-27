#!/usr/bin/env python
from geometry_msgs.msg import Pose
from graspit_commander import GraspitCommander as gc
import sys
import time

if __name__ == '__main__':
    assert len(sys.argv) <=8, "length is larger than 7!"
    pose = Pose()
    
    if len(sys.argv)<8:
	values = raw_input('Pose:')
	values_float = map(float, values.split())
	assert len(values_float) == 7, "length is not 7!"
    else:
        values_float = []
        for i in range(1,8):
	    values_float.append(float(sys.argv[i]))

    pose.position.x = values_float[0]
    pose.position.y = values_float[1]
    pose.position.z = values_float[2]
    pose.orientation.w = values_float[3]
    pose.orientation.x = values_float[4]
    pose.orientation.y = values_float[5]
    pose.orientation.z = values_float[6]

    gc.setRobotPose(pose)

    time.sleep(1)
    gc.autoGrasp()

