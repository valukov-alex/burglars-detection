# burglars-detection
This is test task for SAP internship

# Task
"I am a robber of an ATM, when I break it I usually use a hammer, an ax or a nail-drawer.

Write a program that by photo or video (at your choice) would recognize these objects in the hands of
the burglars, displaying a warning when this item is found on the screen or storing it in a file."

# Data processing
I'm use images of ax and hammer with bounding boxes from [ImageNet](http://image-net.org). Unfortlently, I don't find bounding boxes for nail-drawer so I had to do it myself with [labelImg](https://github.com/tzutalin/labelImg).
Total i have ~1500 images. About 90% I used for train.
# Model
I used [TensorFlow object detection API](https://github.com/tensorflow/models/blob/master/research/object_detection) and pre-trained model ssd_mobilenet_v1_coco
# Results
As you can see,model works not bad, but it need more time and images for training.
<p align="center">
  <img src="https://github.com/valukov-alex/burglars-detection/blob/master/results/Figure_1.png" width=430 height=330>
  <img src="https://github.com/valukov-alex/burglars-detection/blob/master/results/Figure_2.png" width=430 height=330>
</p>

# Installation

## Dependencies

Tensorflow Object Detection API depends on the following libraries:

*   Protobuf 3+
*   Python-tk
*   Pillow 1.0
*   lxml
*   tf Slim (which is included in the "tensorflow/models/research/" checkout)
*   Jupyter notebook
*   Matplotlib
*   Tensorflow
*   Cython

For detailed steps to install Tensorflow, follow the [Tensorflow installation
instructions](https://www.tensorflow.org/install/). A typical user can install
Tensorflow using one of the following commands:

``` bash
# For CPU
pip install tensorflow
# For GPU
pip install tensorflow-gpu
```

The remaining libraries can be installed on Ubuntu 16.04 using via apt-get:

``` bash
sudo apt-get install protobuf-compiler python-pil python-lxml python-tk
sudo pip install Cython
sudo pip install jupyter
sudo pip install matplotlib
```

Alternatively, users can install dependencies using pip:

``` bash
sudo pip install Cython
sudo pip install pillow
sudo pip install lxml
sudo pip install jupyter
sudo pip install matplotlib
```

## Protobuf Compilation

The Tensorflow Object Detection API uses Protobufs to configure model and
training parameters. Before the framework can be used, the Protobuf libraries
must be compiled. This should be done by running the following command from
the burglars-detection/ directory:


``` bash
# From burglars-detection/
protoc object_detection/protos/*.proto --python_out=.
```

## Add Libraries to PYTHONPATH

When running locally, the tensorflow/models/research/ and slim directories
should be appended to PYTHONPATH. This can be done by running the following from
/burglars-detection/:


``` bash
# From /burglars-detection/
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```

Note: This command needs to run from every new terminal you start. If you wish
to avoid running this manually, you can add it as a new line to the end of your
~/.bashrc file.

# How to start

``` bash
# From /burglars-detection/
python3 start.py
```
You can change path to image in start.py

``` bash
#Path to image
PATH_TO_TEST_IMAGES_DIR = 'test_images'
TEST_IMAGE_PATHS =  os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image3.jpg')
```

