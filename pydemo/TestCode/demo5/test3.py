file = open(r'E:/1.txt', mode = 'w+', encoding = 'UTF-8')
# open()打开一个文件，返回一个文件对象
file.write('Hello!\nWoodman')  # 写入文件
file.seek(0)  # 光标移动到文件开头
file_content = file.read()  # 读取整个文件内容
print(file_content)
file.close() # 关闭文件