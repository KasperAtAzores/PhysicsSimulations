import bpy
from math import pi

"""
This is a 3D simulation of chaos pendula. 
This video shows a simple 2 arm chaos pendulum in the real physical world
https://www.youtube.com/watch?v=U39RMUzCjiU

A level 0 pendula has one stick, a level 1 has 2 sticks, etc.
"""

golden = (1 + 5 ** 0.5) / 2

def scale (scale, vector):
    return (vector[0]*scale, vector[1]*scale, vector[2]*scale)
    
def translate(a,b): # a and b are 3D vectors
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])
    
def make_sphere(radius, location, name):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, size=radius, location=location)
    ball = bpy.context.active_object
    ball.name = name
    return ball


def new_stick(pivot, weight, level):
    """ Main method to put up the connected balls. 

    Parameters
    ----------
    pivot : 3D vector where the hinge object will be placed
    weight: float, the mass of the entire construction 
            (all balls at this level and lower)
    level: int, used to control recursion and distance
            between balls and their radius
    """
    
    if level == 0:
        my_weight = weight
    else:
        my_weight = weight/golden
        
    stick_length = 3+level*2
    if level % 2 == 0: 
        ball_offset = (stick_length,0,0)
    else:
        ball_offset = (0,stick_length,0)
  
    hinge_radius = 0.5
    hinge_location = pivot
    make_sphere( hinge_radius, hinge_location, "hinge_level_"+str(level))
    bpy.ops.object.modifier_add(type='SOLIDIFY')
    bpy.context.object.modifiers["Solidify"].thickness = 0.1
    bpy.context.object.modifiers["Solidify"].thickness_clamp = 0
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify")

    ball_radius = min(4-level,1)
    ball_location = translate(pivot, ball_offset)
    make_sphere(ball_radius, ball_location, "ball_level_"+str(level) )

    mini_radius = 0.25
    mini_location = translate( pivot, scale(-1,ball_offset))
    make_sphere( mini_radius, mini_location, "mini_level_"+str(level))

    bpy.ops.object.select_pattern(pattern="*_level_"+str(level), extend=False)
    bpy.ops.object.join()
    stick = bpy.context.active_object
    stick.name = "stick_level_"+str(level)
    bpy.context.scene.cursor_location = ball_location
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    
    stick.game.physics_type = 'RIGID_BODY'
    stick.game.use_collision_bounds = True
    stick.game.collision_bounds_type = 'TRIANGLE_MESH'
    stick.game.mass = my_weight
    if level > 0:
        new_stick(mini_location, weight-my_weight, level-1)
        
        

def clean_scene_of_objects():
    if len(bpy.context.selected_objects) > 0: # if the scene has objects
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False) # set object mode
        #bpy.ops.object.select_all(action='SELECT')           # select all objects
        bpy.ops.object.select_pattern(pattern="*_level_*", extend=False)
        bpy.ops.object.delete(use_global=True)               # and delete them



clean_scene_of_objects()
bpy.context.scene.render.engine = 'BLENDER_GAME'
make_sphere( 0.25, (0,0,0), "fixpoint_level_start")
new_stick( (0,0,0), 50, 3)
#bpy.ops.view3d.game_start()