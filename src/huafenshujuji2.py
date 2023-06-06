import os

train_dir = r'C:\Users\14403\Desktop\FedSTAR2\CASIA\train'
test_dir = r'C:\Users\14403\Desktop\FedSTAR2\CASIA\test'

# 生成训练集文件索引
with open(r'C:\Users\14403\Desktop\FedSTAR2\CASIA\splits\train_list.txt', 'w') as f:
    for foldername in os.listdir(train_dir):
        folder_path = os.path.join(train_dir, foldername)
        for filename in os.listdir(folder_path):
            label = foldername  # 文件夹名作为标签
            new_filename = os.path.join(foldername, filename)
            f.write(f'{new_filename}\n')

# 生成测试集文件索引
with open(r'C:\Users\14403\Desktop\FedSTAR2\CASIA\splits\test_list.txt', 'w') as f:
    for foldername in os.listdir(test_dir):
        folder_path = os.path.join(test_dir, foldername)
        for filename in os.listdir(folder_path):
            label = foldername  # 文件夹名作为标签
            new_filename = os.path.join(foldername, filename)
            f.write(f'{new_filename}\n')
