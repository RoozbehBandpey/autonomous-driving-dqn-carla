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


actors = []

# -- attempt to connect to server and clean ups
try:
	client = carla.Client('localhost', 2000)
	client.set_timeout(2.0)
	world = client.get_world()
	blueprint_library = world.get_blueprint_library()

	blueprint = blueprint_library.filter("model3")[0]
	print(blueprint)

finally:
	for actor in actors:
		actor.destroy()
	print("All cleaned up!")
