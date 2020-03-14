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
import numpy as np
import cv2



SHOW_PREVIEW = False # Turn to ture for debuigging purposes. Display the actual camera. To display the preview it's gonna lock up compute resources. Setting this to True probably gonna maxing things up
IM_WIDTH = 640
IM_HEIGHT = 480


class CarEnvironment:
	SHOW_CAM = SHOW_PREVIEW
	STEER_AMT = 1.0
	im_width = IM_WIDTH
	im_height = IM_HEIGHT
	front_camera = None


	def __init__(self):
		self.client = carla.Client("localhost", 2000)
		self.client.set_timeout(2.0)
		self.world = self.client.get_world()
		self.blueprint_library = self.world.get_blueprint_library()
		self.model_3 = blueprint_library.filter("model3"[0])

	def reset(self):
		"""
		To run annother episode
		"""
		self.collision_hist = []
		self.actor_list = []

		self.transform = random.choice(self.world.get_map().get_spawn_points())
		self.vehicle = self.world.spawn_actor(self.model3, self.transform)
		self.actor_list.append(self.vehicle)

		self.rgb_cam = self.blueprint_library.find('sensor.camera.rgb')
		self.rgb.set_attribute("image_size_x", f"{self.im_width}")
		self.rgb.set_attribute("image_size_y", f"{self.im_height}")
		self.rgb.set_attribute("fov", f"110")

		transform = carla.Transform(carla.Location(x=2.5, z=0.7))
		self.sensor = self.world.spawn_actor(self.rgb_cam, transform, attach_to=self.vehicle)
		self.actor_list.append(self.sensor)
		self.sensor.listen(lambda data: self.process_img(data))

	def process_img(self, image):
		i = np.array(image.raw_data)
		print(i.shape)
		i2 = i.reshape((IM_HEIGHT, IM_WIDTH, 4))

		# The entire height, the entire width, thr first three of r, g, b, a
		# Kinda nifty way to grab r,g,b there is an open cv method to do the exact same thing
		# Basically converts rgb alpha to just straight up  rgb, interestingly enough it is slower than the numpy method
		# You would have expected it to do the same thing, but simply does not
		i3 = i2[:, :, :3]
		print(i3.shape)
		cv2.imshow("", i3)
		cv2.waitKey(1)
		return i3/255.0
