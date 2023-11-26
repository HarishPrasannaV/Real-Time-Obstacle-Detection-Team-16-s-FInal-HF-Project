from ultralytics import YOLO
# Using Yolo V8 directly

model = YOLO("y8best.pt")
results = model.predict(source="input.mp4", show=True)

print(results)