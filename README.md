# Circular Object Detection and Tracking

This repository contains a Python project focused on detecting circular objects using image processing techniques. The project utilizes the Hough Circles algorithm for circular object detection, and Gaussian Blur is applied to control the frequency of circle detection. Additionally, a marker is placed at the center of the detected circle to track the movement of the object.

## Table of Contents
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)

## Introduction

The main goal of this project is to showcase a simple yet effective method for detecting circular objects in videos in real-time. The Hough Circles algorithm is employed due to its capability to identify circular shapes even with noise and partial occlusion. By applying Gaussian Blur on the frames before running the Hough Circles algorithm, we can control the sensitivity of circle detection and reduce false positives.

In addition to circle detection, a visual marker is placed at the center of the detected circle. This marker aids in tracking the movement of the circular object within the video.

## Technologies

- Python
- OpenCV: A powerful computer vision library used for image and video analysis.

## Setup

1. Clone this repository to your local machine using:
   ```
   git clone https://github.com/Muhammad-Wajahat/Image-Processing-Circular-Object-Detection-and-Tracking.git 
   ```
   
2. Navigate to the project directory:
   ```
   cd Image-Processing-Circular-Object-Detection-and-Tracking
   ```

3. Install the required dependencies using `pip`:
   ```
   pip install opencv-python
   ```

## Usage

1. Run the main script:
   ```
   python circular_detection.py
   ```

2. The Script will start the front camera and you can hold a circular object in front of it to start the detection and tracking process

3. press the ESC key to exit the program.
