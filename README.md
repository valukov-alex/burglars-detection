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
  <img src="burglars-detection/results/Figure_1.png" >
</p>
    
