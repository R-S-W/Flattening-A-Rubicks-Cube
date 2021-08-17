from manimlib import *
import numpy as np
import sys

if len(sys.argv)<4: print('Please add the diagram number')

diagramNumber = int(sys.argv[3])
cameraSettingNumber = 4
if len(sys.argv) >4:  cameraSettingNumber = int(sys.argv[4])
#1 = Clover, 2 = 2-Pair, 3 = Tri-Pair

#_____Entity Constants and Parameters_____
alpha = 5/6*PI/2
ca = np.cos(alpha)
RED2= "#BF0000"
GREEN2 = "#038800"
BLUE2 = "#3240AF"

colorArr1 = [WHITE, WHITE, BLUE, GREEN, ORANGE, RED]
colorArrB2 = [RED2, "#660000", BLUE_E, BLUE_E, "#005F20", GREEN2]
colorArrB3 = [RED2, RED2, BLUE2,BLUE2, GREEN2, GREEN2]
colorArrB3_2 = [RED2, "#660000", "#1A278A",BLUE2, "#005F20", GREEN2]
colorArrA2 = [colorArrB2[1], colorArrB2[0], colorArrB2[2],colorArrB2[3], 
	colorArrB2[4], colorArrB2[5]]

#_______Create Entities_______

#---Create Rubicks Sphere  (Shape A)---
if diagramNumber == 1: aColors = colorArr1
elif diagramNumber == 2: aColors = colorArrA2
else: aColors = colorArrB3
farrA = [Circle(color=x) for x in aColors]

'''After transformations, farrA has circles 1 and 2 perpendicular to z,
	circles 3 and 4 perp. to y, and circles 5 and 6 perp. to x.'''
farrA[0].shift((0, 0, ca))
farrA[1].shift((0, 0, -ca))
farrA[2].rotate(90*DEGREES, axis=RIGHT)
'''Circle() is parametrized: Original circles at t=0 is [1,0,0]. 
Must rotate circles about their axis of symmetry so the Transform animation 
properly rotates the rings from farrA to farrB.'''
farrA[2].rotate(-90*DEGREES, axis = DOWN)
farrA[2].shift((0, ca, 0))
farrA[3].rotate(90*DEGREES, axis=RIGHT)
farrA[3].rotate(-90*DEGREES, axis = DOWN)
farrA[3].shift((0, -ca, 0))
farrA[4].shift((ca, 0, 0))
farrA[4].rotate(90*DEGREES, axis = UP)
farrA[5].shift((-ca, 0, 0))
farrA[5].rotate(90*DEGREES, axis=UP)
for x in farrA:		x.scale(np.sin(alpha))


if diagramNumber ==1:
	#---Create Clover Schlegel Diagram---
	farrB = [Circle(color=x) for x in colorArr1]	
	farrB[0].scale(.5)
	farrB[1].scale(1)
	farrB[4].shift((1.15,0,0))
	farrB[2].shift((0,1.15,0))
	farrB[2].rotate(180*DEGREES, axis = LEFT+DOWN) #rotate to correct transformation 
	farrB[5].shift((-1.15,0,0))
	farrB[5].rotate(180*DEGREES, axis = UP)#to correct transformation
	farrB[3].shift((0, -1.15,0))
	farrB[3].rotate(-90*DEGREES)


elif diagramNumber==2:
	#---Create 2-Pair Schlegel Diagram---
	for x in farrA:  x.rotate_about_origin(45*DEGREES, axis=UP)
	farrA[2].rotate(45*DEGREES,axis = DOWN)
	farrA[3].rotate(45*DEGREES,axis = DOWN)
	farrA[4].rotate(180*DEGREES, axis = DOWN)
	farrA[5].rotate(180*DEGREES, axis = DOWN)

	farrB = [Circle(color = x) for x in colorArrB2]
	farrB[0].shift([-.6,0,0])
	farrB[0].scale(.75)
	farrB[1].shift([-.6,0,0])
	farrB[2].shift([0,1.15,0])
	farrB[2].rotate(180*DEGREES, axis = RIGHT+UP)
	farrB[3].shift([0,-1.15,0])
	farrB[3].rotate(-90*DEGREES)
	farrB[4].shift([.6,0,0])
	farrB[5].shift([.6,0,0])
	farrB[5].scale(.75)


elif diagramNumber==3:
	#---Create Tri-Pair Schlegel Diagram---
	farrA[2].rotate(45*DEGREES,axis = DOWN)
	farrA[3].rotate(45*DEGREES,axis=DOWN)
	farrA[4].rotate(45*DEGREES,axis = RIGHT)
	farrA[5].rotate(45*DEGREES, axis=RIGHT)
	for x in farrA: 
		x.rotate_about_origin(45*DEGREES, axis=UP)
		x.rotate_about_origin(-45*DEGREES,axis = RIGHT)

	farrB = [Circle(color =x) for x in colorArrB3]
	smR = 2/3.
	l = .7*2/3
	farrB[3].shift((0,-l,0))
	farrB[3].scale(smR)
	farrB[3].rotate(-90*DEGREES)
	farrB[2].shift((0,-l,0))
	farrB[2].rotate(-90*DEGREES)
	farrB[0].shift((l,0,0))
	farrB[0].rotate_about_origin(30*DEGREES)
	farrB[0].scale(smR)
	farrB[1].shift((l,0,0))
	farrB[1].rotate_about_origin(30*DEGREES)
	farrB[5].shift((-l,0,0))
	farrB[5].rotate_about_origin(-30*DEGREES)
	farrB[5].scale(smR)
	farrB[5].rotate(180*DEGREES, axis = RIGHT)
	farrB[5].rotate(150*DEGREES)
	
	farrB[4].shift((-l,0,0))
	farrB[4].rotate_about_origin(-30*DEGREES)
	farrB[4].rotate(180*DEGREES, axis = RIGHT)
	farrB[4].rotate(150*DEGREES)
	

a_to_b = [Transform(farrA[i], farrB[i]) for i in range(len(farrA))]





class RubicksSchlegelTransform(Scene):
	CONFIG = {
		'camera_class':ThreeDCamera,
	}
	def construct(self):
		#_____Setup Frame_____
		axes = ThreeDAxes()#**axis_config)
		self.add(axes) 
		frame = self.camera.frame
		if cameraSettingNumber <4:
			frame.set_euler_angles(
					theta=30 * DEGREES,
					phi=75 * DEGREES,
			)		

		#_____Create Entities_____
		# text2d = Text("Hello")
		# text2d.to_edge(UP+RIGHT)
		# initSphere = Sphere(color = GREY)
		# initSphere.scale(.8*np.sin(alpha))


		
		#_____Add Shapes_____
		self.add(text2d)
		# self.add(initSphere)
		for x in farrA: self.add(x)
		
		#_____Animate_____
		self.wait(2)
		if cameraSettingNumber == 1:
			self.play(frame.animate.increment_theta(-55*DEGREES),run_time = 2	)
			self.play(frame.animate.increment_phi(-25*DEGREES),run_time = 2	)
		if cameraSettingNumber == 2:
			self.play(frame.animate.increment_theta(-40*DEGREES), run_time=2	)
			self.play(frame.animate.increment_phi(-50*DEGREES), run_time=2	)
		if cameraSettingNumber == 3:
			self.play(frame.animate.increment_theta(-55*DEGREES), run_time=2	)
			self.play(frame.animate.increment_phi(-50*DEGREES), run_time=2	)
		self.wait(1)

		# a_to_b.append(FadeOut(initSphere))
		self.play(*a_to_b, run_time = 4)
		self.wait(4)

		# self.embed()
		# quit()
