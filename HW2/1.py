import pandas as pd

# 載入 CSV 文件
df = pd.read_csv('IT_submission.csv')

# 顯示前幾筆資料
print(df.head())

# 檢查資料的資訊
print(df.info())

# 確認是否有 PassengerId 重複的情況
print("重複的 PassengerId 數量：", df['PassengerId'].duplicated().sum())

# 檢查 Survived 欄位是否只包含 0 或 1
print("Survived 欄位的唯一值：", df['Survived'].unique())