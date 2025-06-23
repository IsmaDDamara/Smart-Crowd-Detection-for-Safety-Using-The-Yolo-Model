# **📸 Smart Crowd Detection for Safety Using the YOLO Model**

**Crowd Detection Using YOLO** is a machine learning project designed to automatically detect crowds using the **You Only Look Once (YOLO)** algorithm. This system can be used to monitor public areas and issue alerts in cases of overcrowding, making it useful for safety protocols, surveillance, and crowd management.

## 🎯 Project Objectives

* Detect and count the number of people in a given area.
* Provide alerts when crowd density exceeds a defined threshold.
* Use the YOLO model for real-time object detection.

## 📦 Key Features

* 🔍 **Real-Time Detection**: Utilizes YOLO to detect crowds in live video or camera feeds.
* 📊 **People Counting**: Counts the number of individuals in each frame.
* 🚨 **Crowd Alert System**: Triggers alerts when the number of people exceeds a specified limit.

## 🧠 Technologies Used

* **YOLO (You Only Look Once)** – YOLOv4-tiny
* **OpenCV** – For image and video processing
* **Python** – Primary programming language
* **Darknet** – Framework for training and inference

## 🎥 Project Demo

Watch the demo video of the system in action here:
<video controls src="test.mp4" title="Title"></video>

## 📊 Dataset

The dataset used for training and testing the model is available at:
👉 [CrowdHuman Dataset](https://www.crowdhuman.org/)

## 🚀 How to Run

**Clone the repository:**

```bash
git clone https://github.com/IsmaDDamara/iSense_Smart-Crowd-Detection-with-ML-Model.git
```

**Navigate to the test directory:**

```bash
cd test/opencv_dnn
```

**Run the detection script:**

```bash
python opencv_video.py
```

## 📄 License

This project is licensed under the **MIT License**.
