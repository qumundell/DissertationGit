"""tiago_stirring controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

names = ["torso_lift_joint",
                                "arm_1_joint",
                                "arm_2_joint",
                                "arm_3_joint",
                                "arm_4_joint",
                                "arm_5_joint",
                                "arm_6_joint",
                                "arm_7_joint",
                                "wheel_left_joint",
                                "wheel_right_joint"]
                                
init_positions = [0, 0, 0, 0, 0, 0, 0, 0, float('inf'), float('inf')]

parts = []

for i in range(len(names)):
    parts.append(robot.getDevice(names[i]))
    
    
def stir_loop():
    # starting positions:
    # 0 -> 0.07,
    # 1 -> 0.77,
    # 3 -> -1.507,
    # 4 -> 1.5,
    # 7 -> -1.035
    
    # start with 4 points that go from a vague corner to corner
    
    parts[1].setPosition(0.8)
    parts[4].setPosition(1.67)
    print("movement1")
    
    if robot.step(1500) == -1:
        return
        
    parts[1].setPosition(0.5)
    parts[4].setPosition(1.9)    
    print("movement2")
    
    if robot.step(1500) == -1:
        return
        
    parts[4].setPosition(1.74)    
    print("movement3")
    
    if robot.step(1000) == -1:
        return
        
    parts[1].setPosition(0.7)
    parts[4].setPosition(1.55)      
    print("movement4")
        
    if robot.step(1000) == -1:
        return
        
    parts[1].setPosition(0.77)
    parts[4].setPosition(1.5)
    print("movement5")
    if robot.step(1500) == -1:
         return
    
    
   
def start_position():
    parts[0].setVelocity(0.07)
    parts[0].setPosition(0.35)
            
    parts[3].setPosition(-1.507)
        
    if robot.step(6000) == -1:
        return
    parts[1].setVelocity(0.6)
    parts[1].setPosition(0.77)
    parts[4].setPosition(1.5)
    # parts[1].setPosition(1.55)
    
    if robot.step(3000) == -1:
        return
    parts[7].setPosition(-1.035)
    if robot.step(1500) == -1:
        return
    
    
# Main loop:
# - perform simulation steps until Webots is stopping the controller
start_position()

parts[1].setVelocity(0.25)
parts[4].setVelocity(0.25)
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    stir_loop()
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
