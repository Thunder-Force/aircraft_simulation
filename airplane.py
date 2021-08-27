import vedo as vd
import numpy as np

vd.settings.useDepthPeeling = True

# vedo.shapes.Box(pos=(0, 0, 0), length=1, width=2, height=3, size=(), c='g4', alpha=1)
world = vd.Box([0,0,0], 100, 50, 30).wireframe()

#plane1 = vd.Mesh(vd.dataurl+"cessna.vtk").c("Blue").addTrail().addShadow(z=-4)
plane = vd.Mesh("f15.obj").rotateY(90)
plane1 = plane.c("Grey").addTrail().addShadow(z=-4)
plane2 = plane1.clone().c("Black") 

# Setup the scene
vd.show(world, plane1, plane2, axes=1, viewup="z", interactive=0, title='SNC Aircraft Demo')

for t in np.arange(0, 5.1, 0.01):
    plane1.pos(20*t-15, 8-t, vd.sin(3-t)).rotateX(0+t) 
    plane2.pos(16*t-15, t-2, vd.sin(t-3)).rotateX(2-t) 
    plotter = vd.show(world, plane1, plane2)
    if plotter.escaped: break  # if ESC button is hit during the loop

vd.interactive().close()
