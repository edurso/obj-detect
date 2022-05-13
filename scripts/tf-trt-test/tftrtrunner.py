#!/usr/bin/env python3

# update path
import sys
sys.path.append('../../scripts')

# imports
from cv2 import imread
from time import process_time
from scripts import tftrtutils as utils

batch_size = 1
precision = "FP16"
model_dir = '../models/saved_model_rev1'
test_img = '../img/frame-321.jpg'

model_opt = utils.ModelOptimizer(model_dir)
model_fp16 = model_opt.convert(model_dir+'_fp16', precision=precision)

model_fp16.predict(imread(test_img))

startt = process_time()
out = model_fp16.predict(imread(test_img))
endt = process_time()
print('Inference took {}s'.format(endt-startt))
print(out)
