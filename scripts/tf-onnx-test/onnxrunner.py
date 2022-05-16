#!/usr/bin/env python3

# update path
import sys
sys.path.append('../scripts')

# imports
import os
from cv2 import imread
from scripts import onnxutils as utils

batch_size = 1
precision = "FP16"
model_dir = '../models/saved_model_rev1'
model_name = model_dir + '/saved_model.onnx'
test_img = '../img/frame-321.jpg'

# build trt engine
os.system('trtexec --onnx={} --saveEngine=engine.trt  --explicitBatch --inputIOFormats=fp16:chw --outputIOFormats=fp16:chw --fp16'.format(model_name))

trt_model = utils.ONNXClassifierWrapper("engine.trt", [batch_size, 1000], target_dtype=precision)
print(trt_model.predict(imread(test_img))[0][:10])
