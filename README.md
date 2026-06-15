# Pen-highlighter-detector-colab 🖊️🖍️

A real-time object detection project that detects and classifies **pens** and **highlighters** using YOLOv8, trained on Google Colab with a T4 GPU.

This is my second computer vision project — an upgrade from my first pen-only detector, now with two classes and cloud GPU training.

---

## What it does

Point your webcam at a pen or highlighter and it draws a bounding box around it with the label and confidence score in real time.

---

## Results

Trained for 100 epochs on a custom dataset of ~300+ images labeled using Roboflow.

| Class | Precision | Recall | mAP50 |
|---|---|---|---|
| All | 0.874 | 0.914 | 0.904 |
| Pen | 0.816 | 0.864 | 0.847 |
| Highlighter | 0.932 | 0.965 | 0.962 |

---

## How to run

**1. Clone the repo**
```bash
git clone https://github.com/rishidakshbansal2004-create/pen-highlighter-detector-colab.git
cd pen-highlighter-detector-colab
```

**2. Install dependencies**
```bash
pip install ultralytics opencv-python
```

**3. Run webcam detection**
```bash
python webcam.py
```
Press `q` to quit.

---

## Training

Training was done on Google Colab using a free T4 GPU — see `train.ipynb` for the full training notebook.

If you want to retrain with your own dataset, get a Roboflow API key, update the snippet in the notebook, and run all cells.

---

## Tech used

- YOLOv8 (Ultralytics)
- OpenCV
- Roboflow
- Google Colab (T4 GPU)

---

## My other projects

Check out my first pen detector (trained locally): [Object-Detector-Pen](https://github.com/rishidakshbansal2004-create/Object-Detector-Pen-)
