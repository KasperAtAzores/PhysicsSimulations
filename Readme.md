# 12 principles of animation

Video link: [https://www.youtube.com/watch?v=uDqjIdI4bF4](https://www.youtube.com/watch?v=uDqjIdI4bF4)

Compare with [this blender animation](https://www.youtube.com/watch?time_continue=20&v=RdJQBqTbHCM)

## Blender physics simulations

Demo at: [https://www.youtube.com/watch?v=PfezSJB21vk](https://www.youtube.com/watch?v=PfezSJB21vk)

### Demo in blender

* [Game engine](https://docs.blender.org/manual/en/dev/game_engine/index.html)
* Physics and gravity
	* Simple box that fall (gravety01)
	* Simple box that hit something (gravity02)
	* Parented boxes (gravety03)
	
* Joined boxes
	* Bounding boxes (gravity04)
	* Center of mass (**Shift-Control-Alt-C**)

* Elasticity (gravity05)
	* Boing - physics of materials - remember to make both objects springy
		*  Double ball bounce

* Soft objects (gravity06)
	*  Key parameters (`Shape Match`, `Liniar Stiffness`, `Margin`)
	

### Recap 

* Gravity
* Static objects 
* Rigid objects
* Soft objects

## Fysics control
* Framerates
* Physics steps
	* `physics_step_max`. Maximum number of physics step per game frame if graphics slows down the game, higher value allows physics to keep up with realtime
	<br>Type:	int in [1, 10000], default 5
	* `physics_step_sub`. Number of simulation substep per physic timestep, higher value give better physics precision. <br>
Type:	int in [1, 50], default 1

Example: In the `chain.blend` example. If the Scene physics are set to (5,1,30), you can see that one of the rings falls of (you can see it in wireframe mode). If you increase the `physics_step_sub` to 2, this does not happen.

## Pendulums

This [little video](https://www.youtube.com/watch?v=U39RMUzCjiU) shows the difference between a regular pendulum and a multi-arm pendulum.

### Rigid body joints

Each rigid object can be attached to an other object using a `Rigid Body Joint`. 

With the outset in (joints01) we will make the pendulum swing. To do this one need to make sure the location of the joint (called pivot) and the center of mass is not the same spot.

* Notice, the pivot can be outside of the child object.
* Notice, the pivot of the child is relative to the center of mass of the parent.

Explain physical ball joints (physicalBallJoint). In particular notive the margins of error and the difference in effect of the different bounding box types. It is best seen in wiremesh view.

One of the peculiar things in blender and other physics engines is that one can join objects into a whole even when they appear to be unconnected - you do not need a stick or glue to join two objects.

### A full chaos pendulum script

Notice, the script do not color the balls.




