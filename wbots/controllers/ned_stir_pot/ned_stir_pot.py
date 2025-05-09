"""ned_stir_pot controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
# from controller import VacuumGripper

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

m1 = robot.getDevice('joint_1')
m2 = robot.getDevice('joint_2')
m3 = robot.getDevice('joint_3')
m4 = robot.getDevice('joint_4')
m5 = robot.getDevice('joint_5')
m6 = robot.getDevice('joint_6')
m7 = robot.getDevice('gripper::left')
# vgrip = robot.getDevice('vacuum gripper')

m1.setPosition(0)
m2.setPosition(0)
m3.setPosition(0)
m4.setPosition(0)
m5.setPosition(0)
m6.setPosition(0)
m7.setPosition(0)
# if vgrip.isOn():
    # vgrip.turnOff()
    # print("turnin off")

m1.setVelocity(1)
m2.setVelocity(1)
m3.setVelocity(1)
m4.setVelocity(1)
m5.setVelocity(1)
m6.setVelocity(1)
m7.setVelocity(1)

def pick_up_stir():
    # vgrip.enablePresence(10000)
    
    if robot.step(1500) == -1:
        return
    m1.setPosition(-0.75)
    m2.setPosition(0.8)
    m7.setPosition(0.01)   
    if robot.step(500) == -1:
        return
    # vgrip.turnOn()    
    if robot.step(1000) == -1:
        return
    
    m3.setPosition(0.487)
    m5.setPosition(1)
    
    
    if robot.step(1500) == -1:
        return
        
    # if possible, switch to vacuumGripper cause this is so much better probably
    m7.setPosition(-0.01)
    if robot.step(1500) == -1:
        return
    # vgrip.enablePresence(timestep)
    # while robot.step(timestep) != -1:
        # if vgrip.isOn():
            # print("still on")
        # print(vgrip.getPresence())
        # if vgrip.getPresence() == True:
            # break
        
            
        
        # pass
    
    
    # print(vgrip.getPresence())
        
    m2.setPosition(0)
    # if vgrip.isOn():
        # print("still on")
   
pick_up_stir()
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
