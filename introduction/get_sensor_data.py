'''
In this exercise you need to know how to get sensor data.

* Task: get the current joint angle and temperature of joint HeadYaw

* Hint: The current sensor data of robot is stored in perception (class Perception in spark_agent.py)

'''

# add PYTHONPATH
import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'software_installation'))

from spark_agent import SparkAgent

class MyAgent(SparkAgent):
    def think(self, perception):
        angle = 0
        temperature = 0
        # YOUR CODE HERE
        # Get angle and temperature of joint HeadYaw ('hj1')
        angle = perception.joint['HeadYaw'] # angle
        temperature=perception.joint_temperature['HeadYaw'] # temperature
        
        # Print the results
        print('HeadYaw angle: ' + str(angle) + ' temperature: ' + str(temperature))
        
        return super(MyAgent, self).think(perception)

if '__main__' == __name__:
    agent = MyAgent()
    agent.run()
