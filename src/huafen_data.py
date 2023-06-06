import os

data_dir = r"C:\Users\14403\Desktop\FedSTAR2\speech_commands"  # 数据集所在目录的路径

# 获取数据集中的所有文件夹和文件名
folders = os.listdir(data_dir)

import shutil

train_dir = r"C:\Users\14403\Desktop\FedSTAR2\src\train"  # 训练集目录的路径
test_dir = r"C:\Users\14403\Desktop\FedSTAR2\src\test"  # 测试集目录的路径

# 创建训练集和测试集目录
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# 复制所有文件夹到训练集和测试集目录中
for folder in folders:
    folder_path = os.path.join(data_dir, folder)
    train_folder_path = os.path.join(train_dir, folder)
    test_folder_path = os.path.join(test_dir, folder)
    os.makedirs(train_folder_path, exist_ok=True)
    os.makedirs(test_folder_path, exist_ok=True)
    files = os.listdir(folder_path)
    for file in files:
        src_file = os.path.join(folder_path, file)
        train_file = os.path.join(train_folder_path, file)
        test_file = os.path.join(test_folder_path, file)
        if os.path.isfile(src_file):
            if hash(file) % 10 < 8:  # 将80%的文件复制到训练集目录中
                shutil.copy(src_file, train_file)
            else:  # 将20%的文件复制到测试集目录中
                shutil.copy(src_file, test_file)
