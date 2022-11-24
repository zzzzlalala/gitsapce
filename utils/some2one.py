# coding: utf-8
# @Time : 2022/11/23 16:05
import os
# path = r'../1/democracy-in-hong-kong-under-attack.txt'  # 文本存放的路径
def xiugai(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # 读取每一行
    a = ''  # 空字符（中间不加空格）
    for line in lines:
        a += line.strip()  # strip()是去掉每行末尾的换行符\n 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(a)

path = r"E:\workspace\utils\volexity_txt"
names = []
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.splitext(file_path)[1] == '.txt':
        names.append(file_path)
for name in names:
    xiugai(name)
