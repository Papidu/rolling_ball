import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions

window = pyglet.window.Window(1800, 720, "Pymunk Tester", resizable=True)
options = DrawOptions()
space = pymunk.Space()
space.gravity = 0, -980


@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)


def animations(mass, radius, circle_friction, circle_pos, segment_friction, segment_pos):
    '''
        Initialized space, add circle and segment into space.  
    '''
    circle_moment = pymunk.moment_for_circle(mass, 0, 30)
    circle_body = pymunk.Body(mass, circle_moment)
    circle_body.position = circle_pos 
    circle_shape = pymunk.Circle(circle_body, radius)
    circle_shape.friction = circle_friction 

    segment_shape = pymunk.Segment(space.static_body, segment_pos[0], segment_pos[1], 2)
    segment_shape.body.position = 0, 0
    segment_shape.friction = segment_friction #0.1

    space.add(segment_shape, circle_body, circle_shape)


def update(dt):
    space.step(dt)

def start_animations(mass, radius, circle_friction, circle_pos, segment_friction, segment_pos):
    animations(mass, radius, circle_friction, circle_pos, segment_friction, segment_pos)
    pyglet.clock.schedule_interval(update, 1.0 / 60)
    pyglet.app.run()

