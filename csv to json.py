import pandas as pd

# 讀取 CSV 檔案
csv_file = '2330.csv'
df = pd.read_csv(csv_file)

# 將資料轉換成 JSON 格式
json_data = df.to_json(orient='records', force_ascii=False, indent=4)

# 將 JSON 資料寫入新的檔案
json_file = '2330.json'
with open(json_file, 'w', encoding='utf-8') as f:
    f.write(json_data)

print(f"已成功將 {csv_file} 轉換成 {json_file}")