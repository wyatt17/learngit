import csv
import codecs
from itertools import islice

# 读取本地 CSV 文件
data = csv.reader(codecs.open('./data_file/user_info.csv', 'r', 'utf_8_sig'))

# 存放用户数据
users1 = []

# 循环输出每行信息
for line in islice(data, 1, None):
    users1.append(line)

# 打印
print(users1)