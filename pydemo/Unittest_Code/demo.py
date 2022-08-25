import csv
import codecs
from itertools import islice

with codecs.open("baidu_data.csv", "r", "gbk") as f:
    list = []
    data = csv.reader(f)
    for line in islice(data, 1, None):
        list.append(line)
        print(list)

    # print(list)