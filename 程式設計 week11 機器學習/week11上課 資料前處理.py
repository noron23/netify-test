import pandas as pd
from sklearn.preprocessing import StandardScaler
import os
os.chdir("c:/Users/user/Desktop/林均融/程式/程式設計 week11 機器學習")


# 加載資料
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# 缺失值處理
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)
train_data.drop(['Cabin'], axis=1, inplace=True)

test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)
test_data.drop(['Cabin'], axis=1, inplace=True)

# 類別標籤轉換
train_data['Sex'] = train_data['Sex'].map({'male': 1, 'female': 0})
test_data['Sex'] = test_data['Sex'].map({'male': 1, 'female': 0})

train_data = pd.get_dummies(train_data, columns=['Embarked'], drop_first=True)
test_data = pd.get_dummies(test_data, columns=['Embarked'], drop_first=True)

# 標準化
scaler = StandardScaler()
num_features = ['Age', 'Fare']
train_data[num_features] = scaler.fit_transform(train_data[num_features])
test_data[num_features] = scaler.transform(test_data[num_features])

# 移除無用欄位
train_data.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
test_data.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

# 分離特徵和標籤
X_train = train_data.drop('Survived', axis=1)
y_train = train_data['Survived']
X_test = test_data

# 檢查結果
print("訓練特徵：", X_train.head())
print("訓練標籤：", y_train.head())
print("測試特徵：", X_test.head())

# 保存處理後的訓練和測試資料
X_train.to_csv('X_train_processed.csv', index=False)
y_train.to_csv('y_train_processed.csv', index=False)
X_test.to_csv('X_test_processed.csv', index=False)
