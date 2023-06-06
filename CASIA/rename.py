# import os
#
# folder_path = r"C:\Users\14403\Desktop\FedSTAR2\speech_commands\angry"
# file_names = os.listdir(folder_path)
#
# # 初始化记录计数器
# count = 1
#
# # 遍历文件名列表，逐一修改文件名
# for i in range(len(file_names)):
#     old_name = os.path.join(folder_path, file_names[i])
#     base_name, file_ext = os.path.splitext(file_names[i])
#     new_name = os.path.join(folder_path, f"{count}{file_ext}")
#
#     # 如果新文件名已经存在，则在文件名后添加一个数字
#     while os.path.exists(new_name):
#         count += 1
#         new_name = os.path.join(folder_path, f"{count}{file_ext}")
#
#     os.rename(old_name, new_name)
#     print(f"{old_name} -> {new_name}")
#
#     # 更新计数器
#     count += 1

import os

# 指定文件路径
path = r'C:\Users\14403\Desktop\FedSTAR2\speech_commands\ZhaoZuoxiang\surprise'

# 获取文件夹内文件的名字和路径
files = os.listdir(path)

# 定义文件的初始编号
counter = 1

# 遍历文件夹中的所有文件
for file_name in files:
    # 分离文件名和扩展名
    name, extension = os.path.splitext(file_name)

    # 只对.wav文件进行重命名
    if extension == '.wav':
        # 以新的文件名命令文件
        os.rename(os.path.join(path, file_name), os.path.join(path, '4_' + str(counter) + extension))

        # 更新计数器
        counter += 1
