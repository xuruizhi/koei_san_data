import pandas as pd
from pypinyin import lazy_pinyin, Style

# 读取Excel文件
input_file = '人物.xlsx'  # 输入文件路径
df = pd.read_excel(input_file)


# 假设第一列需要转换为拼音，这里检查是否为字符串并转换
def get_pinyin(text):
    if isinstance(text, str):  # 确保是字符串
        return ' '.join(lazy_pinyin(text, style=Style.TONE))
    else:
        return text  # 如果不是字符串，则直接返回原值


# 对第一列应用get_pinyin函数并将结果存储在新列中
df.insert(1, '拼音', df.iloc[:, 0].apply(get_pinyin))

# 输出到新的Excel文件
output_file = 'output_with_pinyin.xlsx'
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"带有拼音的Excel文件已保存为: {output_file}")
