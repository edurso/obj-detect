#!/usr/bin/env python3

import importlib
import json

def loadall(config_file: str, table):

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

def load(config_file: str, pipe, table):

	# read json config for pipeline
	name = pipe['name']
	fname = pipe['fname']
	camera = int(pipe['camera'])

	# dynamically import/load pipeline
	module = importlib.import_module(fname)
	class_ = getattr(module, name)
	instance = class_(config_file, camera, table)

	# return instance
	return name, instance
