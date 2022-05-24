# Build the [TensorRT](https://developer.nvidia.com/tensorrt) Engine

To export the TensorRT Model, the first cell must be edited in order for the `workdir` variable to point to the `trained_model/` directory.

The whole notebook can be run at once. An intermediate model will be saved (called `model.onnx`) in the `trained_model/` directory.

The notebook will take a while to run as it will need to update [cuDNN](https://developer.nvidia.com/cudnn), and a few other NVIDIA libraries.

The engine will download automatically at the end of training, and should be moved to the `bin/` directory of this project in preparation for deployment to the Jetson.
