from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import os

# 切換到工作目錄
os.chdir("c:/Users/user/Desktop/林均融/程式/程式設計 week11 機器學習")

# 加載前處理後的資料
X_train = pd.read_csv('X_train_processed.csv')
y_train = pd.read_csv('y_train_processed.csv').squeeze()  # 將 DataFrame 轉為 Series
X_test = pd.read_csv('X_test_processed.csv')

# 分割訓練集和驗證集
X_train_part, X_valid, y_train_part, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# ===========================================
# 羅吉斯回歸模型
# ===========================================
# 建立羅吉斯回歸模型
logistic_model = LogisticRegression()
logistic_model.fit(X_train_part, y_train_part)

# 驗證羅吉斯回歸模型
y_pred_logistic = logistic_model.predict(X_valid)

# 評估羅吉斯回歸模型
accuracy_logistic = accuracy_score(y_valid, y_pred_logistic)
precision_logistic = precision_score(y_valid, y_pred_logistic)
recall_logistic = recall_score(y_valid, y_pred_logistic)
f1_logistic = f1_score(y_valid, y_pred_logistic)

print(f"羅吉斯回歸模型評估：\nAccuracy: {accuracy_logistic:.4f}, Precision: {precision_logistic:.4f}, Recall: {recall_logistic:.4f}, F1-score: {f1_logistic:.4f}")

# 羅吉斯回歸混淆矩陣
cm_logistic = confusion_matrix(y_valid, y_pred_logistic)

# ===========================================
# 決策樹模型
# ===========================================
# 建立決策樹模型
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train_part, y_train_part)

# 驗證決策樹模型
y_pred_tree = tree_model.predict(X_valid)

# 評估決策樹模型
accuracy_tree = accuracy_score(y_valid, y_pred_tree)
precision_tree = precision_score(y_valid, y_pred_tree)
recall_tree = recall_score(y_valid, y_pred_tree)
f1_tree = f1_score(y_valid, y_pred_tree)

print(f"決策樹模型評估：\nAccuracy: {accuracy_tree:.4f}, Precision: {precision_tree:.4f}, Recall: {recall_tree:.4f}, F1-score: {f1_tree:.4f}")

# 決策樹混淆矩陣
cm_tree = confusion_matrix(y_valid, y_pred_tree)

# ===========================================
# 並排顯示混淆矩陣
# ===========================================
fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # 創建1行2列的子圖

# 羅吉斯回歸混淆矩陣圖
disp_logistic = ConfusionMatrixDisplay(confusion_matrix=cm_logistic, display_labels=[0, 1])
disp_logistic.plot(cmap="Blues", ax=axes[0], colorbar=False)
axes[0].set_title("Logistic Regression Confusion Matrix")

# 決策樹混淆矩陣圖
disp_tree = ConfusionMatrixDisplay(confusion_matrix=cm_tree, display_labels=[0, 1])
disp_tree.plot(cmap="Greens", ax=axes[1], colorbar=False)
axes[1].set_title("Decision Tree Confusion Matrix")

# 顯示圖表
plt.tight_layout()
plt.show()
