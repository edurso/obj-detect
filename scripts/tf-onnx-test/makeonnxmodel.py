#!/usr/bin/env python3

# update path
import sys
sys.path.append('../scripts')

# imports
import os
import onnx
import tf2onnx

batch_size = 1
model_dir = '../models/saved_model_rev1'
model_name = model_dir + '/saved_model.onnx'

os.system('python3 -m tf2onnx.convert --saved-model {} --output temp.onnx'.format(model_dir))
model_onnx = onnx.load_model('temp.onnx')

# fix batch size
inputs = model_onnx.graph.input
for input in inputs:
    dim1 = input.type.tensor_type.shape.dim[0]
    dim1.dim_value = batch_size
onnx.save_model(model_onnx, model_name)
