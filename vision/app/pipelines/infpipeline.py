import numpy as np

from app.pipelines.pipeline import VisionPipeline
from app.inference.inference import TensorRTInfer
import app.camera.camutils as utils

ENGINE = '/home/lightning/bin/engine.trt'
PREPROCESSOR = 'fixed_shape_resizer'
DETECTION = 'bbox'
IOU_THRESH = 0.5

class InferencePipeline(VisionPipeline):

	def __init__(self, config: str, cam_num: int, table) -> None:
		
		# one camera thing
		self.cam = utils.start(config, cam_num)

		# network table output
		self.detectionEntry = table.getEntry('detections')

		# inference util
		self.engine = TensorRTInfer(ENGINE, PREPROCESSOR, DETECTION, IOU_THRESH)

		# allocate image for whenever
		self.img = np.zeros(shape=(self.height, self.width, 3), dtype=np.uint8)

	def process(self):

		# get frame from camera
		self.t, self.img = self.cam.get_frame(self.img)

		# run inference
		detections = self.engine.infer(self.img)

		# run detections back to rio
		self.detectionEntry.putNumberArray(detections)

		return
