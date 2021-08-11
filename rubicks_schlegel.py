from manimlib import *
import numpy as np

diagramNumber = 3
#1 = Clover, 2 = 2-Pair, 3 = Tri-Pair

#_____Entity Constants and Parameters_____
alpha = 5/6*PI/2
ca = np.cos(alpha)
colorArr1 = [WHITE, WHITE, BLUE, GREEN, ORANGE, RED]
colorArrB2 = [RED, RED, BLUE, BLUE, GREEN, GREEN]
colorArrA2 = [colorArrB2[1], colorArrB2[0], colorArrB2[2],colorArrB2[3], 
	colorArrB2[4], colorArrB2[5]]

#_______Create Entities_______

#---Create Rubicks Sphere  (Shape A)---
if diagramNumber == 1: aColors = colorArr1
elif diagramNumber == 2: aColors = colorArrA2
else: aColors = colorArrB2





farrA = [Circle(color=x) for x in aColors]
for x in farrA:
		x.scale(np.sin(alpha))

'''After transformations, farrA has circles 1 and 2 perpendicular to z,
	circles 3 and 4 perp. to y, and circles 5 and 6 perp. to x.'''
farrA[0].shift((0, 0, ca))
farrA[1].shift((0, 0, -ca))
farrA[2].rotate(90*DEGREES, axis=RIGHT)
farrA[2].shift((0, ca, 0))
farrA[3].rotate(90*DEGREES, axis=RIGHT)
farrA[3].shift((0, -ca, 0))
farrA[4].rotate(90*DEGREES, axis=UP)
farrA[5].rotate(90*DEGREES, axis=UP)
farrA[4].shift((ca, 0, 0))
farrA[5].shift((-ca, 0, 0))


if diagramNumber ==1:
	#---Create Clover Schlegel Diagram---
	farrB = [Circle(color=x) for x in colorArr1]	
	farrB[0].scale(.5)
	farrB[1].scale(1)
	farrB[4].shift((1.15,0,0))
	farrB[2].shift((0,1.15,0))
	farrB[5].shift((-1.15,0,0))
	farrB[3].shift((0, -1.15,0))

elif diagramNumber==2:
	for x in farrA:  x.rotate_about_origin(45*DEGREES, axis=UP)

	#---Create 2-Pair Schlegel Diagram---
	farrB = [Circle(color = x) for x in colorArrB2]
	
	farrB[2].shift([0,1.15,0])
	farrB[3].shift([0,-1.15,0])
	farrB[4].shift([.6,0,0])
	farrB[5].shift([.6,0,0])
	farrB[5].scale(.75)
	farrB[0].shift([-.6,0,0])
	farrB[1].shift([-.6,0,0])
	farrB[0].scale(.75)


else:
	for x in farrA: 
		x.rotate_about_origin(45*DEGREES, axis=UP)
		x.rotate_about_origin(-45*DEGREES,axis = RIGHT)

	#---Create Tri-Pair Schlegel Diagram---
	farrB = [Circle(color =x) for x in colorArrB2]
	smR = 2/3.
	l = .7*2/3
	farrB[0].shift((0,-l,0))
	farrB[0].scale(smR)
	farrB[1].shift((0,-l,0))
	farrB[2].shift((-l,0,0))
	farrB[2].rotate_about_origin(-30*DEGREES)
	farrB[2].scale(smR)
	farrB[3].shift((-l,0,0))
	farrB[3].rotate_about_origin(-30*DEGREES)
	farrB[4].shift((l,0,0))
	farrB[4].rotate_about_origin(30*DEGREES)
	farrB[4].scale(smR)
	farrB[5].shift((l,0,0))
	farrB[5].rotate_about_origin(30*DEGREES)
	




# a_to_b1 = [Transform(farrA[i], farrB1[i]) for i in range(len(farrA))]
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
		frame.set_euler_angles(
				theta=30 * DEGREES,
				phi=75 * DEGREES,
		)
		# frame.rotate(90*DEGREES,axis = RIGHT)
	


		#_____Create Entities_____
		text2d = Text("Hello")
		text2d.to_edge(UP+RIGHT)


		
		#_____Add Shapes_____
		self.add(text2d)

		for x in farrA: self.add(x)
		self.wait(2)
		self.play(frame.animate.increment_theta(-55*DEGREES),run_time = 2	)
		self.play(frame.animate.increment_phi(-25*DEGREES),run_time = 2	)
		self.wait(1)
		self.play(*a_to_b, run_time = 4)
		self.wait(4)

		# self.embed()
		# quit()







		# axis_config = {
		# 	'x_min': -5,
		# 	'x_max':5,
		# 	'y_min':-5,
		# 	'y_max':5,
		# 	'z_min':-5,
		# 	'z_max':5
		# }


		#text3d = TextMobject('Yo').scale(2)
		#text3d.rotate(PI/2,axis=RIGHT)

	# def func1(t):
	# 	return np.array([np.sin(t), np.cos(t), 1])

	# circ1 = ParametricCurve(func1, t_range =[0,TAU])
	# circ2 = Circle(color= RED)
	# circ2.move_to(axes.c2p(1,2))
	# circ3 = Circle(color=BLUE)
	# circ4 = Circle(color = GREEN)
	# circ3.move_to(axes.c2p(5,-3,1))
	# circ3.rotate(45*DEGREES, axis = RIGHT)
	# circ4.move_to(axes.c2p(3,3,-4))

	# self.add_fixed_in_frame_mobjects(text2d)

	# self.add(circ1)
	# self.add(circ3)
	# self.wait(2)


	# transforms = [Transform(circ1,circ2),Transform(circ3, circ4)]
	# self.play(*transforms)

	# curve1a = ParametricFunction(lambda t:np.array([np.sin(t), np.cos(t),1]),color= BLUE, t_min = 0, t_max = TAU)
	# curve1b = ParametricFunction(lambda t: np.array([t,t,t]), color=BLUE, t_min=0, t_max=TAU)

	# self.play(ShowCreation(axes))

	# self.play(ShowCreation(curve1a),run_time = 2)
	# self.wait()
	# self.play(Transform(curve1a,curve1b))
	# self.wait(5)
