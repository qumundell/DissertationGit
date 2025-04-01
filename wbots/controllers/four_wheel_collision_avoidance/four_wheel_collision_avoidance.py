"""four_wheel_collision_avoidance controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Motor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
MAX_SPEED = 6.28
TIME_STEP = 64

wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for name in wheelsNames:
    wheels.append(robot.getDevice(name))
   
leftSensor = robot.getDevice('ds_left')
leftSensor.enable(timestep)
rightSensor = robot.getDevice('ds_right')
rightSensor.enable(timestep)
    
speed = -1.5  # [rad/s]
# 
for wheel in wheels:
    wheel.setPosition(float('inf'))
    wheel.setVelocity(3)
    
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    leftObstacle = 0
    rightObstacle = 0
    leftSpeed = 3
    rightSpeed = 3
    
    leftVal = leftSensor.getValue()
    rightVal = rightSensor.getValue()
    
    if leftVal < 950:
        leftObstacle += 1
        
    if rightVal <950:
        rightObstacle +=1
        
    if leftObstacle > 0 and rightObstacle > 0:
        leftSpeed = 3
        rightSpeed = -3
        leftObstacle -= 1
        rightObstacle -= 1
    elif leftObstacle > 0:
        leftSpeed = 3
        rightSpeed = -3
        leftObstacle -= 1
    elif rightObstacle > 0:
        rightSpeed = 3
        leftSpeed = -3
        rightObstacle -= 1
    
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    
        

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
