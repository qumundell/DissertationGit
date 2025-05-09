"""particle_spawner controller."""

from controller import Supervisor

# create the Supervisor
supervisor = Supervisor()

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
spacing = 0.03
origin = [1.92, 0.3, 0.74]  

root = supervisor.getRoot()
children = root.getField("children")
for i in range(5):
    for j in range(5):
        for k in range(5):
            x = origin[0] + i * spacing
            y = origin[1] + j * spacing
            z = origin[2] + k * spacing
            children.importMFNodeFromString(-1, particle_node % (x, y, z))



