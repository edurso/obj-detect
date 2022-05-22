#!/usr/bin/env python3
from cscore import CameraServer, UsbCamera
import json

class Camera:

	def __init__(self, inp, out, width, height, cam, exposure, brightness, cameraPath):

		# Camera
		self.cam = cam
		self.path = cameraPath

		# Input & output sources
		self.inp = inp
		self.out = out
		
		# Camera settings
		self.width = width
		self.height = height
		self.exposure = exposure
		self.brightness = brightness

	def get_frame(self, img):
		return self.inp.grabFrame(img)

	def put_frame(self, img):
		self.out.putFrame(img)

def start(config_file: str, cam_num: int):

	with open(config_file) as cfg:
		config = json.load(cfg)
	camera = config['cameras'][cam_num]
	print(camera)

	width = camera['width']
	height = camera['height']
	cameraPath = camera['path']
	exposure = camera['exposure']
	brightness = camera['brightness']
	cs = CameraServer.getInstance()

	# Test making camera
	cam = UsbCamera(dev=cam_num, name=camera['name'])
	cam.setFPS(camera['fps'])

	cam.setResolution(width, height)

	cs.startAutomaticCapture(camera=cam, return_server=True) # Returns `VideoSource`
	# cap.setFPS(camera['fps'])
	
	inp = cs.getVideo(name=camera['name']) # Returns `CvSink`
	out = cs.putVideo(name=camera['name']+'_out', width=width, height=height)

	return Camera(inp, out, width, height, cam, exposure, brightness, cameraPath)

if __name__ == "__main__":
	print('do not run this script\nsomething is wrong')
