import pandas as pd
import json
import numpy as np
from tkinter import Tk, filedialog

# 创建 Tkinter 根窗口（不显示）
root = Tk()
root.withdraw()

# 打开文件对话框让用户选择 Excel 文件
file_path = filedialog.askopenfilename(
    title="选择 Excel 文件",
    filetypes=[("Excel files", "*.xlsx")]
)

if file_path:
    # 读取 Excel 文件
    df = pd.read_excel(file_path)

    # 确保 SKU 列的数据类型为字符串
    if 'SKU' in df.columns:
        df['SKU'] = df['SKU'].astype(str)

    # 将 DataFrame 转换为字典列表
    data = df.replace({np.nan: None}).to_dict(orient='records')

    # 将字典列表保存为 JSON 文件
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("转换成功，JSON 文件已保存。")
else:
    print("没有选择文件。")

