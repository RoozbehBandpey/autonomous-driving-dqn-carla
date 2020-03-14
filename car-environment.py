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
		
