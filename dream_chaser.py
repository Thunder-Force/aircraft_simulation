import vedo as vd
import numpy as np

vd.settings.useDepthPeeling = False

# vedo.shapes.Box(pos=(0, 0, 0), length=1, width=2, height=3, size=(), c='g4', alpha=1)
world = vd.Box([0,0,0], 100, 50, 30).wireframe()

#plane1 = vd.Mesh(vd.dataurl+"cessna.vtk").c("Blue").addTrail().addShadow(z=-4)
dream_chaser = vd.Mesh("dream_chaser.obj").rotateX(90).rotateZ(-90)
dream_chaser.addTrail().addShadow(z=-4).c("lightgray")

# Setup the scene
vd.show(world, dream_chaser, axes=1, viewup="z", interactive=0, title='SNC Aircraft Demo')

for t in np.arange(0, 5.1, 0.01):
    dream_chaser.pos(20*t-15, 8-t, vd.sin(3-t)) #.rotateX(0+t) 
    plotter = vd.show(world, dream_chaser)
    if plotter.escaped: break  # if ESC button is hit during the loop

vd.interactive().close()
