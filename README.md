# Real-Time Object Detection System : Team-16's HF Final Project

https://docs.google.com/document/d/1EcaAYSVAPxhZW8EdJLPCVg30SXhnowI04mBlaU2_MMM/edit?usp=sharing

## Team Members:

CHITRANSHU WAGH (ED21B020)
HARISH PRASANNA V (ED21B027)
JEEVABHARATHI R (ED21B030)

## Steps to run Code

1. Clone the repository.

2. Install the requried modules

3. To directly use YOLO v8:
   `python test.py`

4. Download Weights : https://drive.google.com/drive/folders/1gPa3KPLKyO4hx13vOiTgIiRGESQb24Lk?usp=drive_link

5. To use the model custom trained on data online:
   `python predict.py model=y8best.pt source="input.mp4" show=True`
   You can choose one of Two weights availabe: 'y8best.pt' or 'best.pt'

#### train.py was used to generate the weights.
