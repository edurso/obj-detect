#!/usr/bin/env python3

import importlib
import json
import sys
from pipeline import VisionPipeline

def loadall(config_file: str, table):

	# insert at 1, 0 is the script path (or '' in REPL)
	sys.path.insert(1, './pipelines/')

	# list of pipelines
	piperunners = []

	# read pipelines from config file
	with open(config_file) as cfg:
		config = json.load(cfg)
	pipes = config['pipelines']

	# initialize and load each pipeline
	for pipe in pipes:
		print(pipe)
		piperunner = load(config_file, pipe, table)
		piperunners.append(piperunner)
		
	return piperunners

def load(config_file: str, pipe, table) -> VisionPipeline:

	# read json config for pipeline
	name = pipe['name']
	fname = pipe['fname']
	camera = pipe['camera']
	cam_name = pipe['cameraname']

	# dynamically import/load pipeline
	module = importlib.import_module(fname) # 'voidvision.pipelines.'+fname
	class_ = getattr(module, name)
	instance = class_(config_file, camera, cam_name, (name + '_output'))

	# return instance
	return instance
