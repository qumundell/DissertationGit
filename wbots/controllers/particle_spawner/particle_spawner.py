"""particle_spawner controller."""

from controller import Supervisor

# create the Supervisor
supervisor = Supervisor()

# get the time step of the current world.
timestep = int(supervisor.getBasicTimeStep())

particle_node = """
    Solid {
  translation %f %f %f
  children [
    Shape {
      geometry DEF PARTICLE_GEOMETRY Sphere {
        radius 0.01
      }
    }
  ]
  name "Water Particle"
  immersionProperties [
    ImmersionProperties {
      fluidName "fluid"
    }
  ]
  boundingObject USE PARTICLE_GEOMETRY
  physics Physics {
  }
}


"""

# Fill a 3x3x3 grid of particles
spacing = 0.012
origin = [2.0, 0.4, 0.82]  

root = supervisor.getRoot()
children = root.getField("children")
for i in range(3):
    for j in range(3):
        for k in range(3):
            x = origin[0] + i * spacing
            y = origin[1] + j * spacing
            z = origin[2] + k * spacing
            children.importMFNodeFromString(-1, particle_node % (x, y, z))

# Main loop:
# - perform simulation steps until Webots is stopping the controller
#while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    #pass

# Enter here exit cleanup code.
