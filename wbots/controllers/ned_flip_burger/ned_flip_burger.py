"""ned_flip_burger controller."""

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

m1 = robot.getDevice('joint_1')
m2 = robot.getDevice('joint_2')
m3 = robot.getDevice('joint_3')
m4 = robot.getDevice('joint_4')
m5 = robot.getDevice('joint_5')
m6 = robot.getDevice('joint_6')
m7 = robot.getDevice('gripper::left')

# Initial movements/actions:
m1.setPosition(0)
m2.setPosition(0)
m3.setPosition(0)
m4.setPosition(0)
m5.setPosition(0)
m6.setPosition(0)
m7.setPosition(0)

m1.setVelocity(1)
m2.setVelocity(1)
m3.setVelocity(1)
m4.setVelocity(1)
m5.setVelocity(1)
m6.setVelocity(1)
m7.setVelocity(1)

def flip():
    m7.setPosition(0.01)
    m1.setPosition(0.15)
    
    if robot.step(1000) == -1:
        return
        
    m2.setPosition(0.8)
    
    m5.setPosition(0.7)
    m6.setPosition(1.5708)
    
    if robot.step(1500) == -1:
        return
        
    m3.setPosition(0.3)
    
    if robot.step(1000) == -1:
        return
    
    m1.setPosition(-0.1)
    
    if robot.step(1000) == -1:
        return
    
    m7.setPosition(0)
    
    if robot.step(1000) == -1:
        return
    
    m2.setPosition(0.4)
    m6.setPosition(-1.5708)
    
    if robot.step(1500) == -1:
        return


while True:

    print("------------COMMANDS--------------")
    print("Flip the Burger --> SHIFT+F")
    print("Move joint_1 --> SHIFT+A or SHIFT+Z")
    print("Move joint_2 --> SHIFT+Q or SHIFT+S")
    print("Move joint_3 --> SHIFT+W or SHIFT+X")
    print("Move joint_4 --> SHIFT+Y or SHIFT+U")
    print("Move joint_5 --> SHIFT+H or SHIFT+J")
    print("Move joint_6 --> SHIFT+B or SHIFT+N")
    print("Open/Close Gripper --> SHIFT+L or SHIFT+M")
    print("----------------------------------")

    timestep = int(robot.getBasicTimeStep())
    keyboard = Keyboard()
    keyboard.enable(timestep)

    while robot.step(timestep) != -1:

        key = keyboard.getKey()

        if key == Keyboard.SHIFT + ord('A'):
            print("Move --> joint_1 left")
            m1.setPosition(-1.5)

        elif key == Keyboard.SHIFT + ord('Z'):
            print("Move --> joint_1 right")
            m1.setPosition(1.5)

        elif key == Keyboard.SHIFT + ord('Q'):
            print("Move --> joint_2 left")
            m2.setPosition(0.5)

        elif key == Keyboard.SHIFT + ord('S'):
            print("Move --> joint_2 right")
            m2.setPosition(-0.5)

        elif key == Keyboard.SHIFT + ord('W'):
            print("Move --> joint_3 left")
            m3.setPosition(0.5)

        elif key == Keyboard.SHIFT + ord('X'):
            print("Move --> joint_3 right")
            m3.setPosition(-0.5)

        elif key == Keyboard.SHIFT + ord('Y'):
            print("Move --> joint_4 left")
            m4.setPosition(1)

        elif key == Keyboard.SHIFT + ord('U'):
            print("Move --> joint_4 right")
            m4.setPosition(-1)

        elif key == Keyboard.SHIFT + ord('H'):
            print("Move --> joint_5 left")
            m5.setPosition(1.4)

        elif key == Keyboard.SHIFT + ord('J'):
            print("Move --> joint_5 right")
            m5.setPosition(-1.4)

        elif key == Keyboard.SHIFT + ord('B'):
            print("Move --> joint_6 left")
            m6.setPosition(1.5)

        elif key == Keyboard.SHIFT + ord('N'):
            print("Move --> joint_6 right")
            m6.setPosition(-1.5)

        elif key == Keyboard.SHIFT + ord('L'):
            print("Move --> Open Gripper")
            m7.setPosition(0.01)

        elif key == Keyboard.SHIFT + ord('M'):
            print("Move --> Close Gripper")
            m7.setPosition(0)
        
        elif key == Keyboard.SHIFT + ord('F'):
            print("Flipping burg")
            flip()


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
