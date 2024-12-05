import cv2

def capture_and_process():
    # 開啟相機
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("無法開啟相機")
        return

    print("按下空白鍵拍照並進行處理，按下 'q' 退出")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("無法讀取相機影像")
            break

        # 顯示影像
        cv2.imshow('Camera', frame)

        # 等待按鍵事件
        key = cv2.waitKey(1)
        if key == ord(' '):  # 按下空白鍵拍照
            cv2.imwrite('captured_image.jpg', frame)
            print("照片已儲存為 captured_image.jpg")

            # 進行影像處理
            process_image('captured_image.jpg')
        elif key == ord('q'):  # 按下 'q' 退出
            break

    cap.release()
    cv2.destroyAllWindows()


def process_image(image_path):
    # 讀取照片
    image = cv2.imread(image_path)

    # 旋轉 90 度
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite('rotated_image.jpg', rotated_image)

    # 水平翻轉
    flipped_image = cv2.flip(image, 1)
    cv2.imwrite('flipped_image.jpg', flipped_image)

    # 轉為灰階圖片
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_image.jpg', gray_image)

    print("影像處理完成並儲存：rotated_image.jpg, flipped_image.jpg, gray_image.jpg")


def detect_and_record_faces():
    # 加載人臉偵測模型
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    if not cap.isOpened():
        print("無法開啟相機")
        return

    print("按下 'q' 退出錄影")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("無法讀取相機影像")
            break

        # 轉為灰階以進行人臉偵測
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # 擷取人臉區域並進行馬賽克處理
            face = frame[y:y+h, x:x+w]
            face = cv2.GaussianBlur(face, (99, 99), 30)
            frame[y:y+h, x:x+w] = face

        # 寫入錄製影片
        out.write(frame)
        cv2.imshow('Face Detection with Mosaic', frame)

        if cv2.waitKey(1) == ord('q'):  # 按下 'q' 退出
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("錄影已保存為 output.avi")


# 主程序
if __name__ == "__main__":
    print("選擇模式：")
    print("1: 開啟相機並拍照處理")
    print("2: 即時偵測人臉並錄影")
    mode = input("請輸入模式編號 (1 or 2): ")

    if mode == "1":
        capture_and_process()
    elif mode == "2":
        detect_and_record_faces()
    else:
        print("無效選擇")
