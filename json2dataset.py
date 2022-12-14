import os
files = os.listdir('./') #返回指定文件夾下的所有檔案名稱
#files.remove('json2dataset.py')
for i in range(len(files)):
    if files[i].endswith(".json"):
        os.system('labelme_json_to_dataset'+files[i])