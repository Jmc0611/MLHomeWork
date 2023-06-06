import os

# 遍历文件夹中的所有txt文件
for root, dirs, files in os.walk(r'C:\Users\14403\Desktop\FedSTAR2\CASIA\splits'):
    for file in files:
        if file.endswith('.txt'):
            # 读取txt文件内容
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
            # 将反斜杠替换为正斜杠
            content = content.replace('\\', '/')
            # 将修改后的内容写回txt文件
            with open(os.path.join(root, file), 'w') as f:
                f.write(content)
