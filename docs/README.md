# Overview

This project is intended to serve as a sample codebase for machine learning based computer vision systems in the [FIRST Robotics Competition](https://www.firstinspires.org/robotics/frc). The project leverages transfer learning via the [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection), optimization and inference with [TensorRT](https://developer.nvidia.com/tensorrt), and deployment with the help of [RobotPy](https://robotpy.readthedocs.io/en/stable/). The application that run inference on the TensorFlow Object Detection Model should be run on a NVIDIA Jetson Module, such as the [NVIDIA Jetson Nano 2GB Developer Kit](https://developer.nvidia.com/embedded/jetson-nano-2gb-developer-kit), which would be on-board the robot. A 3D printable case for the Jetson Nano 2GB can be found [here](https://grabcad.com/library/jetson-nano-2gb-case-1).

This project consists of five main components listed below:

1. A set of scripts to work with datasets for object detection models.
2. A Jupyter Notebook (intended for the [Google Colab](https://colab.research.google.com/)) intended for training object detection models.
3. Another Jupyter Notebook (for the [Google Colab](https://colab.research.google.com/)) intended to convert the trained model (a TensorFlow `saved_model`) to a [TensorRT](https://developer.nvidia.com/tensorrt) engine.
4. A set of scripts to setup and configure a Jetson Nano.
5. A simple python command-line application to run inference on a [TensorRT](https://developer.nvidia.com/tensorrt) engine.

The following section highlights the outline of this documentation and the steps needed to get this project up and running.

## Getting Started

Getting a model up and running consists of 3 steps, each of which is described in the corresponding document:

| Step                                                                                                                                    | Doc                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Training a Model with the [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) | [train_model.md](https://github.com/edurso/obj-detect/blob/master/docs/train_model.md)                     |
| Converting the Model to a [TensorRT](https://developer.nvidia.com/tensorrt) engine                                                      | [build_tensorrt_engine.md](https://github.com/edurso/obj-detect/blob/master/docs/build_tensorrt_engine.md) |
| Deploying the Model to a NVIDIA Jetson                                                                                                  | [inference_application.md](https://github.com/edurso/obj-detect/blob/master/docs/inference_application.md) |

## Benefits of GPU Acceleration

GPU acceleration allows neural network operations to be much faster as GPUs are more optimized for the kinds of operations machine learning libraries, such as [TensorFlow](https://www.tensorflow.org/) use. The benefits of GPU acceleration are highlighted in [notebooks/test_tf.ipynb](https://github.com/edurso/obj-detect/blob/master/notebooks/test_tf.ipynb) which runs the same operation on both a CPU and GPU and displays the difference in runtime. As the scale of the input increases, the GPU becomes faster relative to the CPU.
