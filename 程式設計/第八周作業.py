import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle, Polygon, Ellipse

# 創建畫布
fig, ax = plt.subplots(figsize=(8, 8))

# 設定背景為白色
ax.set_facecolor('white')

# 繪製南瓜主體（三個分開的橢圓）
# 左邊的橢圓
left_ellipse = Ellipse((0.35, 0.45), 0.35, 0.6, angle=8, color='#FFA500')
ax.add_patch(left_ellipse)

# 中間的橢圓
middle_ellipse = Ellipse((0.5, 0.45), 0.33, 0.58, angle=0, color='#FFA500')
ax.add_patch(middle_ellipse)

# 右邊的橢圓
right_ellipse = Ellipse((0.65, 0.45), 0.35, 0.6, angle=-8, color='#FFA500')
ax.add_patch(right_ellipse)

# 繪製南瓜梗（梯形）
stem = Polygon([
    [0.47, 0.74],  # 左下
    [0.53, 0.74],  # 右下
    [0.54, 0.88],  # 右上
    [0.46, 0.88]   # 左上
], color='green')
ax.add_patch(stem)

# 計算正三角形的高度
triangle_side = 0.12  # 三角形邊長
triangle_height = triangle_side * np.sqrt(3) / 2

# 繪製左眼（正三角形）
left_eye_x = 0.32  # 更靠左
left_eye_y = 0.5
left_eye = Polygon([
    [left_eye_x, left_eye_y],  # 底部左點
    [left_eye_x + triangle_side, left_eye_y],  # 底部右點
    [left_eye_x + triangle_side/2, left_eye_y + triangle_height]  # 頂點
], color='black')
ax.add_patch(left_eye)

# 繪製右眼（正三角形）
right_eye_x = 0.56  # 更靠右
right_eye = Polygon([
    [right_eye_x, left_eye_y],  # 底部左點
    [right_eye_x + triangle_side, left_eye_y],  # 底部右點
    [right_eye_x + triangle_side/2, left_eye_y + triangle_height]  # 頂點
], color='black')
ax.add_patch(right_eye)

# 繪製鼻子（小正三角形）
nose_side = 0.08  # 鼻子三角形邊長
nose_height = nose_side * np.sqrt(3) / 2
nose_x = 0.46
nose_y = 0.43
nose = Polygon([
    [nose_x, nose_y],  # 底部左點
    [nose_x + nose_side, nose_y],  # 底部右點
    [nose_x + nose_side/2, nose_y + nose_height]  # 頂點
], color='black')
ax.add_patch(nose)

# 繪製嘴巴（船型/梯形）
mouth = Polygon([
    [0.35, 0.37],  # 左上（上移）
    [0.65, 0.37],  # 右上（上移）
    [0.55, 0.30],  # 右下（上移）
    [0.45, 0.30]   # 左下（上移）
], color='black')
ax.add_patch(mouth)

# 設定坐標軸範圍
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# 隱藏坐標軸
ax.axis('off')

# 保持圖形比例
plt.axis('equal')

# 顯示圖形
plt.show()