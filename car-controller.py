from __future__ import print_function

# -- find carla module
import glob
import os
import sys

try:
	sys.path.append(glob.glob('C:/CARLA_0.9.8/WindowsNoEditor/PythonAPI/carla/dist/carla-*%d.%d-%s.egg' % (
		sys.version_info.major,
		sys.version_info.minor,
		'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError as err:
	print(err)
	pass


# -- imports
import carla
import random
import time

actors = []
IM_WIDTH = 640
IM_HIGHT = 480


def process_img(image):
	

# -- attempt to connect to server and clean ups
try:
	client = carla.Client('localhost', 2000)
	client.set_timeout(2.0)
	world = client.get_world()
	blueprint_library = world.get_blueprint_library()

	blueprint = blueprint_library.filter("model3")[0]
	print(blueprint)

	spawn_point = random.choice(world.get_map().get_spawn_points())

	vehicle = world.spawn_actor(blueprint, spawn_point)
	# vehicle.set_autopilot(True)

	vehicle.apply_control(carla.VehicleControl(throttle=1.0, steer=0.0))
	actors.append(vehicle)

	# attach a camera sensor to the car
	cam_blueprint = blueprint_library.find("sensor.camera.rgb")
	cam_blueprint.set_attribute("image_size_x", f"{IM_WIDTH}")
	cam_blueprint.set_attribute("image_size_y", f"{IM_HIGHT}")
	cam_blueprint.set_attribute("fov", "110")


	spawn_point = carla.Trasform(carla.Location(x=2.5, z=0.7))
	sensor = world.spawn_actor(cam_blueprint, spawn_point, attach_to=vehicle)
	actors.append(sensor)

	# listening
	sensor.listen(lambda dsta: process_img(data))

	time.sleep(15)



finally:
	for actor in actors:
		actor.destroy()
	print("All cleaned up!")
