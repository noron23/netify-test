import cv2
import numpy as np

# 啟用攝影機
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("無法啟用攝影機")
    exit()

# 拍照
print("按下空白鍵拍照...")
while True:
    ret, frame = cap.read()
    if not ret:
        print("無法讀取影像")
        break

    cv2.imshow("Live View", frame)

    # 按空白鍵拍照
    if cv2.waitKey(1) & 0xFF == ord(' '):
        captured_image = frame.copy()
        print("拍照完成")
        break

# 關閉攝影機
cap.release()
cv2.destroyAllWindows()

# 儲存原始圖片
cv2.imwrite("original_image.jpg", captured_image)

# 向左旋轉60度
rows, cols = captured_image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 60, 1)
rotated_image = cv2.warpAffine(captured_image, rotation_matrix, (cols, rows))

# 水平垂直翻轉
flipped_image = cv2.flip(captured_image, -1)

# 轉灰階
grayscale_image = cv2.cvtColor(captured_image, cv2.COLOR_BGR2GRAY)

# 轉HSV
hsv_image = cv2.cvtColor(captured_image, cv2.COLOR_BGR2HSV)

# 馬賽克處理
def pixelate_image(image, pixel_size=10):
    height, width = image.shape[:2]
    temp = cv2.resize(image, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

mosaic_image = pixelate_image(captured_image, pixel_size=20)

# 儲存結果
cv2.imwrite("rotated_image.jpg", rotated_image)
cv2.imwrite("flipped_image.jpg", flipped_image)
cv2.imwrite("grayscale_image.jpg", grayscale_image)
cv2.imwrite("hsv_image.jpg", hsv_image)
cv2.imwrite("mosaic_image.jpg", mosaic_image)

print("影像處理完成，結果已儲存")

# 顯示所有處理結果
cv2.imshow("Original Image", captured_image)
cv2.imshow("Rotated Image", rotated_image)
cv2.imshow("Flipped Image", flipped_image)
cv2.imshow("Grayscale Image", grayscale_image)
cv2.imshow("HSV Image", hsv_image)
cv2.imshow("Mosaic Image", mosaic_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
