import time

from threading import Thread
from time import sleep

import app.network.dashboard as dash
import app.pipelines.pipelineloader as pl
from app.pipelines.pipeline import VisionPipeline

CFG = '/home/lightning/bin/config.json'

def main():

	# start dashboard
	table = dash.load(CFG)

	# start pipelines
	pipes = pl.loadall(CFG, table)

	# push number of pipelines to dashboard
	table.putNumber('# Pipelines', len(pipes))

	# start threads
	for pipe in pipes:
		thread = Thread(target=vision_thread, args=(pipe[1],table,pipe[0],))
		thread.start()

	print('APPLICATION STARTED SUCCESSFULLY')
	
	while True:
		sleep(10)

def vision_thread(pipe: VisionPipeline, table, pipe_name: str) -> None:

	while True:
		start_time = time.time()
		pipe.process()
		processing_time = time.time() - start_time
		fps = 1 / processing_time
		table.putNumber('FPS_'+pipe_name, fps)

if __name__ == '__main__':
    main()
