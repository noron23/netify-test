# 匯入必要的套件
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# 1. 載入乳癌資料集
data = load_breast_cancer()
X, y = data.data, data.target
feature_names = data.feature_names
target_names = data.target_names

# 建立 DataFrame，方便檢視資料
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# 印出前 10 筆資料
print("前 10 筆資料：")
print(df.head(10))

# 2. 資料前處理
# 將資料分成訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 特徵標準化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. 訓練模型
# (1) 羅吉斯回歸
logistic_model = LogisticRegression(random_state=42)
logistic_model.fit(X_train_scaled, y_train)
logistic_preds = logistic_model.predict(X_test_scaled)

# (2) 決策樹
decision_tree_model = DecisionTreeClassifier(random_state=42)
decision_tree_model.fit(X_train, y_train)
decision_tree_preds = decision_tree_model.predict(X_test)

# 4. 模型評估
# 定義評估函數
def evaluate_model(name, y_true, y_pred):
    print(f"模型：{name}")
    print(f"準確率 (Accuracy): {accuracy_score(y_true, y_pred):.2f}")
    print(f"精確率 (Precision): {precision_score(y_true, y_pred):.2f}")
    print(f"召回率 (Recall): {recall_score(y_true, y_pred):.2f}")
    print(f"F1 分數: {f1_score(y_true, y_pred):.2f}")
    print("-" * 30)

# 評估羅吉斯回歸
evaluate_model("羅吉斯回歸", y_test, logistic_preds)

# 評估決策樹
evaluate_model("決策樹", y_test, decision_tree_preds)

# 5. 混淆矩陣圖
logistic_cm = confusion_matrix(y_test, logistic_preds)
decision_tree_cm = confusion_matrix(y_test, decision_tree_preds)

# 繪製混淆矩陣圖
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ConfusionMatrixDisplay(logistic_cm, display_labels=target_names).plot(ax=ax[0], cmap='Blues')
ax[0].set_title("羅吉斯回歸 - 混淆矩陣")
ConfusionMatrixDisplay(decision_tree_cm, display_labels=target_names).plot(ax=ax[1], cmap='Blues')
ax[1].set_title("決策樹 - 混淆矩陣")
plt.tight_layout()
plt.show()
