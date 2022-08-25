import os

def list_file_walk(path):
   file_list = []
   for root, dirs, files in os.walk(path):
       for file in files:
           file_path = os.path.join(root, file)
           file_list.append(file_path)
   return file_list


print(list_file_walk(r'e:\TestCode\demo'))