"""panda_pick_place controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Keyboard

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

m1 = robot.getDevice('panda_joint1')
m2 = robot.getDevice('panda_joint2')
m3 = robot.getDevice('panda_joint3')
m4 = robot.getDevice('panda_joint4')
m5 = robot.getDevice('panda_joint5')
m6 = robot.getDevice('panda_joint6')
m7 = robot.getDevice('panda_joint7')
gripper = robot.getDevice('panda_finger::right')


def pick_up():

    m4.setPosition(-2.5)
    m6.setPosition(2.86)
    m7.setPosition(2.45)
    gripper.setPosition(0.03)
    
    if robot.step(1500) == -1:
        return
    m2.setPosition(0.52)
    
    if robot.step(1500) == -1:
        return
    gripper.setPosition(0.011)
    
    if robot.step(1200) == -1:
        return
    m2.setPosition(0.1)
    if robot.step(1000) == -1:
        return
    m4.setPosition(-2.1)
    
    if robot.step(1000) == -1:
        return
    m6.setPosition(2.1)
    m7.setPosition(1.4)
    if robot.step(1000) == -1:
        return
    m1.setVelocity(0.6)
    m1.setPosition(-1)
    
    if robot.step(3000) == -1:
        return
    m6.setPosition(2.2)
    m4.setPosition(-2.36)
        
    if robot.step(1000) == -1:
        return
        
    sausage_m1 = -1
    sausage_m2 = 0.1
    sausage_m3 = 0
    sausage_m4 = -2.36
    sausage_m5 = 0
    sausage_m6 = 2.2
    sausage_m7 = 1.4
        
    gripper.setPosition(0.03)
    
    if robot.step(1000) == -1:
        return
    
    m4.setPosition(-2.1)
    m6.setPosition(2.1)
    m1.setPosition(0)
        
    reset()

# close to original position
def reset():
    m1.setPosition(0)
    m2.setPosition(0)
    m3.setPosition(0)
    m4.setPosition(-1.8)
    m5.setPosition(-1.6)
    m6.setPosition(1.65)
    m7.setPosition(0.8)
    gripper.setPosition(0)
    


while True:

    print("Pick up items--> SHIFT+D")
    print("Reset Panda --> SHIFT+R")

    timestep = int(robot.getBasicTimeStep())
    keyboard = Keyboard()
    keyboard.enable(timestep)

    while robot.step(timestep) != -1:

        key = keyboard.getKey()

        if key == Keyboard.SHIFT + ord('D'):
            print("Picking up items")
            pick_up()
            
            
        elif key == Keyboard.SHIFT + ord('R'):
            reset()


