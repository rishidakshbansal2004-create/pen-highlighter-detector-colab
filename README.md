```markdown
# Pen-highlighter-detector-colab 🖊️🖍️

A real-time object detection project that detects and classifies **pens** and **highlighters** using YOLOv8s, trained on Google Colab with a T4 GPU.

This is my second computer vision project — an upgrade from my first pen-only detector, now with two classes, a larger balanced dataset, and an upgraded model architecture.

---

## What it does

Point your webcam at a pen or highlighter and it draws a bounding box around it with the label and confidence score in real time.

---

## Results

Trained for 100 epochs on a custom balanced dataset of 678 images (434 pen / 422 highlighter annotations) labeled using Roboflow.

| Class | Precision | Recall | mAP50 |
|---|---|---|---|
| All | 0.919 | 0.885 | 0.932 |
| Pen | 0.881 | 0.794 | 0.899 |
| Highlighter | 0.957 | 0.976 | 0.965 |

**Inference speed:** 10.4ms (~96 FPS) on Colab T4 GPU

---

## Upgrade from v1

| | v1 (YOLOv8n) | v2 (YOLOv8s) |
|---|---|---|
| Dataset | ~300 images | 678 images |
| mAP50 (all) | 0.904 | 0.932 |
| Highlighter mAP50 | 0.962 | 0.965 |
| Inference | — | 10.4ms (~96 FPS) |

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

**3. Set model path**

Before running, open `webcam.py` and update the model path to where your `best.pt` is located:
```python
model = YOLO("path/to/best.pt")
```

**4. Run webcam detection**
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

- YOLOv8s (Ultralytics)
- OpenCV
- Roboflow
- Google Colab (T4 GPU)

---

## My other projects

Check out my first pen detector (trained locally): [Object-Detector-Pen](https://github.com/rishidakshbansal2004-create/Object-Detector-Pen-)
```

Copy paste this directly into your README.md on GitHub. Done!
