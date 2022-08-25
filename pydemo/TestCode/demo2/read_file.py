with open(r"./data_file/user_info.txt",'r') as user_info:
    data = user_info.readlines()

users=[]
for line in data:
    user  = line[:-1].split(":")
    users.append(user)

print(users)