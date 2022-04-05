#!/usr/bin/env python3

import cv2

class Pipeline():

	def __init__(self, graphpath: str, labelpath: str) -> None:
		self.net = cv2.dnn.readNetFromTensorflow(graphpath, labelpath)

	def inference(self, img):
		rows = img.shape[0]
		cols = img.shape[1]
		self.net.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
		cv2Out = self.net.forward()

		for detection in cv2Out[0,0,:,:]:
			score = float(detection[2])
			if score > 0.3:
				left = detection[3] * cols
				top = detection[4] * rows
				right = detection[5] * cols
				bottom = detection[6] * rows
				cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

		return img

pipe = Pipeline('./graph/faster_rcnn_resnet50_coco_2018_01_28/frozen_inference_graph.pb', './graph/faster_rcnn_resnet50_coco_2018_01_28/faster_rcnn_resnet50_coco_2018_01_28.pbtxt')
cap = cv2.VideoCapture(0)
while cap.isOpened():
	ret, frame = cap.read()
	if ret:
		cv2.imshow('Frame', pipe.inference(frame))
