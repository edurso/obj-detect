#!/usr/bin/env python3

from abc import ABC, abstractmethod

class VisionPipeline(ABC):

	@abstractmethod
	def __init__(self, config: str, cam_num: int, table) -> None:
		pass
	
	@abstractmethod
	def process(self):
		pass
