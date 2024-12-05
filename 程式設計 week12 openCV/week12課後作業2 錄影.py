import cv2
from deepface import DeepFace

# 初始化攝影機
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("無法啟用攝影機")
    exit()

# 使用 Haar Cascade 偵測人臉
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 設定錄影參數
fourcc = cv2.VideoWriter_fourcc(*'XVID')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('emotion_output.avi', fourcc, 20.0, (frame_width, frame_height))

print("按下 'q' 鍵結束辨識並保存影片")

while True:
    ret, frame = cap.read()
    if not ret:
        print("無法讀取影像")
        break

    # 轉換為灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 偵測人臉
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    for (x, y, w, h) in faces:
        # 擷取人臉
        face = frame[y:y+h, x:x+w]

        # 使用 DeepFace 進行情緒辨識
        try:
            analysis = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
            dominant_emotion = analysis['dominant_emotion']
        except Exception as e:
            dominant_emotion = "N/A"

        # 繪製人臉框
        cv
